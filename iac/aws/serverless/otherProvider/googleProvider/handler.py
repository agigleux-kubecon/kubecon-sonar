import os

def testGoogle(event, context):
    taintedInput = event['body']
    os.popen(taintedInput) # Ok - serverless yaml config file does not refer to this handler (provider is not AWS)
    return {"statusCode": 200}
