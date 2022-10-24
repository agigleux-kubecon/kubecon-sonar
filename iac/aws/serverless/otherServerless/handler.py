import os

def entrypoint(event, context):
    taintedInput = event['body']
    os.popen(taintedInput) # Noncompliant (S2076)
    return {"statusCode": 200}
