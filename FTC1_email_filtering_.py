"""
topic: regular expressions; email filtering

input: str(file_name)
output: str(ham) or str(spam)

18/08/2020 by Letícia Minelvino
"""
import re

#functions, head
def check_begin(line1):
    check = re.search(r'^(-){5}beginmessage(-){5}$', line1)
    if (check == None):
        return 1
    else:
        return 0

def check_from(line2):
    check = re.search(r'from: (.+).*\@[\w\.]+;$', line2)
    if (check == None):
        return 1
    else:
        return 0

def check_to(line3):
    check = re.search(r'to: (.+).*\@[\w\.]+;$', line3)
    if (check == None):
        return 1
    else:
        return 0   

def check_ip(line4):
    check = re.search(r'(\d+\.){3}\d+', line4)
    if (check == None):
        return 1
    else:
        return 0

def check_time_stamp(line5):
    check = re.search(r'^\d{4}\.\d{2}.\d{2} \d{2}:\d{2}:\d{2}$', line5)
    if (check == None):
        return 1
    else:
        return 0

def check_separator(line6):
    check = re.search(r'^(-){23}$', line6)
    if (check == None):
        return 1
    else:
        return 0


#functions, body
def find_suspicious_email(body):
    check = re.search(r'(.+).*\@[\w\.]+', body)
    if (check == None):
        return 0
    else:
        return 1

def find_suspicious_html(body):
    check = re.search(r'<.+>|<\/.+>', body)
    if (check == None):
        return 0
    else:
        return 1

def find_suspicious_words(body): 
    check = re.search(r'milionario|emprestimo|loteria|banco|heranca|seguidor|desconto', body, flags= re.I)
    if (check == None):
        return 0
    else:
        return 1
    
def find_suspicious_ponctuation(body):
    check = re.findall(r'\;|\,|\.', body)
    if (len(check) <= 15):
        return 0
    else:
        return 1
    
def find_suspicious_word_structures(body):
    all_words = body.split()
    all_words.pop()
    for word in all_words:
        its_consonants = len(re.findall(r'b|c|d|f|g|h|j|k|l|m|n|p|q|r|s|t|v|w|x|y|z', word, flags = re.I))
        its_vowels = len(re.findall(r'a|e|i|o|u', word, flags = re.I))
        if((its_consonants + its_vowels) > 11):
            if(its_consonants > its_vowels):
                return 1
            else:
                return 0
    

#function, last line
def check_end(lastline):
    check = re.search(r'(-){5}endmessage(-){5}', lastline)
    if (check == None):
        return 1
    else:
        return 0

    
#start
file_name = str(input().strip("\r")) #remove the \r from input
with open(file_name, 'r') as email: 
    check = [] 
    line = email.readline() #reading 6 lines from the file 
    check.append(check_begin(line))
    line = email.readline()
    check.append(check_from(line))
    line = email.readline()
    check.append(check_to(line))
    line = email.readline()
    check.append(check_ip(line))
    line = email.readline()
    check.append(check_time_stamp(line))
    line = email.readline()
    check.append(check_separator(line))
    if 1 in check:
        print('spam') 
        
    else:
        check = []
        body_lines = email.readlines() #putting the remaining lines in a list
        body = ''.join(body_lines) #removing the lines from the list; type(body) == str
        check.append(find_suspicious_email(body))
        check.append(find_suspicious_html(body))
        check.append(find_suspicious_words(body))
        check.append(find_suspicious_ponctuation(body))
        check.append(find_suspicious_word_structures(body))
        check.append(check_end(body))
        if 1 in check:
            print('spam')
            
        else:
            print('ham')