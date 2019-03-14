#!/usr/bin/python3
import argparse
from PyLuogu import read_problem

def init_args():
    parser = argparse.ArgumentParser(description='''
I'm too lazy to write this.
                ''')
    parser.add_argument('-p', '--problem', action='append',
            help='Read a problem')
    return parser.parse_args()

def main():
    args = init_args()
    if args.problem:
        read_problem.read(args.problem[0])

if __name__ == '__main__':
    main()
