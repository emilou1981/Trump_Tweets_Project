from mrjob.job import MRJob
import pandas as pd


class Bacon_count(MRJob):

    def mapper(self, _, line):
        #- Read in the words file and fill up
        # the array for the 'in' statement
        
        for word in line.split():
            
            if word.lower() in ("mar", "largo", "president"):
                yield word, 1

    def reducer(self, key, values):
        yield key, sum(values)


if __name__ == "__main__":
    Bacon_count.run()

# word_df = pd.read_csv('words.csv')
# word_list = word_df['word']

# print(f'WordList: {word_list}')
# l = Bacon_count(word_list)
# print(l)