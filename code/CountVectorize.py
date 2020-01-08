#!/usr/bin/env python
# coding: utf-8

# vector and count the words in tweets.


from sklearn.feature_extraction.text import CountVectorizer



import pandas as pd
from datetime import datetime

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import func, inspect
from sqlalchemy import Table, Column, Integer, String, Float, DateTime, MetaData



start_dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(f'Starting CountVectorize at: {start_dt}')

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



#- select column 'text' from the tweets table - this has no retweets
tweets_text_data = pd.read_sql('SELECT TEXT FROM TWEETS', conn)


tweets = tweets_text_data.text


from sklearn.feature_extraction import text 

# define additonal stop words to add to english stop words.
my_additional_stop_words = ['https','http', 'rt', '00', '000', '005', '00a', '00am',
        '00ame', '00p', '00pm', 'amp', 'realdonaldtrump', 'donald', 'trump', 'president']

stop_words = text.ENGLISH_STOP_WORDS.union(my_additional_stop_words)

# Instantiate Count Vectorizer
vectorizer = CountVectorizer( lowercase=True, stop_words=stop_words)

vector_text = tweets

# To actually create the vectorizer, we simply need to call fit on the text
# data that we wish to fix
cv_fit = vectorizer.fit_transform(vector_text)


words = vectorizer.vocabulary_

# get the feature names (words)
feature_names = vectorizer.get_feature_names()

# get the count for the words
feature_counts = cv_fit.toarray().sum(axis=0)


final_count_df = pd.DataFrame({"word": feature_names, "cnt_word": feature_counts})
final_count_df.sort_values(by='cnt_word', ascending=False)


final_count_df.to_csv('../data/final_word_count.csv', index=False)

end_dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(f'END OF CountVectorize at: {end_dt}')
print('') # print empty line