import pytest
import api_helpers
import json
from jsonschema import validate
import jsonpath
from assertpy import assert_that


@pytest.mark.parametrize("status", ["available", "pending", "sold"])
def test_find_by_status_200(status):
    print("\nRunning with status {}".format(status))
    test_endpoint = "/pets/findByStatus"
    params = {
        "status": status
    }
    response = api_helpers.get_api_data(test_endpoint, params)
    assert response.status_code == 200

    if status in ['available', 'pending']:
        print("\nStatus: {}".format(status))
        my_json = json.loads(response.text)
        validate(instance=my_json, schema=schemas.pet, cls=None)
        assert jsonpath.jsonpath(my_json, '$[0].status') == status
        assert_that(jsonpath.jsonpath(my_json, '$[0].status')).is_equal_to(status)
    elif status in ['sold']:
        print("\nStatus: {}".format(status))
        my_json = json.loads(response.text)
        my_json = json.loads(response.text)



@pytest.mark.parametrize("status", ["available", "pending", "sold"])
def test_find_by_status_200(status):
    print("\nRunning with status {}".format(status))
    test_endpoint = "/pets/findByStatus"
    params = {
        "status": status
    }
    response = api_helpers.get_api_data(test_endpoint, params)
    assert response.status_code == 200
    if(status == 'available' or status == 'pending'):
        print("\n1.status {}".format(status))
        my_json = json.loads(response.text)
        validate(instance=my_json, schema=schemas.pet, cls=None)
        print(jsonpath.jsonpath(my_json,'$[0].status'))
        assert jsonpath.jsonpath(my_json, '$[0].status') == status
        assert_that(jsonpath.jsonpath(my_json,'$[0].status')) == status