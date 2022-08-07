from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools.event_handler.api_gateway import ApiGatewayResolver, Response, content_types
from aws_lambda_powertools.utilities.typing import LambdaContext

app = ApiGatewayResolver()  # デフォルトではAPI Gateway REST API (v1)が使われます。
