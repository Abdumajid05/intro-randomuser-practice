import requests 
import json
url = 'https://randomuser.me/api/'


def get_version():
    '''get requests module'''
    return requests.__version__


def get_status_code(url: str) -> int:
    '''get status code of response
    
    Args:
        url (str): api url
    
    Returns:
        str: status code of response
    '''
    return requests.get(url)

 
def get_content_type(url: str) -> str:
    '''get content type of response
    
    Args:
        url (str): api url
    
    Returns:
        str: content type of response
    '''
    return requests.get(url).content


def get_headers(url: str) -> dict:
    '''get headers of response
    
    Args:
        url (str): api url
    
    Returns:
        str: headers of response
    '''
    return requests.get(url).headers


def get_text(url: str) -> str:
    '''get text of response
    
    Args:
        url (str): api url
    
    Returns:
        str: text of response
    '''
    return  requests.get(url).text



def text_to_dict(text: str) -> dict:
    '''convert text to dict
    
    Args:
        text (str): text of response
    
    Returns:
        str: dict
    '''
    return json.dumps(text)


def get_data(url: str) -> dict:
    '''get data of response. use method json()
    
    Args:
        url (str): api url
    
    Returns:
        dict: data
    '''
    return requests.get(url).json()


def get_user(url: str) -> dict:
    '''get user
    
    Args:
        url (str): api url
    
    Returns:
        dict: user
    '''
    return requests.get(url).json()["results"][0]

def get_users(url: str, n: int) -> list:
    '''get user
    
    Args:
        url (str): api url
        n (int): number of users
    
    Returns:
        list: list of users
    '''
    l=[]
    for i in range(n):
        l.append(requests.get(url).json()["results"][0])
    return l
#print(text_to_dict(get_text(url)))
print(get_users(url,100))