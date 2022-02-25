import json
import boto3
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nlpEmoAnalysis import emoAnalyze
from nlpSentAnalysis import sentAnalyze


# nltk method to analyze pos/neg/neutral sentiment of a provided string
def sentence_classification(sentence: str):
    sid = SentimentIntensityAnalyzer()
    ss = sid.polarity_scores(sentence)

    if ss['pos'] > 0.3 and ss['neg'] < 0.1:
        return 'positive'
    elif ss['neg'] > 0.15:
        return 'negative'
    else:
        return 'neutral'


# Initiate s3 connection to desired bucket and desired object filename.
s3 = boto3.resource('s3')

obj = s3.Object('ad440-mpg-floop-export-storage', 'auto-floop-s3-export3.json')

# Loads body of json from the s3 object
data = json.load(obj.get()['Body'])


# Create temp list of 50 items from the s3 file for modifying data elements
fbList = []
for x in range(50):
    fbList.append(data[x])

# Placeholder variables for string formatting - to be replaced with question/statement,
#   positive/negative/neutral, and emotion matching below
question = ''
posNeg = ''
emotion = ''

# For each item in fbList, check # of dictionaries in item. For each dictionary, update
#   with new key:value of <'metadata':array of length 3> -- formatted for each placeholder
for x in fbList:
    for y in range(len(x)):
        # - retrieve the value for key 'Text' (the feedback/replies to analyze)
        sentence = x[y].get('Text')

        # run Text value through the three analyzers
        question = sentAnalyze(sentence)
        posNeg = sentence_classification(sentence)
        emotion = emoAnalyze(sentence)

        # This updates each comment dictionary in fbList with metadata K:V.
        x[y].update(
            metadata=['{}'.format(question), '{}'.format(
                posNeg), '{}'.format(emotion)]
        )

# Define new object to be put in s3
enrichObj = s3.Object('ad440-mpg-floop-export-storage',
                      'enriched-conv-sample.json')

# Put json of fbList into object and put into s3 bucket.
enrichObj.put(
    Body=(bytes(json.dumps(fbList).encode('UTF-8'))), ContentType='application/json'
)
