#!/usr/bin/env python
# coding: utf-8

# write out json of tweet text in format text: values


import pandas as pd
from datetime import datetime

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine


start_dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(f'Starting write_json_4bubbles at: {start_dt}')


engine = create_engine("sqlite:///../data/data.sqlite", echo=False)
conn = engine.connect()


df = pd.read_sql('SELECT * FROM TWEETS', conn)


df.to_json('../data/tweets_grid.json', orient='records', lines=True)


end_dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(f'END OF write_json_4bubbles at: {end_dt}')