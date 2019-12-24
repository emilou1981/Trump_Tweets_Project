#!/usr/bin/env python
# coding: utf-8

# In[45]:


import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import func, inspect
from sqlalchemy import Table, Column, Integer, String, Float, DateTime, MetaData


# In[46]:


# Create an engine for the  FemaData.db database

engine = create_engine("sqlite:///../data/data.sqlite", echo=False)
conn = engine.connect()


# In[47]:


# Reflect Database into ORM classes
Base = automap_base()
Base.prepare(engine, reflect=True)
meta = MetaData()


# In[48]:


filename = "../data/Trump_Tweets_01012015_12182019.json"
tweets_df = pd.read_json(filename, orient='columns', encoding='utf-8')
tweets_df.head()


# In[49]:


retweets = tweets_df[tweets_df["is_retweet"] == 1.0]
own_tweets = tweets_df[tweets_df["is_retweet"] == 0.0]
retweets.head()


# In[50]:


own_tweets.head()


# In[51]:


own_tweets = own_tweets.drop(columns=['is_retweet'])
own_tweets.head()


# In[52]:


retweets = retweets.drop(columns=['is_retweet'])
retweets.head()


# In[53]:


tweets = Table(
   'tweets', meta, 
    Column('source',String), 
    Column('text', String), 
    Column('created_at', DateTime),
    Column('retweet_count', Integer),
    Column('favorite_count', Integer),
    Column('id_str', Integer, primary_key = True)
)


# In[54]:


# - Don't really need this data duplication.  
# Column is_retweet: 0 (zero) == No, 1 == yes

no_retweets = Table(
   'retweets', meta, 
    Column('source',String), 
    Column('text', String), 
    Column('created_at', DateTime),
    Column('retweet_count', Integer),
    Column('favorite_count', Integer),
    Column('id_str', Integer, primary_key = True)
)


# In[55]:


#- bind engine, then drop all tables
meta.bind = engine
meta.drop_all()


# In[56]:


meta.create_all()


# In[57]:


own_tweets.dtypes


# In[58]:


retweets.dtypes


# In[59]:


own_tweets.to_sql('tweets', conn, if_exists='append', index=False, index_label="id_str")
retweets.to_sql('retweets', conn, if_exists='append', index=False, index_label="id_str")


# In[60]:


# Compact/compress db after working on it.
engine.execute("VACUUM")


# In[61]:


conn.close


# In[62]:


df_tweets_only = own_tweets['text']


# In[63]:


df_tweets_only.to_csv('../data/tweet_only.csv', index=False, header=['text'])


# In[ ]:




