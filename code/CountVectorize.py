#!/usr/bin/env python
# coding: utf-8

# vector and count the words in tweets.

# In[1]:


from sklearn.feature_extraction.text import CountVectorizer


# In[2]:


import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import func, inspect
from sqlalchemy import Table, Column, Integer, String, Float, DateTime, MetaData


# In[3]:


# Create an engine for the  database

engine = create_engine("sqlite:///../data/data.sqlite", echo=False)
conn = engine.connect()

# Reflect Database into ORM classes
Base = automap_base()
Base.prepare(engine, reflect=True)
meta = MetaData()

tweets = Table(
   'tweets', meta, 
    Column('source',String), 
    Column('text', String), 
    Column('created_at', DateTime),
    Column('retweet_count', Integer),
    Column('favorite_count', Integer),
    Column('id_str', Integer, primary_key = True)
)

no_retweets = Table(
   'no_retweets', meta, 
    Column('source',String), 
    Column('text', String), 
    Column('created_at', DateTime),
    Column('retweet_count', Integer),
    Column('favorite_count', Integer),
    Column('id_str', Integer, primary_key = True)
)


# In[4]:


#- select column 'text' from the tweets table - this has no retweets
tweets_text_data = pd.read_sql('SELECT TEXT FROM TWEETS', conn)


# In[5]:


tweets = tweets_text_data.text


# In[15]:


# Instantiate Count Vectorizer
#vectorizer = CountVectorizer( lowercase=True, token_pattern=r'\b[^\d\W]+\b', stop_words='english')
vectorizer = CountVectorizer( lowercase=True, stop_words='english')

vector_text = tweets

# To actually create the vectorizer, we simply need to call fit on the text
# data that we wish to fix
vectorizer.fit(vector_text)

# Now, we can inspect how our vectorizer vectorized the text
# This will print out a list of words used, and their index in the vectors
# print('Vocabulary: ')
# print(vectorizer.vocabulary_)

# # If we would like to actually create a vector, we can do so by passing the
# # text into the vectorizer to get back counts
# vector = vectorizer.transform(vector_text)

# # Our final vector:
# print('Full vector: ')
# print(vector.toarray())

# # Or if we wanted to get the vector for one word:
# print('Hot vector: ')
# print(vectorizer.transform(['hot']).toarray())

# # Or if we wanted to get multiple vectors at once to build matrices
# print('Hot and one: ')
# print(vectorizer.transform(['hot', 'one']).toarray())

# # We could also do the whole thing at once with the fit_transform method:
# print('One swoop:')
# new_text = ['Today is the day that I do the thing today, today']
# new_vectorizer = CountVectorizer()
# print(new_vectorizer.fit_transform(new_text).toarray())


# In[16]:


words = vectorizer.vocabulary_


# In[ ]:





# In[17]:


word_list = list(words.keys())


# In[18]:


word_list


# In[19]:


_word_ = {'word': word_list}


# In[20]:


word_df = pd.DataFrame(data=_word_)


# In[21]:


word_df.head()


# In[22]:


word_df.to_csv('../data/words.csv', index=False)


# In[23]:


conn.close()


# In[ ]:





# In[ ]:




