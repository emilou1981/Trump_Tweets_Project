# Extract Translate Load

From the website http://www.trumptwitterarchive.com/archive we downloaded a json of tweets using the date range January 1, 2015 through December 18, 2019. This file had the following fields:

`source, text, created_at, retweet_count, favorite_count, is_retweet, id_str`

**ETL:** Using python, sqlalchemy, we split out tweets and retweets and load tables ‘tweets’, ‘retweets’ to sqlite database. We then save csv files for use in downstream processes that require text input.

**CountVectorize:** Using CountVectorizer we create stop words using English stop words as well as a custom list, then get the words and counts and load to the database

**Load_word_count_to_db**: load the text file of word counts to the database.

**Phrases**: Using CountVectorizer we create 2-4 word phrases with English stop words as well as custom list, get the phrases and counts and load to the database

**run_etl_load_wordCounts:** The jobs are run sequentially through this shell script