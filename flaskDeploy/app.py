import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


#################################################
# Database Setup
#################################################

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/data.sqlite"
db = SQLAlchemy(app)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
# Base.prepare(db.engine, reflect=True)
Base.prepare(db.engine, reflect=True)
print("Echo out keyes")
print(Base.classes.keys())
# Save references to each table
Tweets = Base.classes.tweets
Retweets = Base.classes.retweets
Phrases  = Base.classes.phrases
Word_Counts = Base.classes.word_counts
Sentiment = Base.classes.sentiment


# print(Nmbr_Events)
# print(db.session.query(Nmbr_Events.STATE).all())

@app.route("/")
def index():
    print("This should print in the console")
    """Return the homepage."""
    return render_template("index.html")

@app.route("/header")
def header():
    return render_template("page_header.html")

@app.route("/search_results")
def search_results():
    return render_template("search_results.html")   

@app.route("/bubble_word")
def bubble_word():
    return render_template("bubble_word.html")

@app.route("/bubble_phrase_cnt")
def bubble_phrase_cnt():
    return render_template("bubble_phrase_cnt.html")  

@app.route("/market_impact")
def market_impact():
    return render_template("market_impact.html")   

@app.route("/twitter_data")
def twitter_data():
    return render_template("data.html")      

@app.route("/api/tweets/")
def tweets():
    sel = [Tweets.source, Tweets.text, Tweets.created_at, Tweets.retweet_count, Tweets.favorite_count, Tweets.id_str]
    results = db.session.query(*sel).all()

    all_results = []
    for source, text, created_at, retweet_count, favorite_count, id_str in results:
        results_dict = {}
        results_dict["source"] = source
        results_dict["text"] = text
        results_dict["created_at"] = created_at
        results_dict["retweet_count"] = retweet_count
        results_dict["favorite_count"] = favorite_count
        results_dict["id_str"] = id_str
        all_results.append(results_dict)
    
    return jsonify(all_results)    


@app.route("/api/retweets/")
def retweets():
    sel = [Retweets.source, Retweets.text, Retweets.created_at, Retweets.retweet_count, Retweets.favorite_count, Retweets.id_str]
    results = db.session.query(*sel).all()

    all_results = []
    for source, text, created_at, retweet_count, favorite_count, id_str in results:
        results_dict = {}
        results_dict["source"] = source
        results_dict["text"] = text
        results_dict["created_at"] = created_at
        results_dict["retweet_count"] = retweet_count
        results_dict["favorite_count"] = favorite_count
        results_dict["id_str"] = id_str
        all_results.append(results_dict)
    
    return jsonify(all_results)    



@app.route("/api/wordcnt/")
def wordcnt():
    sel = [Word_Counts.word, Word_Counts.cnt_word]
    results = db.session.query(*sel).order_by(Word_Counts.cnt_word.desc()).limit(50)

    all_results = []

    for _word_, _cnt_word_ in results:
        results_dict = {}
        results_dict["word"] = _word_
        results_dict["cnt_word"] = _cnt_word_
        all_results.append(results_dict)
    
    return jsonify(all_results)

@app.route("/api/phrasecnt/")
def phrasecnt():
    sel = [Phrases.phrase_pkey, Phrases.phrase, Phrases.cnt_phrase]
    results = db.session.query(*sel).order_by(Phrases.cnt_phrase.desc()).limit(50)


    all_results = []
    for phrase_pkey, phrase, cnt_phrase in results:
        results_dict = {}
        results_dict["phrase_pkey"] = phrase_pkey
        results_dict["phrase"] = phrase
        results_dict["cnt_phrase"] = cnt_phrase
        all_results.append(results_dict)
    
    return jsonify(all_results)


@app.route("/api/searchtweets/<searchpattern>")
def searchtweets(searchpattern):
    # print(f'Search Pattern: {searchpattern}')


    sel = [Tweets.source, Tweets.text, Tweets.created_at, Tweets.retweet_count, Tweets.favorite_count, Tweets.id_str]
    s_str = f'%{searchpattern}%'
    results = db.session.query(*sel).filter(Tweets.text.like(s_str)).all()

    all_results = []
    for source, text, created_at, retweet_count, favorite_count, id_str in results:
        results_dict = {}
        results_dict["source"] = source
        results_dict["text"] = text
        results_dict["created_at"] = created_at
        results_dict["retweet_count"] = retweet_count
        results_dict["favorite_count"] = favorite_count
        results_dict["id_str"] = id_str
        all_results.append(results_dict)
    
    return jsonify(all_results)    


if __name__ == "__main__":
    app.run(debug=True)
