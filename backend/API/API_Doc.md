# Summary
Documentation for the back-end API. 

# Student
## /Student/{studentID}
### POST
Create a student record, and optionally add feedback. Can create empty student record or add data when student record created.
- 200 OK
- 400 Bad Request
- 401 Unauthorized 
- 403 Forbidden
- 500 Internal Server Error
### GET 
Get all student feedback data. Returns JOSN object.
- 200 OK.
    - Returns JSON object.
- 401 Unauthorized 
- 403 Forbidden
- 500 Internal Server Error
### PATCH
- 200 OK.
- 401 Unauthorized 
- 403 Forbidden
- 500 Internal Server Error
### DELETE
- 200 OK.
- 401 Unauthorized 
- 403 Forbidden

# Comment
## /Student/{studentID}/comment/
### POST
- 200 OK. 
    - Returns string with AI feedback.
- 400 Bad Request
- 401 Unauthorized 
- 403 Forbidden
- 500 Internal Server Error
### GET 
- 401 Unauthorized 
- 403 Forbidden
- 500 Internal Server Error
### PATCH
- 401 Unauthorized 
- 403 Forbidden
- 500 Internal Server Error
### DELETE
- 401 Unauthorized 
- 403 Forbidden
- 500 Internal Server Error