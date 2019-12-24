
source activate pandas

echo "starting at:"
date +"%m-%d-%y %H:%M:%S"
python ETL.py && python CountVectorize.py && python wrapper_runJob.py && python load_word_count_to_db.py
echo "Ending at:"
date +"%m-%d-%y %H:%M:%S"