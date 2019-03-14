#!/usr/bin/python3
'PyLuogu 的框架'
import argparse
from PyLuogu import read_problem
from PyLuogu import read_task

def init_args():
    '初始化参数'
    parser = argparse.ArgumentParser(description='''
在终端，享受 Coding 的快乐
                ''')
    parser.add_argument('-p', '--problem', action='append',
                        help='在洛谷阅读题目 [PROBLEM]')
    parser.add_argument('-t', '--task', action='store_true',
                        help='读取任务计划，需要用户信息')
    parser.add_argument('-c', '--cid', action='append',
                        help='给定用户的 __client_id')
    parser.add_argument('-u', '--uid', action='append',
                        help='给定用户的 _uid')
    return parser.parse_args()

def main():
    '运行 PyLuogu'
    args = init_args()
    cid, uid = None, None
    if args.cid:
        cid = args.cid[0]
    if args.uid:
        uid = args.uid[0]
    if args.problem:
        read_problem.read(args.problem[0])
    elif args.task:
        if not uid:
            print('未给定 uid')
        if not cid:
            print('未给定 cid')
        if cid and uid:
            read_task.read(cid, uid)

if __name__ == '__main__':
    main()
