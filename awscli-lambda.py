"""
(main) Ryans-Air:aws-lambda ryan$ py awscli-lambda.py
b'"WUT"'
"""

import json

import boto3

payload = {"key1": "WUT", "key2": "value2", "key3": "value3"}

client = boto3.client("lambda")
response = client.invoke(FunctionName="lambda-hello", Payload=json.dumps(payload))

print(response["Payload"].read())
