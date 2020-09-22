'''
topic: context-sensitive language; regular expression; braces/brackets/parentheses matcher
input: str(symbols)
output: str(não casada) or str(casada e correta) or (str(casada e correta) and str(correct_symbols_order))
21/09/2020 by Letícia Minelvino
'''
import re
class Stack:
    def __init__(self):
        self._data = []
    def is_empty(self):
        return self._data == []
    def push(self, e):
        self._data.append(e)
    def top(self):
        if self.is_empty():
            return self._data
        return self._data[-1]
    def pop(self):
        if self.is_empty():
            return self._data
        return self._data.pop() 
    def size(self):
        return len(self._data)

def is_it_correct(string):
    return not bool(re.search(r'(\(\[)|(\(\{)|(\[\{)|(\]\))|(\}\))|(\}\))|(\(\})|(\[\})|(\{\))|(\{\])|(\[\))', string)) 
 
def fix_it(string):
    fixed = False
    while not fixed:
        string = re.sub(r'\(\{', '{(', string)
        string = re.sub(r'\(\[', '[(', string)
        string = re.sub(r'\[\{', '{[', string)
        string = re.sub(r'\}\)', ')}', string)
        string = re.sub(r'\]\)', ')]', string)
        string = re.sub(r'\}\]', ']}', string)
        fixed = is_it_correct(string)
    return string

#start
stack = Stack()  
string = str(input())
matched_and_incorrect_strings = []
while (string != ''):
    string = re.sub(r' ', '', string)
    braces_counter = 0
    brackets_counter = 0
    parenthesis_counter = 0
    string_aux = ''
    for i in string:
        stack.push(i)
    for i in range(stack.size()):
        top = stack.pop()
        if top == '(':
            parenthesis_counter += 1
            if bool(re.search(r'(?<!\()\)', string_aux)) == True: 
                string_aux+=top
        elif top == ')':
            parenthesis_counter -= 1
            string_aux += top
        elif top == '[':
            brackets_counter += 1
            if bool(re.search(r'(?<!\[)\]', string_aux)) == True:
                string_aux+=top
        elif top == ']':
            brackets_counter -= 1
            string_aux+=top
        elif top == '{':
            braces_counter += 1
            if bool(re.search(r'(?<!\{)\}', string_aux)) == True: 
                string_aux += top
        elif top == '}':
            braces_counter -= 1
            string_aux += top
    if (parenthesis_counter == 0) and (braces_counter == 0) and (brackets_counter == 0) and ((len(string_aux)) == (len(string))):
        correct = is_it_correct(string)
        if not correct:
            matched_and_incorrect_strings.append(string)
            print('casada e incorreta')
        else:
            print('casada e correta')   
    else:
        print('nao casada')
    string = str(input())

for incorrect in matched_and_incorrect_strings:
    correct = fix_it(incorrect)
    print(correct)
