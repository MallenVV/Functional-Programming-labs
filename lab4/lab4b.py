import os

def cls():                      # cleans previous terminal
    if os.name == 'nt':
        os.system('cls')
    else: os.system('clear')

cls()


def string_to_list(string_seq):  # 
    """makes sure that operators are in a list"""

    ls=[]

    if type(string_seq) == str:
        ls.append(string_seq)
        return ls
    
    else: return string_seq


def variable_value(op,variables):
    """checks the value a vairable is given. if it does not exist we asume it is already 'true' or 'false'."""
    
    if op in variables:
        state = variables[op]
    else:
        state = op
    
    return state


def interpret(seq,variables):
    """Main function that determains the state of the operators"""

    v = variables
    seq = string_to_list(seq)
    operators = []

    if len(seq) == 1:   # Funktion som ger tillbaka värdet på seq då det är ett värde i listan
        value = seq[0]
        if type(value) == list:
            return interpret(value,v)
        else:
            return variable_value(value,v)
        

    elif len(seq) == 2: # Funktion som löser NOT på seq då det är två värden i listan
        right = seq[0]
        left = seq[1]
        if right == 'NOT':
            if type(left) == list:
                state = interpret(left,v)
            else:
                state = variable_value(left,v)
            
            if state == 'true': return 'false'
            else: return 'true'

        else: return False

    elif len(seq) == 3: # Funktion som löser AND eller OR på seq då det är tre värden i listan
        left = seq[0]
        middle = seq[1]
        right = seq[2]

        if type(left) == list:
            left = interpret(left,v)
        if type(right) == list:
            right = interpret(right,v)

        if middle == 'OR':
            
            if (variable_value(left,v) == 'true' or variable_value(right,v) == 'true'): return 'true'
            else: return 'false'

        elif middle == 'AND':
            
            if (variable_value(left,v) == 'true' and variable_value(right,v) == 'true'): return 'true'
            else: return 'false'
        
        else: return False