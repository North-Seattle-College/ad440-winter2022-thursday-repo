# Function purpose
demoThursdayLambda is responsibile for responding to the requests made from the front-end, by providing a response that takes into consideration primarily four things:
1. Splitting the feedback into individual sentences
2. Performing an analysis of whether the statement is a question or not,
3. Performing an analysis on the sentiment of the statemetn: Whether it is positive, negative or neutral
4. Detecting the emotion shown by the feedback: Happy/Sad/Angry/Afraid/etc.

# Input Format:
The lambda function is configured to respond to a POST request, that contains the feedback.
For eg:
```JSON
{
"text": "You have done really well on your assignment. I believe if you can keep up this performance, you will do really well on your course. Keep up the good work!"
}
```

# Output Format:
The lambda function will return a json file that looks similar to this:
```JSON
{
  "result": {
    "sentences": [
      {
        "sentence": "You have done really well on your assignment.",
        "sentiment": "neutral",
        "sentimentScore": 0.3384,
        "emotion": "Surprise",
        "isQuestion": false
      },
      {
        "sentence": "I believe if you can keep up this performance, you will do really well on your course.",
        "sentiment": "neutral",
        "sentimentScore": 0.3384,
        "emotion": "Surprise",
        "isQuestion": false
      },
      {
        "sentence": "Keep up the good work!",
        "sentiment": "positve",
        "sentimentScore": 0.4926,
        "emotion": "Happy",
        "isQuestion": false
      }
    ]
  }
}
```
