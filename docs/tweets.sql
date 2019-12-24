CREATE TABLE tweets (
  source VARCHAR, 
  text VARCHAR, 
  created_at DATETIME, 
  retweet_count INTEGER, 
  favorite_count INTEGER, 
  id_str INTEGER NOT NULL, 
  PRIMARY KEY (id_str)
);