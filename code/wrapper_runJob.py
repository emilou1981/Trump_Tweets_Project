from tweet_count import Tweet_count
from runJob import runJob
from datetime import datetime

start_dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(f'Starting wrapper_runJob at: {start_dt}')

# Run the MR Job wrapper code with options.
runJob(Tweet_count, ['/DA_WU/myFinalProject/data/tweet_only.csv', '--output-dir=/DA_WU/myFinalProject/outputdir', '--cleanup=ALL'])

end_dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(f'END wrapper_runJob at: {end_dt}')
print('') # print empty line
