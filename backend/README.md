# Backend README

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