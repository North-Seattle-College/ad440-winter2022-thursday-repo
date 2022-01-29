import sys
from os import path
from os.path import exists
import string
from collections import Counter
from tokenize import maybe
import nltk
import matplotlib.pyplot as plt
from textblob import TextBlob
from pathlib import Path
from textblob.sentiments import NaiveBayesAnalyzer
import nltk.corpus
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk.corpus
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import word_tokenize
from nltk.data import load
fdist = FreqDist()
from nltk.tokenize import sent_tokenize

######## *****************************************************************************************************
#    If this is your first time to run this app, uncomment these lines, run the app and comment them up again.
######## *****************************************************************************************************

#    downloading required packages
nltk.download('nps_chat')
nltk.download('punkt')
nltk.download('brown')
nltk.download('stopwords')
nltk.download('vader_lexicon')
nltk.download('tagsets')



print('\n'+'******************************************************************')
print('This application is about Natural Language Processing (NLP).')
print('The user enters sentence(s) and by using Natural Language Tool Kit (nltk) and other algorithm the application')
print('will analyze that entry and gives some feesback.')
print('\n'+'*****   THIS APPLICATION DOES NOT SUPPORT CONTRACTED FORM    *****'+'\n')
print("If this is your first time to run this application, please uncomment all the nltk.downloads and then run the app!")
print('For the test of this app we have two list of comments in this file!')


def main():

    myFile = input('Enter your feedback: ') .lower()

# to see if the feedback cointains any ? mark

    print('\n'+'******************************************************************')
    print('                     RESULT for this entry                         ')
    print('******************************************************************')

    sentList = nltk.sent_tokenize(myFile)
    sentences_qnt = len(sentList)
    print('\n'+'You entered ', str(sentences_qnt), ' sentences.')

    if '?' in myFile:
        qnt = myFile.count('?')
        print('This entry includes: ' + str(qnt)+' question marks but ...')
        print('\n'+'******************************************************************')
    else:
        print('\n'+'******************************************************************')
        print('There is no question mark in this feedback but wait for more result!')
        print('\n'+'******************************************************************')
        print('Here are more analyses about this entry:'+'\n')

# lists of words that indicates question

    wh_question = ['what', 'when', 'where', 'who',
                   'whom', 'which', 'whose', 'why', 'how']
    yN_question = ["am", "is", "are", "do", "does", "did", "have", "has", "was", "were", "can", "cannot", "could",
                   "couldn't", "dare", "may", "might", "must", "need", "ought", "shall", "should", "shouldn't", "will", "would"]

# initialize

    first_words = []
    type_of_ending = []
    list_of_question_words = []
    type_sentence = []

# adding first words of all the sentences in one list and adding the last item in one sentence in another list

    for items in sentList:
        first_words.append(items.split(' ')[0])
        type_of_ending.append(items[-1][-1])

# validatin of words

    for item in type_of_ending:
        if item == '.':
            type_sentence.append('Sentence')
        elif item == '!':
            type_sentence.append('Exclamatory')
        elif item == '?':
            type_sentence.append('Interrogative')
        else:
            type_sentence.append('Unknown ')
    for items in first_words:
        if items in wh_question:
            list_of_question_words.append('WH question')
        elif items in yN_question:
            list_of_question_words.append('Y/N question')
# Here it shows all the sentences with their type

    for i in range(len(type_of_ending)):
        print('Sentence #', str(i+1), 'Type:', type_sentence[i])
        if type_sentence[i] == 'Unknown or Numbers':
            print("This is the type that we did not catch it: ", type_of_ending[i])
    for i in range(len(list_of_question_words)):
        print('Question #', str(i+1), 'Type:', list_of_question_words[i])

    countQuestionWords = Counter(list_of_question_words)
    print('Summary of question words: ', countQuestionWords)

# cleanup the text and make it as words in a list

    cleanedText = myFile.translate(str.maketrans('', '', string.punctuation))
    tokenizedList = word_tokenize(cleanedText, "english")

