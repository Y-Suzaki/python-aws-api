import os
import sys
import json
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from domain.domain_response import DomainResponse
from datasource.model.employee import Employee


class EmployeesResponse(DomainResponse):
    def to_json_from_model(self, source):
        return [{'id': x.id, 'name': x.name, 'age': x.age} for x in source]


def get(event, context):
    try:
        return EmployeesResponse(Employee.get_employee_all()).build_success()
    except:
        return EmployeesResponse().build_server_error()
