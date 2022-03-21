"""
This is snapshot of what is currently on AWS Lambda function, named 'sw-test'
Last updated on 3/16/2022 @ 16:38 PST

This live version on AWS can be updated anytime, and this snapshot WILL NOT always be in-sync with the live version.
"""

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.data.path.append("/tmp")

nltk.download('stopwords', download_dir="/tmp")
nltk.download('punkt', download_dir="/tmp")
nltk.download('averaged_perceptron_tagger', download_dir="/tmp")


class Tokenizer:

    def __init__(self, text):
        self.text = text
        self.stopwords = set(stopwords.words('english'))
        self.punctuation = nltk.RegexpTokenizer(r"\w+")

    def setText(self, newText):
        self.text = newText

    def addToText(self, newText):
        self.text += newText

    def clearText(self):
        self.text = ""

    def splitSentences(self):
        return nltk.sent_tokenize(self.text)

    def splitWords(self):
        return self.punctuation.tokenize(self.text)

    def removeStopwords(self):
        dirty = self.splitWords()
        return [w for w in dirty if not w.lower() in self.stopwords]
