"""
This is snapshot of what is currently on AWS Lambda function, named 'sw-test'
Last updated on 3/16/2022 @ 16:38 PST

This live version on AWS can be updated anytime, and this snapshot WILL NOT always be in-sync with the live version.
"""
import json
import nltk
from tokenizer import Tokenizer


def lambda_handler(event, context):
    result = {}
    invalidRequest = False

    try:
        text = event["text"]
        op = event["path"]
    except KeyError:
        result = {
            "error": "missing input for request body and/or improper endpoints, proper request requires following format: {'text': '[string to be parsed]'}, proper end points are '[API_URL]/tokenize/[operation]'"
        }
        invalidRequest = True

    if not invalidRequest:
        token = Tokenizer(text)
        if op not in ["splitSentences", "splitWords", "removeStopwords"]:
            result = {
                "error": "missing or invalid end point, valid operations end points are '[API_URL]/tokenize/splitSentences', '[API_URL]/tokenize/splitWords', '[API_URL]/tokenize/removeStopwords'"}
        elif not isinstance(text, str):
            result = {"error": "text provided is not a string or invalid type"}
        elif op == "splitSentences":
            result = {"sentences": token.splitSentences()}
        elif op == "splitWords":
            result = {"words": token.splitWords()}
        elif op == "removeStopwords":
            result = {"words": token.removeStopwords()}

    response = {
        "result": result,
    }

    return response
