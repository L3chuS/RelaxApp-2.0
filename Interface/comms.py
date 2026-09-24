import requests
from settings import API_URL
from user_temporary_settings import Session

def make_request(method, url, **kwargs):
    
    try:
        
        headers = kwargs.pop("headers", {})
        
        if Session.token:
            headers["Authorization"] = f"Token {Session.token}"

        response =  requests.request(
            method,
            url,
            headers=headers,
            timeout=10,
            **kwargs
        )

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

# def validate_profiles(data):
#     response = make_request(
#         "POST",
#         f"{API_URL}profiles/validate/",
#         json=data
#     )
#     return response

def data_validate(data):
    response = make_request(
        "POST",
        f"{API_URL}data/validate/",
        json=data,
    )
    return response