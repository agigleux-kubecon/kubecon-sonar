import logging
import os

logger = logging.getLogger("logger")

def test1(event, context):
    taintedInput = event['queryStringParameters']['foo']
    safeInput = event['apiId']
    os.popen(taintedInput) # Noncompliant (S2076)
    os.popen(safeInput)    # Compliant; not user-controlled
    return {"statusCode": 200}

def test2(event, context):
    taintedInput = event['body']
    os.popen(taintedInput) # Noncompliant (S2076)
    return {"statusCode": 200}

def test3(event, context):
    taintedInput = event['body']
    os.popen(taintedInput) # Noncompliant (S2076)
    return {"statusCode": 200}

def test4(event, context):
    taintedInput = event['body']
    os.popen(taintedInput) # Ok - this function is not defined as serverless entrypoint
    return {"statusCode": 200}

def test6(event, context):
    taintedInput = event['body']
    os.popen(taintedInput) # Ok - the handler function does not have a vulnerable event type
    return {"statusCode": 200}

def test7(event, context):
    taintedInput = event['body']
    os.popen(taintedInput) # Ok - the handler function has mock integration type
    return {"statusCode": 200}

def testSources(event, context):
    source = event
    bodySource = event['body']
    headersSource = event['headers']
    pathParametersSource = event['pathParameters']
    queryStringParametersSource = event['queryStringParameters']
    userAgentSource = event['requestContext']['identity']['userAgent']
    nonSource1 = event['requestContext']['identity']['other']
    nonSource2 = event['requestContext']['other']
    nonSource3 = event['other']

    os.popen(source) # Noncompliant (S2076)
    logger.info(source) # Noncompliant (S5145)
    os.popen(bodySource) # Noncompliant (S2076)
    logger.info(bodySource) # Noncompliant (S5145)
    os.popen(headersSource) # Noncompliant (S2076)
    logger.info(headersSource) # Ok - this is not a source for log injection rule
    os.popen(pathParametersSource) # Noncompliant (S2076)
    logger.info(pathParametersSource) # Noncompliant (S5145)
    os.popen(queryStringParametersSource) # Noncompliant (S2076)
    logger.info(queryStringParametersSource) # Noncompliant (S5145)
    os.popen(userAgentSource) # Noncompliant (S2076)
    logger.info(userAgentSource) # Ok - this is not a source for log injection rule
    os.popen(nonSource1) # Ok - not a source
    logger.info(nonSource1) # Ok - not a source
    os.popen(nonSource2) # Ok - not a source
    logger.info(nonSource2) # Ok - not a source
    os.popen(nonSource3) # Ok - not a source
    logger.info(nonSource3) # Ok - not a source
    return {"statusCode": 200}
