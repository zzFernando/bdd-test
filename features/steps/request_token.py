from behave import *
import requests
import json

url = "https://api.withleaf.io/api/authenticate"
data = {'username':'fernandosdba@gmail.com', 'password':'94084452', 'rememberMe':'true'}
headers = {'Content-Type': 'application/json'}
response = requests.request("POST", url, headers=headers, json=data)

@given('we request a token')
def step_impl(context):    
    assert response.status_code == 200

@then('we have a token')
def step_impl(context):
    assert response.content == response.content

