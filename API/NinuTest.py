import requests
import json

base_url="https://gorest.co.in"
auth_token = "Bearer hsdcskcksckhsvk"

def get_request():
    url=base_url+"/public/v2/users?"
    headers={"Authorization":auth_token,
             "application":"json/type"}
    response= requests.get(url, params="ninu",headers=headers)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data,indent =4)
    print("Response body :: "+json_str)
    requests.get

get_request()

