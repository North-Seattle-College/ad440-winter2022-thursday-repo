import json
import boto3

client = boto3.client('lambda')

def lambda_handler(event, context):
    # TODO implement
    
    data={
  "text": "Hello Fikirte. How are you? I wanted to get in touch with you to inform you that you have done a good job in your assessment. It was a pleasure working with you.",
  "path": "splitSentences"
}
    
    response = client.invoke(
        FunctionName = 'arn:aws:lambda:us-west-2:061431082068:function:sw-test:finalSplit',
        InvocationType = 'RequestResponse',
        Payload = json.dumps(data))
        

    payload = response['Payload']
    split_response = payload.read()
    sentences = json.loads(split_response.decode("UTF-8"))
    
    question_no = []
    #print(sentences.keys())
    for i in sentences['result']['sentences']:
        #print(i)
        question_no_data = {'sentence':i}
        response_q = client.invoke(
            FunctionName = 'arn:aws:lambda:us-west-2:061431082068:function:ab-isQuestion',
            InvocationType = 'RequestResponse',
            Payload = json.dumps(question_no_data))
        payload_q = response_q['Payload']
        q_no_resp = payload_q.read()
        if "false" in q_no_resp.decode('UTF-8'):
            question_no.append({"sentence":i,"isQuestion":False})
        else:
            question_no.append({"sentence":i,"isQuestion":True})
    
    
   # final_data = 
    
    return question_no
    #print(json.load(response['Payload']))
