import os
import sys
import json
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from domain.domain_response import DomainResponse
from datasource.model.employee import Employee


class EmployeeDomainResponse(DomainResponse):
    def to_json_from_model(self, source):
        model = source
        return {'id': model.id, 'name': model.name, 'age': model.age}


def get(event, context):
    pass


def create(event, context):
    pass


def update(event, context):
    pass


def delete(event, context):
    pass

