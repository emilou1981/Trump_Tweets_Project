#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from datetime import datetime

from sklearn.feature_extraction.text import CountVectorizer

start_dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(f'Starting phrases at: {start_dt}')


import sqlalchemy
#from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

# Create an engine for the  database

engine = create_engine("sqlite:///../data/data.sqlite", echo=False)
conn = engine.connect()


tweet_df = pd.read_csv('../data/tweet_only.csv')
tweet_list = tweet_df.text.tolist()


stop_words = ['00', 'zzl2sc29dn', 'zzkh5cmnxy', 'zz41akot6q', 'zyrctsfmsq', 'zyezhe',              'zxurhtdtqq', 'zxl6syiwdm', 'zx9sj0quzn', 'http', 'https', '000', '000 000']


#vectorizer = CountVectorizer(ngram_range=(2,4), stop_words='english')
vectorizer = CountVectorizer(ngram_range=(2,3), stop_words=stop_words)


tf = vectorizer.fit_transform(tweet_list)


res = pd.Series(np.ravel((vectorizer.transform(tweet_list).sum(axis=0))), index=vectorizer.get_feature_names())

df = pd.DataFrame({'phrase':res.index, 'cnt_phrase':res.values})


df.to_csv('../data/phrase_cnt.csv', index=False)


df.to_sql('phrases',conn, if_exists='replace', index=False)


# Compact/compress db after working on it.
engine.execute("VACUUM")


conn.close
end_dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(f'END OF phrases at: {end_dt}')
print("")
