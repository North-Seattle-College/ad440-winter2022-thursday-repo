import json
import boto3
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import string
from nltk.tokenize import word_tokenize
from nltk.tokenize import punkt
from nltk.corpus import stopwords
import re

# download needed packages
nltk.download('punkt')


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


def emoAnalyze(sentence):

    # cleanup the text and make it as words in a list
    sentence = sentence.lower()

    cleanedText = sentence.translate(str.maketrans('', '', string.punctuation))
    tokenizedList = word_tokenize(cleanedText, "english")

    # creating a list of words in the feedback excluding all the stop words
    finalList = [
        item for item in tokenizedList if item not in stopwords.words('english')]


# creating a list of emotion words and the words that have emotion according to our pre defined list

    emotionList = []

# open emotions.txt, clean the text lines, and comparegenerated finalList words with emotion words
    with open('.\emotions.txt', 'r') as file:
        for line in file:
            clearLine = line.replace('\n', '').replace(
                ',', '').replace("'", '').replace(' ', '').strip()
            word, emotion = clearLine.split(':')

            if word in finalList:
                emotionList.append(emotion)

    # returns a determined emotion from the emotionList or returns a default message
    return emotionList[0] if len(emotionList) != 0 else 'hard to read'


def sentAnalyze(sentence):

    # lists of words that indicates question
    wh_question = ['what', 'when', 'where', 'who',
                   'whom', 'which', 'whose', 'why', 'how', "am", "is", "are", "do", "does", "did", "have", "has", "was", "were", "can", "cannot", "could",
                   "couldn't", "dare", "may", "might", "must", "need", "ought", "shall", "should", "shouldn't", "will", "would"]

    # initialize
    sentence = sentence.lower()
    first_words = []
    type = []
    type_sentence = []

    # adding first word of the sentence in one list and adding the last element in the sentence in another list

    first_words.append(sentence.split(' ')[0])
    type.append(sentence[-1][-1])

    # validating of words
    for item in type:
        if item == '.':
            type_sentence.append('sentence')
        elif item == '!':
            type_sentence.append('sentence')
        elif item == '?':
            type_sentence.append('question')
        elif re.match('^[a-zA-Z0-9_]+$', item):
            type_sentence.append('statement')
        else:
            type_sentence.append('Unknown')

    # If a question mark was not included, Look for wh_question words
    for item in first_words:
        if item in wh_question:
            type_sentence[0] = 'question'

    # Return determined sentence type.
    return type_sentence[0]


def createSample():
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


def main():
    # Initiate s3 connection to desired bucket and desired object filename.
    s3 = boto3.resource('s3')

    obj = s3.Object('ad440-mpg-floop-export-storage',
                    'auto-floop-s3-export3.json')

    # Loads body of json from the s3 object
    global data
    data = json.load(obj.get()['Body'])

    # Create temp list of 50 items from the s3 file for modifying data elements
    global fbList
    fbList = []

    # calls createSample method that pulls 50 items from the loaded s3 data
    #   and adds the desired metadata to each conversation message
    createSample()

    # Define new object to be put in s3
    enrichObj = s3.Object('ad440-mpg-floop-export-storage',
                          'enriched-conv-sample.json')

    # Put json of fbList into object and put into s3 bucket.
    enrichObj.put(
        Body=(bytes(json.dumps(fbList).encode('UTF-8'))), ContentType='application/json'
    )


if __name__ == '__main__':
    main()
