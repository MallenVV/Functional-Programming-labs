import os

def cls():                      # cleans previous terminal
    if os.name == 'nt':
        os.system('cls')
    else: os.system('clear')

cls()


def split_it(string):   
    """Iterative way to split into two words"""

    lower_string = ''
    upper_string = ''

    for each in string: 

        if each.islower() == True or each == '_' or each == '.':
            lower_string = lower_string + each
            
        elif each.isupper() == True or each == '|' or each == ' ':
            upper_string = upper_string + each

    return lower_string, upper_string


def split_rec(string):
    """Recursive way to split into two words"""

    if len(string) == 0:
        return '',''
    
    else:
        lower_string, upper_string = split_rec(string[1:])  # returns previous letters into separete strings
        first = string[0]

        if first.islower() == True or first == '_' or first == '.': # chooses where the letter goes for latest letter
            
            return first + lower_string, upper_string 
        
        elif first.isupper() == True or first == ' ' or first == '|':
            
            return lower_string, first + upper_string
        
        else: return lower_string, upper_string

