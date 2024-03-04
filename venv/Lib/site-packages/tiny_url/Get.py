import requests

def get_original(t='undefined'):
    """
    get tiny url
    """
    r = requests.get(
        'https://tiny-url.gq/api/get',
        params={'t':f'{t}'})
    return r.text

def get_tiny(o="undefined"):
    """
    get tiny url
    """
    r = requests.get(
        'https://tiny-url.gq/api/gettiny',
        params={'o':f'{o}'})
    return r.text

