from mrjob.job import MRJob
import pandas as pd


class Bacon_count(MRJob):
    
    def mapper(self, _, line,):
        #- Read in the words file and fill up
        # the array for the 'in' statement
        
        for word in line.split():
            
            if word.lower() in ("mar", "largo", "president"):
                yield word, 1

    def reducer(self, key, values):
        yield key, sum(values)


if __name__ == "__main__":
    Bacon_count.run()

