from behave import *
import requests
import json


@given('I have user authentication credentials')
def step_impl(context):
    context.url = 'https://api.withleaf.io/api/authenticate'
    context.headers = {'content-type': 'application/json'}
    context.data = {
        "username": "fernandosdba@gmail.com",
        "password": "94084452",
        "rememberMe":"true",
    }

@when('I make an http post call')
def step_impl(context):
    context.response = requests.request("POST" , context.url, json=context.data, headers=context.headers)


@then('I must get a reponse with status code 200 and a jSon object with token')
def step_impl(context):
    print("\n" , context.response.content)
    assert context.response.status_code == 200
