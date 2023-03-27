import requests
import json
from domain import jsonMapper

from service.MyEncoder import MyEncoder


class TransferService:
    def generateToken():

        url = 'https://api.sandbox.transferwise.tech/oauth/token'
        data = { 'grant_type': 'refresh_token',   
          'refresh_token': 'efd76f1c-f819-4138-b5f1-2fe69512cec7'}

# Set headers including authorization token and content type
        headers = {'Authorization': 'Basic dHctdGVzdC1iYW5rOnR3LXRlc3QtYmFuaw==',
           'Content-Type': 'application/x-www-form-urlencoded'}

# Make the POST request
        response = requests.post(url, headers=headers, data=data)
        print(response.json()['access_token'])
        return (response.json()['access_token'])

# Check the response status code and content


    def createQuote(createQuoteRequest, token):
        print(vars(createQuoteRequest))
        json_string = json.dumps(createQuoteRequest, cls=MyEncoder)
        print(json_string)
        url = "https://api.sandbox.transferwise.tech/v2/quotes"
        headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer '+token}
        
        response = requests.post(url, data=json_string, headers=headers)
        print(response)
        return response

    
    def createRecipient(createRecipientRequest, token):
        data = jsonMapper.to_api_data(createRecipientRequest)
         
        json_string = json.dumps(data)
        json_string = json.dumps(data, default=lambda o: vars(o))
        print(json_string)
        url = "https://api.sandbox.transferwise.tech/v1/accounts"
        headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer '+token}

        response = requests.post(url, data=json_string, headers=headers)
        print(response)
        return response
    
    
    

      

 

