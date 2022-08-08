import requests
from bs4 import BeautifulSoup as bs

url = 'https://login.dnevnik.ru/login/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'}


def registration(login, password):
    session = requests.Session()
    r = session.get(url, headers=headers)
    session.headers.update({'Referer': url})
    session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'})
    _xsrf = session.cookies.get('_xsrf')
    post_req = session.post(url, {
        'login': login,
        'password': password,
        '_xsrf': _xsrf,
        'remember': 'yes'})
    try:
        soup = bs(post_req.content, 'html.parser')
        res = soup.findAll("div", {"class": "message"})[0].text
        return False
    except IndexError:
        return True

