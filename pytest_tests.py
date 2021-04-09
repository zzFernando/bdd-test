import requests
import json

def test_get_locations_for_us_90023_check_status_code_equals_200():

     print('start test')
     
     #var
     response = requests.get("http://api.zippopotam.us/us/90023")  

     #validation   
     assert response.status_code == 200
     
     #prints
     json_response_content = response.content
     json_parsed = json.loads(json_response_content)
     print('\n\n\n http status code:', response.status_code)
     print(json.dumps(json_parsed, indent=4, sort_keys=True),'\n\n')
     

def test_get_locations_for_us_90023_check_content_type_equals_json():

     print('start test')
     
     #var
     response = requests.get("http://api.zippopotam.us/us/90023")

     #validation 
     assert response.status_code == 200
     
     #prints
     json_response_content = response.content
     json_parsed = json.loads(json_response_content)
     print('\n\n\n http status code:', response.status_code)
     print(json.dumps(json_parsed, indent=4, sort_keys=True), '\n\n')