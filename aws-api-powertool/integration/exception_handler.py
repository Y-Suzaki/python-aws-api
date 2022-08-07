from aws_lambda_powertools.event_handler.api_gateway import Response, content_types

from lambda_proxy import app
from exceptions import WebBadRequestError


@app.exception_handler(WebBadRequestError)
def handle_invalid_limit_qs(e: WebBadRequestError):  # receives exception raised
    return Response(
        status_code=400,
        content_type=content_types.APPLICATION_JSON,
        body=f"Invalid request parameters. {str(e)}",
    )
