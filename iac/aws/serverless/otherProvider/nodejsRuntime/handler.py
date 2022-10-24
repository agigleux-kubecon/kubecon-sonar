import os

def testNodeJs(event, context):
    taintedInput = event['body']
    os.popen(taintedInput) # Ok - serverless yaml config file does not refer to this handler (its using nodejs runtime)
    return {"statusCode": 200}
