import json


class DomainResponse:
    def __init__(self, source=None):
        self.source = source

    def to_json_from_model(self):
        pass
    
    def build_success(self):
        if self.source is None:
            raise ValueError()

        response = {
            'statusCode': 200,
            'body': json.dumps(self.to_json_from_model(self.source))
        }
        return response

    def build_created(self):
        if self.source is None:
            raise ValueError()

        response = {
            'statusCode': 201,
            'body': json.dumps(self.to_json_from_model(self.source))
        }
        return response

    def build_auth_error(self):
        response = {
            'statusCode': 401,
            'body': json.dumps({'message': 'Authentication error.'})
        }
        return response

    def build_not_found(self):
        response = {
            'statusCode': 404,
            'body': json.dumps({'message': 'Resource not found.'})
        }
        return response

    def build_server_error(self):
        response = {
            'statusCode': 503,
            'body': json.dumps({'message': 'Internal server error.'})
        }
        return response
