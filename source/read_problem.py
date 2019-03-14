#!/usr/bin/python3
'获取指定题目页面'
from urllib import request
import sys
from PyLuogu import _print

def read(problem_id):
    '获取 [problem_id] 题目的信息'
    html = request.urlopen( \
            'https://www.luogu.org/problemnew/show/{}'.format( \
            problem_id)).read().decode('utf-8')
    _print.print_html(html)

if __name__ == '__main__':
    read(sys.argv[1])
