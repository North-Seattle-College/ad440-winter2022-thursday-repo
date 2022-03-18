# Backend README

-----

## Integrated API Documentation

Integrated API URL: <https://3s7yrqtdmb.execute-api.us-west-2.amazonaws.com/demo/splitSentences>

See [splitSentences API](#splitSentence) below on how to submit a request.

**Note:** the API is _slow_ (~10 sec via Postman), and memory intensive due to one of the dependencies we used. Try not to call on it too often or we will get a bigger bill than what we already have. 😬

example output:

```JSON
{
    "result": {
        "sentences": [
            {
                "sentence": "Generating random paragraphs can be an excellent way for writers to get their creative flow going at the beginning of the day.",
                "sentiment": "neutral",
                "sentimentScore": 0.765,
                "emotion": "Happy",
                "isQuestion": false
            },
            {
                "sentence": "The writer has no idea what topic the random paragraph will be about when it appears.",
                "sentiment": "neutral",
                "sentimentScore": -0.296,
                "emotion": "Sad",
                "isQuestion": false
            },
            {
                "sentence": "This forces the writer to use creativity to complete one of three common writing challenges.",
                "sentiment": "neutral",
                "sentimentScore": 0.4404,
                "emotion": "Fear",
                "isQuestion": false
            },
            {
                "sentence": "The writer can use the paragraph as the first one of a short story and build upon it.",
                "sentiment": "neutral",
                "sentimentScore": 0.0,
                "emotion": "Angry",
                "isQuestion": false
            },
        ]
    }
}
```

-----

## Split paragraph into sentences (Tokenizer) API Documentation

> Author: Steven Wang
> GitHub: @shipitsteven

Base API URL: <https://3s7yrqtdmb.execute-api.us-west-2.amazonaws.com/tokenize/>

## Endpoints

### **POST** `/splitSentences`

- Description: Split paragraph into sentences
- Request URL: `[BASE_URL]/splitSentences`
- Request body format: `JSON`
- Request body:

    ```JSON
    {"text": "This is a sentence. This is another sentence."}
    ```

- Success response format: `JSON`

    ```JSON
    {
        "result": {
            "sentences": [
                "This is a sentence.",
                "This is another sentence."
            ]
        }
    }
    ```

- Bad response format: `JSON`

    Invalid text (eg. `"text": 123`):  
    Status: **200**

    ```JSON
    {
        "result": {
            "error": "text provided is not a string or invalid type"
        }
    }
    ```

    Invalid request body (eg. `{foo}`):
    Status: **400**

    ```JSON
    {
        "message": "Could not process payload"
    }
    ```

    Wrong request body type (eg. text instead of JSON):
    Status: **415**

    ```JSON
    {
        "message": "Unsupported Media Type"
    }
    ```

### **POST** `/splitWords`

- Description: Split text into words, also removed punctuation marks. Duplicate words will appear multiple times.
- Request URL: `[BASE_URL]/splitWords`
- Request body format: `JSON`
- Request body:

    ```JSON
    {"text": "This is a sentence. This is another sentence."}
    ```

- Success response format: `JSON`

    ```JSON
    {
        "result": {
            "words": [
                "This",
                "is",
                "a",
                "sentence",
                "This",
                "is",
                "another",
                "sentence"
            ]
        }
    }
    ```

- Bad response format: `JSON`
    > Responses are same as `/splitSentences`

### POST `/removeStopWords`

- Description: remove stop words from a text, stop words are words that are not important to the meaning of the text such as 'a', 'the', 'is', 'and', etc.
- Request URL: `[BASE_URL]/splitSentences`
- Request body format: `JSON`
- Request body:

    ```JSON
    {"text": "This is a sentence. This is another sentence."}
    ```

- Success response format: `JSON`

    ```JSON
    {
        "result": {
            "words": [
                "sentence",
                "another",
                "sentence"
            ]
        }
    }
    ```

  - Bad response format: `JSON`
    > Responses are same as `/splitSentences`

-----