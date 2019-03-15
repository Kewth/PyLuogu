#!/usr/bin/python3
'PyLuogu 的框架'
import argparse
from PyLuogu import read_problem
from PyLuogu import read_task

def __func_problem__(args):
    read_problem.read(args.pid)

def __func_task__(args):
    # TODO
    pass

def __func_login__(args):
    # TODO
    pass

def init_args():
    '初始化参数'
    parser = argparse.ArgumentParser(description='''
在终端，享受 Coding 的快乐
                ''')
    sub_parser = parser.add_subparsers(dest='subcommands')
    parser_problem = sub_parser.add_parser('problem', help='在洛谷阅读题目')
    parser_problem.set_defaults(func=__func_problem__)
    parser_problem.add_argument('pid', help='题目的题号')
    parser_task = sub_parser.add_parser('task', help='洛谷任务计划')
    parser_task.set_defaults(func=__func_task__)
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
