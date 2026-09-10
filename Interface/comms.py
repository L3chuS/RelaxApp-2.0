import requests
from settings import API_URL

def make_request(method, url, **kwargs):
    
    try:
        response =  requests.request(
            method,
            url,
            timeout=10,
            **kwargs
        )
        
        return {
            "connection_status" : True,
            "response" : response,
            "message" : None
        }
    
    except requests.exceptions.ConnectionError:
        return {
            "connection_status" : False,
            "response" : None,
            "error" : "The connection to the server has failed.",
            "error_type" : "ERROR_SERVER_CONNECTION"
        }
        
    except requests.exceptions.Timeout:
        return {
            "connection_status" : False,
            "response" : None,
            "error" : "The request timed out.",
            "error_type" : "ERROR_SERVER_TIMEOUT"
        }
    except requests.exceptions.RequestException as error:
        return {
            "connection_status" : False,
            "response" : None,
            "error" : str(error),
            "error_type" : "ERROR_SERVER_GENERAL"
        }

def login(data):
    
    response = make_request(
        "POST",
        f"{API_URL}login/",
        json=data
    )
    print(response)
    
    return response

def register(data):
    
    response = make_request(
        "POST",
        f"{API_URL}register/",
        json=data
    )
    print(response)
    
    return response