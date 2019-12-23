from mrjob.job import MRJob
import pandas as pd


class Tweet_count(MRJob):

    def mapper(self, _, line):
        #- Read in the words file and fill up
        # the array for the 'in' statement
        df = pd.read_csv('/DA_WU/Trump_Tweets_Project/data/words.csv')
        word_list = df['words'].tolist()  
        
        for word in line.split():
            if word.lower() in word_list:
                yield word, 1

    def reducer(self, key, values):
        yield key, sum(values)


if __name__ == "__main__":
    Tweet_count.run()

