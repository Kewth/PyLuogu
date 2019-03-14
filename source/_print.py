'打印页面'
from bs4 import BeautifulSoup
import colorama

def print_content(html):
    '解析一段信息并打印'
    label = ''
    text = ''
    to_be_print = []
    for char in html:
        if char == '<':
            label = '<'
            to_be_print.append(text)
            text = ''
        elif char == '>':
            to_be_print.append(label + '>')
            label = ''
        elif label != '':
            label += char
        else:
            text += char
    to_be_print.append(label)
    to_be_print.append(text)
    ignore = 0
    for content in to_be_print:
        if content in ('', '\n', '<p>', \
                '</li>', '</div>', '<ol>', '</ol>'):
            pass
        elif content[:4] == '<div':
            pass
        elif content[:8] == '<a class':
            ignore += 1
        elif content in ('</a>', '</fuck>'):
            ignore -= 1
        elif content == '</p>':
            print()
        elif content == '<strong>':
            print(colorama.Style.BRIGHT, end='>')
        elif content == '</strong>':
            print(colorama.Style.NORMAL, end='<')
        elif content == '<pre>':
            print(colorama.Fore.CYAN)
        elif content == '</pre>':
            print(colorama.Fore.RESET)
        elif content == '<li>':
            print('{}-{}  '.format( \
                    colorama.Fore.BLUE, colorama.Fore.RESET), end='')
        elif content in ('<br>', '<br/>', '<br />'):
            print()
        elif content[0] == '<':
            print(colorama.Fore.YELLOW, content, \
                    colorama.Fore.RESET, end='')
        elif ignore == 0:
            print(content.replace('&lt;', '<').replace('&gt;', '>'), end='')
    # print(html)

def print_title(tree):
    '打印标题'
    print('{}Title:{} {}{}'.format( \
            colorama.Fore.RED, colorama.Fore.GREEN, \
            tree.find('title').text, colorama.Fore.RESET))

def print_difficulty(tree):
    '打印难度'
    for i in tree.find_all('strong'):
        if i.text == '难度':
            get = i.find_parent().find_all('span')[1]
            print('{}Difficulty:{} {}{}'.format( \
                    colorama.Fore.RED, colorama.Fore.GREEN, \
                    get.text, colorama.Fore.RESET))

def print_description(tree):
    '打印题目描述'
    for i in tree.find_all('h2'):
        if i.text == '题目描述':
            print('{}Description:{}'.format( \
                    colorama.Fore.RED, colorama.Fore.RESET))
            content = ''
            for j in i.next_siblings:
                if j == '\n':
                    continue
                elif j.name == 'h2':
                    break
                content += j.__str__() + '\n'
            print_content(content)

def print_format(tree):
    '打印输入输出格式'
    for i in tree.find_all('h2'):
        if i.text == '输入输出格式':
            print('{}IO Format:{}'.format( \
                    colorama.Fore.RED, colorama.Fore.RESET))
            content = ''
            for j in i.next_siblings:
                if j == '\n':
                    continue
                elif j.name == 'h2':
                    break
                content += j.__str__() + '\n'
            print_content(content)

def print_sample(tree):
    '打印输入输出样例'
    for i in tree.find_all('h2'):
        if i.text == '输入输出样例':
            print('{}IO Sample:{}'.format( \
                    colorama.Fore.RED, colorama.Fore.RESET))
            content = ''
            for j in i.next_siblings:
                if j == '\n':
                    continue
                elif j.name == 'h2':
                    break
                content += j.__str__() + '\n'
            print_content(content)

def print_note(tree):
    '打印说明'
    for i in tree.find_all('h2'):
        if i.text == '说明':
            print('{}NOTE:{}'.format( \
                    colorama.Fore.RED, colorama.Fore.RESET))
            content = ''
            for j in i.next_siblings:
                if j == '\n':
                    continue
                elif j.name == 'h2':
                    break
                content += j.__str__() + '\n'
            print_content(content)

def print_html(html):
    '解析 html 并打印'
    tree = BeautifulSoup(html, 'lxml')
    print_title(tree)
    print_difficulty(tree)
    print_description(tree)
    print_format(tree)
    print_sample(tree)
    print_note(tree)
