'用户信息管理'
from PyLuogu import _config

def get_cid():
    '获取 __client_id'
    config = _config.load()
    return config.get('cid')

def get_uid():
    '获取 _uid'
    config = _config.load()
    return config.get('uid')

def login(cid, uid):
    '记录 __client_id = [cid], _uid = [uid] 登录信息'
    config = _config.load()
    config['cid'] = cid
    config['uid'] = uid
    _config.write(config)

def login_help():
    '打印关于登录的帮助'
    print('''
无需用户名和密码，PyLuogu 采用 __client_id + _uid 的方式登录
_uid 即你的用户编号
__client_id 的获取方式如下：
1. 如果浏览器有关于 cookie 的插件，在洛谷可以直接查看到
2. 否则，在洛谷按 F12 审查
3. 点击 Network
4. 点击 Doc
5. 点击 www.luogu.org （如果没有就刷新，比如 Chrome 上按 Ctrl-r ）
6. 找到 Request Headers ，其中有一个 cookie 的字段有 __client_id 的值
    ''')
