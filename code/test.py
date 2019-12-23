from word_counter_v2 import Tweet_count
from runJob import runJob


# word_df = pd.read_csv('words.csv')
# word_list = word_df['word']

# Tweet_count(word_list)
# runJob(InitProcessing, ['/temp/inputData.txt', '--output-dir=/temp/InitProcessingResults'], 'emr')
runJob(Tweet_count, ['/DA_WU/myFinalProject/tweet_only.csv', '--output-dir=/DA_WU/myFinalProject/outputdir'])