'获取任务计划'
import sys
import requests
from bs4 import BeautifulSoup
from PyLuogu import _print
from PyLuogu import _link

def read(cid, uid):
    '打印任务计划，需要 cookies __client_id=[cid], _uid=[uid]'
    page = _link.get_page('https://www.luogu.org', cid, uid)
    # XXX
    html = page.text
    print('你的任务计划：')
    while True:
        end = html.find('完成任务')
        if end == -1:
            break
        end -= 2
        begin = html[:end].rfind('data-pid="') + 10
        if begin > end:
            break
        problem = requests.get( \
                'https://www.luogu.org/problemnew/show/{}'.format( \
                html[begin:end]), headers=headers)
        tree = BeautifulSoup(problem.text, 'lxml')
        _print.print_title(tree)
        html = html[end + 6:]

if __name__ == '__main__':
    try:
        read(sys.argv[1], sys.argv[2])
    except IndexError:
        print('参数不够')
