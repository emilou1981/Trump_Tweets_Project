from tweet_count import Tweet_count
from runJob import runJob


# word_df = pd.read_csv('words.csv')
# word_list = word_df['word']

# Tweet_count(word_list)
# runJob(InitProcessing, ['/temp/inputData.txt', '--output-dir=/temp/InitProcessingResults'], 'emr')
runJob(Tweet_count, ['/DA_WU/Trump_Tweets_Project/data/tweet_only.csv', '--output-dir=/DA_WU/Trump_Tweets_Project/outputdir'])