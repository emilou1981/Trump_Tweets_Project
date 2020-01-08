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



# Instantiate Count Vectorizer
#vectorizer = CountVectorizer( lowercase=True, token_pattern=r'\b[^\d\W]+\b', stop_words='english')
from sklearn.feature_extraction import text 

my_additional_stop_words = ['https','http', 'rt', '00', '000', '005', '00a', '00am',
        '00ame', '00p', '00pm', 'amp', 'realdonaldtrump']

stop_words = text.ENGLISH_STOP_WORDS.union(my_additional_stop_words)
vectorizer = CountVectorizer( lowercase=True, stop_words=stop_words)

vector_text = tweets

# To actually create the vectorizer, we simply need to call fit on the text
# data that we wish to fix
cv_fit = vectorizer.fit_transform(vector_text)

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



words = vectorizer.vocabulary_



feature_names = vectorizer.get_feature_names()
feature_counts = cv_fit.toarray().sum(axis=0)



final_count_df = pd.DataFrame({"word": feature_names, "cnt_word": feature_counts})
final_count_df.sort_values(by='cnt_word', ascending=False)


final_count_df.to_csv('../data/final_word_count.csv', index=False)

end_dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(f'END OF CountVectorize at: {end_dt}')
print('') # print empty line