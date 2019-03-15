'获取指定题目页面'
import sys
from PyLuogu import _print
from PyLuogu import _link

def search(name):
    '搜索题目'
    page = _link.get_page( \
            'https://www.luogu.org/problemnew/lists?name=\
{}&orderitem=pid&tag=&content=0&type='.format(name), None, None)
    _print.print_problem_list(page.text)

def read(problem_id):
    '获取 [problem_id] 题目的信息'
    page = _link.get_page( \
            'https://www.luogu.org/problemnew/show/{}'.format( \
            problem_id), None, None)
    _print.print_problem_html(page.text)

if __name__ == '__main__':
    try:
        read(sys.argv[1])
    except IndexError:
        print('请给出参数')
