""" This is a copy of the Lambda function that was uploaded to AWS, it is not intended to run locally
and it will not work without modification"""

import json
from math import isqrt
import nltk
import requests
nltk.download('punkt')





def lambda_handler(event=None, context=None):
    sentence = None
    # sentence = event["sentence"]
    sentence.lower()
    tokens = nltk.word_tokenize(sentence)
    tokenlist = ''
    firstword = tokens[0]
    print(firstword)
    
    isQuestion = False

    
    
    for s in tokens:
        tokenlist += s

    print(tokenlist)
        
    if '?' in tokenlist:
        isQuestion = True
    
    wh_question = ['what', 'when', 'where', 'who',
                    'whom', 'which', 'whose', 'why', 'how']
    yN_question = ["am", "is", "are", "do", "does", "did", "have", "has", "was", "were", "can", "cannot", "could",
                    "couldn't", "dare", "may", "might", "must", "need", "ought", "shall", "should", "shouldn't", "will", "would"]
    
    if firstword in wh_question or firstword in yN_question:
        isQuestion = True
    print(isQuestion)
    
    answer = ''
    if (isQuestion):
        answer = 'This is a question'
    else:
        answer = "This is not a question"

    return answer
    # return {
    #     'statusCode': 200,
    #     'answer': answer
    #     # 'body': json.dumps(answer)
    # }
print(lambda_handler())