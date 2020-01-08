from mrjob.job import MRJob
import pandas as pd
   

class Tweet_count(MRJob):
    
    def mapper_init(self):
        
        df = pd.read_csv('/DA_WU/Trump_Tweets_Project/data/words.csv')
        wl = df['word'].tolist()   
        self.word_dict = {}
        for word in wl:
            self.word_dict[word] = word


    def mapper(self, _, line):
        #- Read in the words file and fill up
        # the array for the 'in' statement
        
        for word in line.split():
            if word.lower() in self.word_dict:
                yield word, 1

    def reducer(self, key, values):
        yield key, sum(values)


if __name__ == "__main__":
    Tweet_count.run()

