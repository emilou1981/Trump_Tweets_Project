#!/usr/bin/env python
# coding: utf-8

# # load to db, output of Test.py (to be renamed) - files

# test.py outputs files to outputdir in format part-00000 ... part-nnnnn
#   - file line: "0"	3
# Tab delimited file.
# 
# read all files to dataframe, process, load table word_counts with results.
# 


import pandas as pd
import glob
from datetime import datetime

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import func, inspect
from sqlalchemy import Table, Column, Integer, String, Float, DateTime, MetaData


start_dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(f'Starting load_word_count_to_db at: {start_dt}')


colnames = ['word', 'cnt_word']
l = [pd.read_csv(filename, sep="\t", names=colnames, header=None) for filename in glob.glob("../outputdir/part-*")]
df = pd.concat(l, axis=0, sort=False)


# Create an engine for the database

engine = create_engine("sqlite:///../data/data.sqlite", echo=False)
conn = engine.connect()


# Reflect Database into ORM classes
Base = automap_base()
Base.prepare(engine, reflect=True)
meta = MetaData()


word_counts = Table(
   'word_counts', meta, 
    Column('word',String), 
    Column('cnt_word', Integer)
)


# REPLACING, never updating if exists.
df.to_sql('word_counts', conn, if_exists='replace', index=False)


# Compact/compress db after working on it.
engine.execute("VACUUM")


conn.close()


end_dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(f'END OF load_word_count_to_db at: {end_dt}')
print('') # print empty line

