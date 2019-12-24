from tweet_count import Tweet_count
from runJob import runJob
from datetime import datetime

# word_df = pd.read_csv('words.csv')
# word_list = word_df['word']

# Tweet_count(word_list)
# runJob(InitProcessing, ['/temp/inputData.txt', '--output-dir=/temp/InitProcessingResults'], 'emr')
# now = datetime.now()
# current_time = now.strftime("%H:%M:%S")
# print(f'starting at: {current_time}')
runJob(Tweet_count, ['/DA_WU/Trump_Tweets_Project/data/tweet_only.csv', '--output-dir=/DA_WU/Trump_Tweets_Project/outputdir'])

# now = datetime.now()
# current_time = now.strftime("%H:%M:%S")
# print(f'End job at: {current_time}')