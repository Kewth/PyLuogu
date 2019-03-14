'获取任务计划'
import sys
import requests

def read(cid, uid):
    print(cid, uid)
    '打印任务计划，需要 cookies __client_id=[cid], _uid=[uid]'
    page = requests.get('https://www.luogu.org/', headers={ \
            'user-agent': \
            'Mozilla/5.0 (X11; Linux x86_64) \
            AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/72.0.3626.121 Safari/537.36', \
            'cookie': \
            '__client_id={}; _uid={}'.format(cid, uid)})
    # XXX
    html = page.text
    print('你的任务计划：')
    while True:
        end = html.find('完成任务')
        if end == -1:
            break
        end -= 2
        begin = html[:end].rfind('data-pid="') + 10
        # print()
        # print(begin, end)
        # print(html[begin-10:begin+10])
        # print(html[end-10:end+10])
        # print()
        if begin > end:
            break
        print(html[begin:end])
        html = html[end + 6:]

if __name__ == '__main__':
    try:
        read(sys.argv[1], sys.argv[2])
    except IndexError:
        print('参数不够')
