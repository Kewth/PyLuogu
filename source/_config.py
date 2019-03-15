'管理配置'
import json
import os

DIR = os.path.expandvars('$HOME') + '/.local/share/PyLuogu/'

def load():
    '获得配置'
    try:
        config_file = open(DIR + 'status', 'r')
    except FileNotFoundError:
        os.mknod(DIR + 'status')
        config_file = open(DIR + 'status', 'r')
    config_str = config_file.readline()[:-1]
    try:
        config_dict = json.loads(config_str)
    except json.decoder.JSONDecodeError:
        config_dict = {}
    return config_dict

def write(config_dict):
    '写入配置'
    config_str = json.dumps(config_dict)
    config_file = open(DIR + 'status', 'w')
    config_file.write(config_str)
