from behave import *
import requests
import json
from behave.formatter import null
from data import apiResponse

URL = "https://gorest.co.in/public/v2/users"
response = apiResponse(null,null)
@when('I request user data')
def step_impl(context):
    response.responseCode = requests.get(URL).status_code
    response.json = json.dumps(requests.get(URL).json())
    pass

@then("Response is {number}")
def step_impl(context, number):
    assert str(response.responseCode) == number
    pass

@step("The user list has at least {number} user")
def step_impl(context,number):
    data = json.loads(response.json)
    assert len(data) >= int(number)
    pass


@step("The user list has at least {number} user whose name starts with {letter}")
def step_impl(context,number,letter):
    data = json.loads(response.json)
    letterUsers = [x for x in data if x['name'][0] == letter]
    assert len(letterUsers) >= int(number)


@step("The user list has at least {number} user and i display it")
def step_impl(context,number):
    data = json.loads(response.json)
    print((data))
    assert len(data) >= int(number)