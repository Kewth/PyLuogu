'处理链接方式'
import requests

def headers(cid, uid):
    '获取请求头'
    return { \
            'user-agent': \
            'Mozilla/5.0 (X11; Linux x86_64) \
            AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/72.0.3626.121 Safari/537.36', \
            'cookie': \
            '__client_id={}; _uid={}'.format(cid, uid)
            }

def get_page(url, cid, uid):
    '获取页面'
    return requests.get(url, headers=headers(cid, uid))