# creating a list of stop words in the feedback

    listOfWords = [
        item for item in tokenizedList if item in stopwords.words('english')]
    countstopwords = Counter(listOfWords)

# creating a list of words in the feedback excluded all the stop words

    finalList = [
        item for item in tokenizedList if item not in stopwords.words('english')]

    count = 0
    totalCount = 0
    itemsCount = 0
    for item in tokenizedList:
        itemsCount += 1
        if item in stopwords.words('english'):
            count += 1

# creating a list of emotion words and the words that have emotion according to our pre defined list

    emotionList = []
    wordList = []

# list of words with their emothions

    with open('emotions.txt', 'r') as file:
        for line in file:
            clearLine = line.replace('\n', '').replace(
                ',', '').replace("'", '').replace(' ', '').strip()
            word, emotion = clearLine.split(':')

            if word in finalList:
                emotionList.append(emotion)
                wordList.append(word)
            countEmotions = Counter(emotionList)
            countwords = Counter(finalList)
    totalCount = count+len(set(tokenizedList) -
                           set(wordList)-set(stopwords.words('english')))

# creating a blob text

    blob = TextBlob(myFile)
    wordCount = blob.word_counts

# make all the typos correct

    # correctmyFile = blob.correct()
    # sentences = blob.sentences
    # sen = blob.sentiment

    blob = TextBlob(myFile, analyzer=NaiveBayesAnalyzer())
    sen_sub = blob.sentiment

    def sentimentAnalyse(text):
        score = SentimentIntensityAnalyzer().polarity_scores(text)
        for k,v in score.items():
            print(f"{k}:{v:.2f}")
        neg = score['neg']
        pos = score['pos']
        if neg > pos:
            print("\n"+"In general: Negative sentiment!")
        elif pos > neg:
            print("\n"+"In general: Positive sentiment!")
        else:
            print("\n"+"In general: Neutral vibe!")

    sentimentAnalyse(myFile)
    reg = RegexpTokenizer('(?u)\w+|\$[\d\.]+|\s+')

    print('\n'+'******************************************************************')
    print('Summary of sentiments:')
    print('\n'+'list of words with emotions: ', wordList)
    print('\n'+'Summary of emotions count: ', countEmotions)
    print('\n'+'******************************************************************')
    print('                  Close the bar chart windows                     ')
    print('                      End of Application                          ')
    print('******************************************************************')

# Drawing the bar chart

    fig, axl = plt.subplots()
    axl.bar(countEmotions.keys(), countEmotions.values())
    fig.autofmt_xdate()
    plt.savefig('graph.png')
    plt.show()

# here we can get all the tags for each words

    # print(nltk.pos_tag(tokenizedList))



main()

###### Cheat sheet for tagging #########################################################
# CC coordinating conjunction
# CD cardinal digit
# DT determiner
# EX existential there (like: “there is” … think of it like “there exists”)
# FW foreign word
# IN preposition/subordinating conjunction
# JJ adjective ‘big’
# JJR adjective, comparative ‘bigger’
# JJS adjective, superlative ‘biggest’
# LS list marker 1)
# MD modal could, will
# NN noun, singular ‘desk’
# NNS noun plural ‘desks’
# NNP proper noun, singular ‘Harrison’
# NNPS proper noun, plural ‘Americans’
# PDT predeterminer ‘all the kids’
# POS possessive ending parent‘s
# PRP personal pronoun I, he, she
# PRP$ possessive pronoun my, his, hers
# RB adverb very, silently,
# RBR adverb, comparative better
# RBS adverb, superlative best
# RP particle give up
# TO to go ‘to‘ the store.
# UH interjection errrrrrrrm
# VB verb, base form take
# VBD verb, past tense took
# VBG verb, gerund/present participle taking
# VBN verb, past participle taken
# VBP verb, sing. present, non-3d take
# VBZ verb, 3rd person sing. present takes
# WDT wh-determiner which
# WP wh-pronoun who, what
# WP$ possessive wh-pronoun whose
# WRB wh-abverb where, when