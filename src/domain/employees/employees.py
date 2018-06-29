import os
import sys
import json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from datasource.model.employee import Employee


def to_json(entities):
    domians = []
    for entity in entities:
        domain = {'id': entity.id, 'name': entity.name, 'age': entity.age}
        domians.append(domain)
    return domians


def get(event, context):
    response = {
        'statusCode': 200,
        'body': json.dumps(to_json(Employee.get_employee_all()))
    }
    return response

