//TODO: Connect DynamoDB destination
const AWS = require("aws-sdk");
const dynamo = new AWS.DynamoDB.DocumentClient();

exports.handler = async (event, context) => {
    let body;
    let statusCode=200;
    console.log(event)
    const headers = {
        "Content-Type": "application/json"
    };
    
    try {
        switch (event.routeKey) {
            case "GET /test":
                body = ( [{
                'id': 1,
                'title': 'Hello from Lambda',
                'description': 'Jonathon Kindle Coming from Lambda in AWS'
            },
            {
                'id': 2,
               'title': 'Random Text',
                'description': 'Random description'
            }
            ])
            break;
            case "POST /test":
                let requestJSON = JSON.parse(event.body);
                body = (`POST request success `)
            break;
            case "OPTIONS /test":
                body = (`successfully hit options`)
                break;
        
        }
    } catch (err) {
        statusCode = 400;
        body = err.message;
    } finally {
        body = JSON.stringify(body)
    }
    
    return {
        statusCode,
        body,
        headers
};
};