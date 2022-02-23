class Tokenizer:

    def __init__(self, text):
        self.text = text
        import nltk
        self.nltk = nltk
        from nltk.corpus import stopwords
        nltk.download('stopwords')
        self.stopwords = set(stopwords.words('english'))
        nltk.download('punkt')
        nltk.download('averaged_perceptron_tagger')
        self.punctuation = nltk.RegexpTokenizer(r"\w+")

    def setText(self, newText):
        self.text = newText

    def addToText(self, newText):
        self.text += newText

    def clearText(self):
        self.text = ""

    def splitSentences(self):
        return self.nltk.sent_tokenize(self.text)

    def splitWords(self):
        return self.punctuation.tokenize(self.text)

    def removeStopwords(self):
        dirty = self.splitWords()
        return [w for w in dirty if not w.lower() in self.stopwords]


# Test strings below
text = "Generating random paragraphs can be an excellent way for writers to get their creative flow going at the beginning of the day. The writer has no idea what topic the random paragraph will be about when it appears. This forces the writer to use creativity to complete one of three common writing challenges. The writer can use the paragraph as the first one of a short story and build upon it. A second option is to use the random paragraph somewhere in a short story they create. The third option is to have the random paragraph be the ending paragraph in a short story. No matter which of these challenges is undertaken, the writer is forced to use creativity to incorporate the paragraph into their writing."

# test script
token = Tokenizer(text)

print('----------------------------------------')
print('Sentences:')
sent = token.splitSentences()
num = 1
for sentence in sent:
    print(str(num) + " : " + sentence)
    num += 1
print('----------------------------------------')


# You can check the array of words with the follow two print statements
# print(token.splitWords())
# print(token.removeStopwords())
