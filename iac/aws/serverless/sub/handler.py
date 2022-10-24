import os
import json
import boto3

def test4(event, context):
    taintedInput = event['body']
    os.popen(taintedInput)  # Noncompliant (S2076)
    return {"statusCode": 200}


def test5(event, context):
    taintedInput = event['body']
    os.popen(taintedInput)  # Noncompliant (S2076)
    return {"statusCode": 200}


def test6(event, context):
    taintedInput = event['body']
    os.popen(taintedInput)  # Ok - not defined as serverless entrypoint
    return {"statusCode": 200}


def test42(event, context):
    if event["queryStringParameters"]["dbid"] is None:
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "invalid request, missing id param"
            })
        }

    sqlData = ""
    if event["queryStringParameters"]["dbid"] == "redshift_compliant":
        sqlData = executeStatementCompliant(
            event["queryStringParameters"]["username"])

    elif event["queryStringParameters"]["dbid"] == "redshift_noncompliant":
        username = event["queryStringParameters"]["username"]

        redshiftClient = boto3.client('redshift-data')
        sql_str = 'select * from my_table where MY_COLUMN = \'' + username + '\''
        
        response = redshiftClient.execute_statement(
            ClusterIdentifier="myredshiftclusterid",
            Database='dev',
            DbUser='redshift_data_api_user',
            Sql=sql_str,
            WithEvent=True
        )

        time.sleep(5)

        response = redshiftClient.get_statement_result(
            Id=response["Id"]
        )

        sqlData = response

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": sqlData
        })
    }

def executeStatementCompliant(username):
    redshiftClient = boto3.client('redshift-data')
    sql_str="select * from users where name = :username",
    response = redshiftClient.execute_statement(
        ClusterIdentifier="myredshiftclusterid",
        Database='dev',
        DbUser='redshift_data_api_user',
        
        Sql=sql_str,
        Parameters=[
            {
                'name': 'username',
                'value': username
            }
        ],
        WithEvent=True
    ) # Compliant (S3649)

    time.sleep(5)

    response = redshift.database.REDSHIFT_CLIENT.get_statement_result(
        Id=response["Id"]
    )

    return response
