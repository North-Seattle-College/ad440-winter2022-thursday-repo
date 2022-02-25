import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


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
    #wordList = []

# open emotions.txt, clean the text lines, and comparegenerated finalList words with emotion words
    with open('.\emotions.txt', 'r') as file:
        for line in file:
            clearLine = line.replace('\n', '').replace(
                ',', '').replace("'", '').replace(' ', '').strip()
            word, emotion = clearLine.split(':')

            if word in finalList:
                emotionList.append(emotion)
                # wordList.append(word)

# returns a determined emotion from the emotionList or returns a default message
    return emotionList[0] if len(emotionList) != 0 else 'hard to read'
