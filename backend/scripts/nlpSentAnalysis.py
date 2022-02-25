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
        else:
            type_sentence.append('Unknown or Numbers')

    # If a question mark was not included, Look for wh_question words
    for item in first_words:
        if item in wh_question:
            type_sentence[0] = 'question'

    # Return determined sentence type.
    return type_sentence[0]
