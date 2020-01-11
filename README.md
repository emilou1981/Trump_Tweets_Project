**How Trump's Use of Twitter Affects the Financial Markets**

We live in a world where people have the need to tell everyone what we are thinking, even when we shouldn't. The concept of a "filter" is disappearing which often has an effect on the people and world around us without realizing it.

 This project is analyzing Donald Trump’s twitter feed from January 1, 2015 to December 18, 2019. This period of time was select to allow for a comparison of data that is outside of his presidential campaigning and time in office.  This tweets will be compared to various economic indicators to see if there is a correlation between them.



**Our Approach**

------

Machine learning was applied to analyze the tweets by using scikit-learn libraries to determine the positive or negative sentiment of each tweet (NLTK) and determine counts for the most tweeted words and phrases (Count Vectorizer). 

Outcomes from the machine learning are used to visualize in Tableau any potential economic impacts the tweets might have on the following economic indicators:

·     SPY Large Cap ETF which tracks the S&P 500 which represents large cap stocks

·     MDY Mid Cap ETF with represents mid cap stocks

·     IGR Small Cap ETF which tracks the Russell 2000 which represents small cap stocks

·     Employment Situation monthly releases for non-farm jobs added each month

·     Real GDP Growth news releases which is represented by three estimates by quarter

 JavaScript D3.JS was used to create visualizations of the word and phrase counts and Material Design for Bootstrap was used to for search and sort functionality of the data table.



**Sentiment Analysis**

------

 When looking at the tweets that Donald Trump had made, we decided to see if they were primarily positive or negative. In order to achieve this, we searched for a dataset that applied positives and negatives to tweets. We were able to find a dataset (sentiment140) of 1.6 million tweets that had positive or negative sentiment attached to each one. With a dataset in place we were able to create our Bernoulli Naïve Bayes model which we then applied to our dataset of nearly 25,000 tweets.

The analysis of the tweets ultimately led to some surprises. One being that it classified 2/3 of the tweets as positive. Prior to the analysis, we would have thought that it would have been closer to a 50/50 split. There are a handful of factors that could have altered the results. The biggest factor likely being that our model is not 100% accurate, thus causing some of the tweets to be mislabeled. On top of this the dataset we used may not have translated well due to different diction than that of the tweets we analyzed.



**Economic Analysis**

------

##### Does the Market Respond to Trump's Tweets?

###### Trump's Tweets as Word Counts on GDP Components

Graphically, observing the stock market categorized by sizes of market capitalization, large-cap (SPY ETF), mid-cap (MDY ETF), and small-cap (IJR ETF) from January 2015 to December 2019, we see that the number of trump's tweets on components of GDP by months have both positive and negative relations to the changes in the stock markets, more so in the mid-cap stocks and large-cap stocks respectively. The words that we count include words related to trade (e.g., trade, China, tariff, dumping, etc.), market (market, stock, gdp, etc.) and tax. The market in relation to the tweets shows more volatility in 2018 and 2019. Looking closely at the patterns of Trump's tweets, we see that Trump tweeted about market more in 2018 and 2019. Future analysis would involve investigating causality to see whether Trump's tweets are his reactions to the markets or whether his tweets have any impacts to the market.

##### Does Trump Tweet in Respond to the Economic Indicators Instead?

------

###### Trump's Tweet as Word Counts on GDP Components versus the Bureau of Economic Analysis (BEA) New Releases on RGDP growth

Trump has tweeted more over times when the BEA new releases estimate increases in RGDP growth rates. His tweet counts have been flat when the estimates show slow or negative RGDP growth rates.

###### Trump's Tweet as Word Counts on Employment Situations versus the Bureau of Labor Statistics (BLS) New Releases on Non-Farm Employment

In the same conclusions, Trump's tweet counts increase when the numbers of monthly job added are high and flat when they are low.

##### Do Economic Indicators Matter to the Market?

------

Slightly! The market may decline even when there are increases in RGDP growth or number of monthly job added. They move in the same directions likely when the changes in the economic indicators are either positive or negative for a few months or quarters in the roll. The market responses also seem brief. This may confirm that the stock market performance often based on earning estimates and/or word counts during conference calls on quarterly earnings. It will be an interesting project also to find the expected number of job added and expected growth rate that the market would react if the actual numbers of monthly job added or estimated growth rates go above or below.

 

 