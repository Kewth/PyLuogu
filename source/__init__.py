#!/usr/bin/python3
'PyLuogu 的框架'
import argparse
from PyLuogu import read_problem
from PyLuogu import read_task
from PyLuogu import user_management

def __func_problem__(args):
    if args.search:
        read_problem.search(args.search)
    else:
        read_problem.read(args.pid)

def __func_task__(args):
    read_task.read(user_management.get_cid(), user_management.get_uid())

def __func_login__(args):
    if args.learn:
        user_management.login_help()
    elif args.cid and args.uid:
        user_management.login(args.cid, args.uid)
    else:
        cid = input('__client_id: ')
        uid = input('_uid: ')
        user_management.login(cid, uid)

def init_args():
    '初始化参数'
    parser = argparse.ArgumentParser(description='''
在终端，享受 Coding 的快乐
                ''')
    sub_parser = parser.add_subparsers(dest='subcommands')
    parser_problem = sub_parser.add_parser('problem', \
            help='在洛谷阅读题目', description='输出经过处理的题目')
    parser_problem.set_defaults(func=__func_problem__)
    parser_problem.add_argument('pid', nargs='?', help='题目的题号')
    parser_problem.add_argument('-s', '--search', action='store', \
            help='按题目名搜索')
    parser_task = sub_parser.add_parser('task', help='洛谷任务计划', \
            description='查看洛谷的任务计划（需要登录）')
    parser_task.set_defaults(func=__func_task__)
    parser_login = sub_parser.add_parser('login', help='登录洛谷', \
            description='登录洛谷（ login -l 查看方式）')
    parser_login.add_argument('cid', nargs='?', help='__client_id 的值')
    parser_login.add_argument('uid', nargs='?', help='_uid 的值')
    parser_login.add_argument('-l', '--learn', action='store_true', \
            help='学习如何使用 PyLuogu 登录')
    parser_login.set_defaults(func=__func_login__)
    return parser

def main():
    '运行 PyLuogu'
    parser = init_args()
    args = parser.parse_args()
    if not args.subcommands:
        print('Error: 未给出子命令')
        parser.print_help()
        exit(1)
    args.func(args)

if __name__ == '__main__':
    main()
