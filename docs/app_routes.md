#### @app.route("/")

​	return render_template("index.html")



#### @app.route("/bubble_word")

​	 return render_template("bubble_word.html")



#### @app.route("/bubble_phrase_cnt")

def bubble_phrase_cnt():

  return render_template("bubble_phrase_cnt.html") 



#### @app.route("/api/tweets/")

  [
    {
      "created_at": "Thu, 01 Jan 2015 06:54:59 GMT", 
      "favorite_count": 58, 
      "id_str": 550545703932796928, 
      "retweet_count": 18, 
      "source": "Twitter for Android", 
      "text": "\"@flicka__: @realDonaldTrump for president\""
    }, ...



#### @app.route("/api/retweets/")

  [
    {
    created_at: "Sun, 03 Jan 2016 04:06:35 GMT",
    favorite_count: 0,
    id_str: 683499674997796900,
    retweet_count: 1931,
    source: "Twitter for iPhone",
    text: "RT @EricTrump: So proud to be out on the campaign trail with @realDonaldTrump - thanks for an amazing night #Biloxi #Trump2016 https://t.co…"
    }, ....

#### @app.route("/api/wordcnt/")

 results = db.session.query(*sel).order_by(Word_Counts.cnt_word.desc()).limit(50)

[
  {
  cnt_word: 62,
  //wc_pkey: 1,
  word: "10"
  }, ....

#### @app.route("/api/phrasecnt/")

[
  {
    "cnt_phrase": 3, 
    "phrase": "00 00", 
    "phrase_pkey": 1
  }, 

#### @app.route("/api/searchtweets/<searchpattern>")

[
  {
  created_at: "Sat, 31 Jan 2015 02:19:56 GMT",
  favorite_count: 45,
  id_str: 561348121788416000,
  retweet_count: 27,
  source: "Twitter for Android",
  text: ""@russiannavyblog: @realDonaldTrump @ApprenticeNBC An announcement Mr Trump will run for President and fix the Obama-ruined nation?""
  },

This uses sql similar to 'select * from tweets where text LIKE %searchpattern%'