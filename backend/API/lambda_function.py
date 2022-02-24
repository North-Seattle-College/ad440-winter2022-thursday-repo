from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
import json

def lambda_handler(event, context):
    # add temp directory to data path
    nltk.data.path.append('/tmp')
    
    # download data to temp directory
    nltk.download('vader_lexicon', download_dir='/tmp')
    
    # execute sentiment analyzer 
    sid = SentimentIntensityAnalyzer()
    ss = sid.polarity_scores(event['feedback'])
    out = {'neg': ss['neg'], 'neu': ss['neu'], 'pos': ss['pos']}

    return {
        'statusCode': 200,
        'body': out
    }