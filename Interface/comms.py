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
            "message" : "No se pudo conectar con el servidor"
        }
        
    except requests.exceptions.Timeout:
        return {
            "connection_status" : False,
            "response" : None,
            "message" : "El servidor tardó demasiado en responder"
        }
    except requests.exceptions.RequestException as error:
        return {
            "connection_status" : False,
            "response" : None,
            "message" : str(error)
        }
 
def login(data):
    
    response = make_request(
        "POST",
        f"{API_URL}login/",
        json=data
    )
    print(response)
    
    return response

