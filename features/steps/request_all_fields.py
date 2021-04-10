from behave import *
import requests
import json

@given('I have a valid token')
def step_impl(context):
    url = 'https://api.withleaf.io/api/authenticate'
    headers = {'content-type': 'application/json'}
    data = {"username": "fernandosdba@gmail.com", "password": "94084452", "rememberMe":"true"}
    token = requests.request("POST" , url, json=data, headers=headers)
    context.url = "https://api.withleaf.io/services/fields/api/fields"
    context.payload={}
    context.headers = {'Authorization': token.headers['Authorization']}

@when('I make an http GET call to https://api.withleaf.io/services/fields/api/fields')
def step_impl(context):
    context.response = requests.request("GET", context.url, headers=context.headers, data=context.payload)

@then('I must get a response with status code 200 and a json object with all fields')
def step_impl(context):
    print("\n" , context.response.content)
    assert context.response.status_code == 200
