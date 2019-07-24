# -*- coding:utf-8 -*-


import requests


def notice(key, title, text):
    url = 'https://sc.ftqq.com/'+key+'.send'
    data = {
        "text": title,
        "desp": text
    }
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0"
    }
    req = requests.post(url, data=data, headers=headers)
    return req.content
