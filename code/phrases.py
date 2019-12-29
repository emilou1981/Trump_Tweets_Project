
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from datetime import datetime

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import func, inspect
from sqlalchemy import Table, Column, Integer, String, Float, DateTime, MetaData


start_dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(f'Starting phrases at: {start_dt}')


# Create an engine for the  database
engine = create_engine("sqlite:///../data/data.sqlite", echo=False)
conn = engine.connect()


# Reflect Database into ORM classes
Base = automap_base()
Base.prepare(engine, reflect=True)
meta = MetaData()


tweet_df = pd.read_csv('../data/tweet_only.csv')


tweet_list = tweet_df.text.tolist()


#- optional manual list of stop words.
stop_words = ['00', 'zzl2sc29dn', 'zzkh5cmnxy', 'zz41akot6q', 'zyrctsfmsq', 'zyezhe', 'zxurhtdtqq', 'zxl6syiwdm', 'zx9sj0quzn', 'http', 'https', '000', '000 000', 'at']


vectorizer = CountVectorizer(ngram_range=(2,4), stop_words='english') #- use built in stop words
#vectorizer = CountVectorizer(ngram_range=(2,3), stop_words=stop_words) #- use manual stop words


tf = vectorizer.fit_transform(tweet_list)


#- get results
res = pd.Series(np.ravel((vectorizer.transform(tweet_list).sum(axis=0))), index=vectorizer.get_feature_names())


df = pd.DataFrame({'phrase':res.index, 'cnt_phrase':res.values})


df.to_csv('../data/phrase_cnt.csv', index=False)


phrases = Table(
    'phrases', meta, 
    Column('phrase_pkey', Integer, primary_key=True),
    Column('phrase',String), 
    Column('cnt_phrase', Integer)
)


meta.bind = engine
meta.drop_all()


meta.create_all()


pk_nums = list(range(1,len(df) + 1))


df.insert(0, "phrase_pkey", pk_nums)


df.to_sql('phrases',conn, if_exists='append', index=False)

# compact the database
engine.execute("VACUUM")


# close the connection
conn.close

end_dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(f'END OF phrases at: {end_dt}')
print('') # print empty line


