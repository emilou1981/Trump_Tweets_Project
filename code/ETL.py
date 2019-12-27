#!/usr/bin/env python
# coding: utf-8


import pandas as pd
from datetime import datetime

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import func, inspect
from sqlalchemy import Table, Column, Integer, String, Float, DateTime, MetaData



start_dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(f'Starting ETL at: {start_dt}')


# Create an engine for the  sqlite database

engine = create_engine("sqlite:///../data/data.sqlite", echo=False)
conn = engine.connect()

# Reflect Database into ORM classes
Base = automap_base()
Base.prepare(engine, reflect=True)
meta = MetaData()


filename = "../data/Trump_Tweets_01012015_12182019.json"
tweets_df = pd.read_json(filename, orient='columns', encoding='utf-8')
tweets_df.head()



retweets = tweets_df[tweets_df["is_retweet"] == 1.0]
own_tweets = tweets_df[tweets_df["is_retweet"] == 0.0]
retweets.head()



#own_tweets.head()



own_tweets = own_tweets.drop(columns=['is_retweet'])
#own_tweets.head()



retweets = retweets.drop(columns=['is_retweet'])
retweets.head()



tweets = Table(
   'tweets', meta, 
    Column('source',String), 
    Column('text', String), 
    Column('created_at', DateTime),
    Column('retweet_count', Integer),
    Column('favorite_count', Integer),
    Column('id_str', Integer, primary_key = True)
)



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


#- bind engine, then drop all tables, create all tables
#- this gives us PKEY's
meta.bind = engine
meta.drop_all()
meta.create_all()

# Write to the database.  We use append, this preserves the PKEY
own_tweets.to_sql('tweets', conn, if_exists='append', index=False, index_label="id_str")
retweets.to_sql('retweets', conn, if_exists='append', index=False, index_label="id_str")


# Compact/compress db after working on it.
engine.execute("VACUUM")

# Close the connection
conn.close


df_tweets_only = own_tweets['text']


df_tweets_only.to_csv('../data/tweet_only.csv', index=False, header=['text'])


end_dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(f'ETL END at: {end_dt}')
print('') # print empty line

