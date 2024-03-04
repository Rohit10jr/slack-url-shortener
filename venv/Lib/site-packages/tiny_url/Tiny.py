import requests

def make_url(url):
    """
    make tiny url
    """
    r = requests.post(
        'https://tiny-url.gq/api/make',
        {'original':f'{url}'})
    
    return r.text
