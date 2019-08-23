'获取任务计划'
import re
import sys
import requests
from bs4 import BeautifulSoup
from PyLuogu import _print
from PyLuogu import _link

def read(cid, uid):
    '打印任务计划，需要 cookies __client_id=[cid], _uid=[uid]'
    page = _link.get_page('https://www.luogu.org', cid, uid)
    html = page.text
    task_list = re.findall(r'tasklist-item.*?(<b>.*?</a>)', html, re.S)

    print('你的任务计划：')
    for task in task_list:
        problem_id = re.search(r'<b> *([^<]*) *</b>', task).group(1)
        problem_name = re.search(r'</b> *([^<]*) *</a>', task).group(1)
        _print.print_title(BeautifulSoup('<title>' + problem_id + ' ' +
            problem_name + '</title>'))

if __name__ == '__main__':
    try:
        read(sys.argv[1], sys.argv[2])
    except IndexError:
        print('参数不够')
