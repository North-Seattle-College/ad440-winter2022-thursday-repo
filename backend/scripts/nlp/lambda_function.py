""" This is a copy of the Lambda function that was uploaded to AWS, it is not intended to run locally
and it will not work without modification"""

import json
import nltk
import requests
nltk.data.path.append("/tmp")

nltk.download('punkt', download_dir="/tmp")





def lambda_handler(event, context):
    answer = {}
    invalidReq = False
    try:
        sentence = event["sentence"]
    except:
        answer = {
            "error": "not a valid input"
        }
        invalidReq = True
    if not invalidReq:
        
        tokens = nltk.word_tokenize(sentence.lower())
        tokenlist = ''
        firstword = tokens[0]
        
        isQuestion = False

        
        
        for s in tokens:
            tokenlist += s


            
        if '?' in tokenlist:
            isQuestion = True
        
        wh_question = ['what', 'when', 'where', 'who',
                        'whom', 'which', 'whose', 'why', 'how']
        yN_question = ["am", "is", "are", "do", "does", "did", "have", "has", "was", "were", "can", "cannot", "could",
                        "couldn't", "dare", "may", "might", "must", "need", "ought", "shall", "should", "shouldn't", "will", "would"]
        
        if firstword in wh_question or firstword in yN_question:
            isQuestion = True
        
        answer = False
        if (isQuestion):
            answer = True

        
    return {
        'answer': answer
    }