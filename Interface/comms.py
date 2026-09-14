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
        perro = 123
        return {
            "connection_status" : True,
            "response" : response,
            "message" : "* MESSAGE: The connection with the server has been established.",
            "message_link" : None
        }
    
    except requests.exceptions.ConnectionError:
        return {
            "connection_status" : False,
            "response" : None,
            "error" : "* ERROR: The connection to the server has failed.",
            "error_type" : "SERVER",
            "error_link" : "ERROR_SERVER_CONNECTION"
        }
        
    except requests.exceptions.Timeout:
        return {
            "connection_status" : False,
            "response" : None,
            "error" : "* ERROR: The request timed out.",
            "error_type" : "SERVER",
            "error_link" : "ERROR_SERVER_TIMEOUT"
        }
    except requests.exceptions.RequestException as error:
        return {
            "connection_status" : False,
            "response" : None,
            "error" : "* ERROR: " + str(error),
            "error_type" : "SERVER",
            "error_link" : "ERROR_SERVER_GENERAL"
        }

def login(data):
    
    response = make_request(
        "POST",
        f"{API_URL}login/",
        json=data
    )    
    return response

def register(data):
    
    response = make_request(
        "POST",
        f"{API_URL}register/",
        json=data
    )    
    return response

def reset_password(data):
    
    response = make_request(
        "POST",
        f"{API_URL}reset/",
        json=data
    )        
    return response

def reset_password_confirmation(data):
    response = make_request(
            "PUT",
            f"{API_URL}reset/confirm/",
            json=data
        )        
    return response