import boto3
import json
from aws_lambda_powertools.utilities.typing import LambdaContext
from integration.lambda_proxy import app
from exceptions import WebBadRequestError
# app = ApiGatewayResolver()  # デフォルトではAPI Gateway REST API (v1)が使われます。


# Reference
# https://awslabs.github.io/aws-lambda-powertools-python/latest/core/event_handler/api_gateway/


@app.get('/skills')
def get_skills():
    """ パスパラメータがないGET """
    query_strings = app.current_event.query_string_parameters
    headers = app.current_event.headers
    print('** /skills **')
    print(f'{query_strings=}, {headers=}')

    if True:
        raise WebBadRequestError('/skills GET Error.')

    return {
        'total': 100,
        'skills': [
            {
                'id': 1,
                'name': 'Java'
            }
        ]
    }


@app.get('/skills/<skill_id>')
def get_skill(skill_id: str):
    """ パスパラメータがあるGET """
    _id = int(skill_id)
    print('** /skills **')
    print(f'{skill_id=}')
    return {
        'id': 10,
        'name': 'Python'
    }


@app.post('/skills')
def add_skill():
    """ post """
    skill: dict = app.current_event.json_body
    print(f'{skill=}')

    return {
        'id': 999,
        'name': 'Ruby'
    }


def handler(event: dict, context: LambdaContext):
    print(event)
    return app.resolve(event, context)


if __name__ == "__main__":
    _event = {'resource': '/skills', 'path': '/skills', 'httpMethod': 'GET', 'headers': {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'ja-JP,ja;q=0.9,en-US;q=0.8,en;q=0.7', 'CloudFront-Forwarded-Proto': 'https', 'CloudFront-Is-Desktop-Viewer': 'true', 'CloudFront-Is-Mobile-Viewer': 'false', 'CloudFront-Is-SmartTV-Viewer': 'false', 'CloudFront-Is-Tablet-Viewer': 'false', 'CloudFront-Viewer-ASN': '2518', 'CloudFront-Viewer-Country': 'JP', 'Host': 'qnmsyky8n1.execute-api.ap-northeast-1.amazonaws.com', 'Referer': 'https://ap-northeast-1.console.aws.amazon.com/', 'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'cross-site', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36', 'Via': '2.0 3358dad524ffe91108e2a678aaa49dca.cloudfront.net (CloudFront)', 'X-Amz-Cf-Id': 'nn915UfbqAJ6o1Tv6VGRtrpuNh4qtI1Wq425f-hBHiyYKwo_7SwyBA==', 'X-Amzn-Trace-Id': 'Root=1-62ee272d-4702e77873cf8d1c36c637b0', 'X-Forwarded-For': '133.200.47.128, 130.176.189.136', 'X-Forwarded-Port': '443', 'X-Forwarded-Proto': 'https'}, 'multiValueHeaders': {'Accept': ['text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'], 'Accept-Encoding': ['gzip, deflate, br'], 'Accept-Language': ['ja-JP,ja;q=0.9,en-US;q=0.8,en;q=0.7'], 'CloudFront-Forwarded-Proto': ['https'], 'CloudFront-Is-Desktop-Viewer': ['true'], 'CloudFront-Is-Mobile-Viewer': ['false'], 'CloudFront-Is-SmartTV-Viewer': ['false'], 'CloudFront-Is-Tablet-Viewer': ['false'], 'CloudFront-Viewer-ASN': ['2518'], 'CloudFront-Viewer-Country': ['JP'], 'Host': ['qnmsyky8n1.execute-api.ap-northeast-1.amazonaws.com'], 'Referer': ['https://ap-northeast-1.console.aws.amazon.com/'], 'sec-ch-ua': ['".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"'], 'sec-ch-ua-mobile': ['?0'], 'sec-ch-ua-platform': ['"Windows"'], 'sec-fetch-dest': ['document'], 'sec-fetch-mode': ['navigate'], 'sec-fetch-site': ['cross-site'], 'sec-fetch-user': ['?1'], 'upgrade-insecure-requests': ['1'], 'User-Agent': ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'], 'Via': ['2.0 3358dad524ffe91108e2a678aaa49dca.cloudfront.net (CloudFront)'], 'X-Amz-Cf-Id': ['nn915UfbqAJ6o1Tv6VGRtrpuNh4qtI1Wq425f-hBHiyYKwo_7SwyBA=='], 'X-Amzn-Trace-Id': ['Root=1-62ee272d-4702e77873cf8d1c36c637b0'], 'X-Forwarded-For': ['133.200.47.128, 130.176.189.136'], 'X-Forwarded-Port': ['443'], 'X-Forwarded-Proto': ['https']}, 'queryStringParameters': None, 'multiValueQueryStringParameters': None, 'pathParameters': None, 'stageVariables': None, 'requestContext': {'resourceId': 'jiyc30', 'resourcePath': '/skills', 'operationName': 'findSkills', 'httpMethod': 'GET', 'extendedRequestId': 'WbsPGFcXNjMFx_w=', 'requestTime': '06/Aug/2022:08:32:45 +0000', 'path': '/dev/skills', 'accountId': '838023436798', 'protocol': 'HTTP/1.1', 'stage': 'dev', 'domainPrefix': 'qnmsyky8n1', 'requestTimeEpoch': 1659774765240, 'requestId': '90e72acb-ba40-427d-aad1-bcc336b2c4d9', 'identity': {'cognitoIdentityPoolId': None, 'accountId': None, 'cognitoIdentityId': None, 'caller': None, 'sourceIp': '133.200.47.128', 'principalOrgId': None, 'accessKey': None, 'cognitoAuthenticationType': None, 'cognitoAuthenticationProvider': None, 'userArn': None, 'userAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36', 'user': None}, 'domainName': 'qnmsyky8n1.execute-api.ap-northeast-1.amazonaws.com', 'apiId': 'qnmsyky8n1'}, 'body': None, 'isBase64Encoded': False}
    response = handler(_event, None)
    print(response)
