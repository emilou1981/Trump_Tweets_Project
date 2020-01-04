import os

import pandas as pd
import numpy as np

# import sqlalchemy
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
# engine = create_engine("sqlite:///data/femadata.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
# Base.prepare(db.engine, reflect=True)
Base.prepare(db.engine, reflect=True)
# print("Echo out keyes")
# print(Base.classes.keys())
# Save references to each table
# Samples_Metadata = Base.classes.sample_metadata
# Samples = Base.classes.samples
Tweets = Base.classes.tweets
Retweets = Base.classes.retweets
Phrases  = Base.classes.phrases
Word_Counts = Base.classes.word_counts


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

@app.route("/api/tweets/")
def tweets():
    # # x = Base.classes.nmbr_events
    # luState = request.args.get('state')

    # print(db.session.query(Word_Counts.STATE).all())
    sel = [Tweets.source, Tweets.text, Tweets.created_at, Tweets.retweet_count, Tweets.favorite_count, Tweets.id_str]
    # # session = Session(engine)
    # if not luState: # - an empty param luState will evaluate to True
    #     results = db.session.query(*sel).all()  #.order_by(Nmbr_Events.STATE.desc()).all()
    # else:
    #     # The must be a state to match on.
    #     results = db.session.query(*sel).filter(Nmbr_Events.STATE == luState).all()
    results = db.session.query(*sel).all()


    # session.close()

    # print(results)

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
    # # x = Base.classes.nmbr_events
    # luState = request.args.get('state')

    # print(db.session.query(Word_Counts.STATE).all())
    sel = [Retweets.source, Retweets.text, Retweets.created_at, Retweets.retweet_count, Retweets.favorite_count, Retweets.id_str]
    # # session = Session(engine)
    # if not luState: # - an empty param luState will evaluate to True
    #     results = db.session.query(*sel).all()  #.order_by(Nmbr_Events.STATE.desc()).all()
    # else:
    #     # The must be a state to match on.
    #     results = db.session.query(*sel).filter(Nmbr_Events.STATE == luState).all()
    results = db.session.query(*sel).all()


    # session.close()

    # print(results)

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
    # # x = Base.classes.nmbr_events
    # luState = request.args.get('state')

    # print(db.session.query(Word_Counts.STATE).all())
    sel = [Word_Counts.word, Word_Counts.cnt_word]
    # # session = Session(engine)
    # if not luState: # - an empty param luState will evaluate to True
    #     results = db.session.query(*sel).all()  #.order_by(Nmbr_Events.STATE.desc()).all()
    # else:
    #     # The must be a state to match on.
    #     results = db.session.query(*sel).filter(Nmbr_Events.STATE == luState).all()
    results = db.session.query(*sel).order_by(Word_Counts.cnt_word.desc()).limit(50)


    # session.close()

    # print(results)

    all_results = []
    # for _pkey_, _word_, _cnt_word_ in results:
    for _word_, _cnt_word_ in results:
        results_dict = {}
        # results_dict["wc_pkey"] = _pkey_
        results_dict["word"] = _word_
        results_dict["cnt_word"] = _cnt_word_
        all_results.append(results_dict)
    
    return jsonify(all_results)

@app.route("/api/phrasecnt/")
def phrasecnt():
    # # x = Base.classes.nmbr_events
    # luState = request.args.get('state')

    # print(db.session.query(Word_Counts.STATE).all())
    sel = [Phrases.phrase_pkey, Phrases.phrase, Phrases.cnt_phrase]
    # # session = Session(engine)
    # if not luState: # - an empty param luState will evaluate to True
    #     results = db.session.query(*sel).all()  #.order_by(Nmbr_Events.STATE.desc()).all()
    # else:
    #     # The must be a state to match on.
    #     results = db.session.query(*sel).filter(Nmbr_Events.STATE == luState).all()
    results = db.session.query(*sel).order_by(Phrases.cnt_phrase.desc()).limit(50)


    # session.close()

    # print(results)

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
    # # session = Session(engine)
    # if not luState: # - an empty param luState will evaluate to True
    #     results = db.session.query(*sel).all()  #.order_by(Nmbr_Events.STATE.desc()).all()
    # else:
    #     # The must be a state to match on.
    s_str = f'%{searchpattern}%'
    results = db.session.query(*sel).filter(Tweets.text.like(s_str)).all()
    # results = db.session.query(*sel).all()


    # session.close()

    # print(results)

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

# @app.route("/api/pieinfo" , methods=['GET'])
# def pieinfo():
#     #SELECT  EVENT_TYPE, count(EVENT_TYPE) as NBR_EVENT FROM all_events
#     #GROUP BY EVENT_TYPE;

#     # Get the passed in state
#     luState = request.args.get("state")

#     sel = [
#         All_Events.EVENT_TYPE
#     ]
    
#     if not luState: # evaluates to true if luState is empty
#         print('pieinfo: Is Empty')
#         ttleventcounts = db.session.query(*sel, func.count(All_Events.EVENT_TYPE)).group_by(All_Events.EVENT_TYPE).all()
#     else:
#         print('pieinfo: NOT Empty')
#         ttleventcounts = db.session.query(*sel, func.count(All_Events.EVENT_TYPE)).filter(All_Events.STATE == luState).group_by(All_Events.EVENT_TYPE).all()


  
# @app.route("/jnb1")
# def jnb1():
#     print("This should return NOAA_Data.html")
#     """Return the homepage."""
#     return render_template("NOAA_Data.html")
    
# @app.route("/jnb2")
# def jnb2():
#     print("This should return noaa_limited_load.html")
#     """Return the homepage."""
#     return render_template("noaa_limited_load.html")

if __name__ == "__main__":
    app.run(debug=True)
