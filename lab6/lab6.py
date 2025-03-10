from calc import *
import copy


def exec_program(code, my_table = {}):
    """executes the program if list starts with 'calc'"""
    if is_program(code):
        statements = program_statements(code)
        return exec_statements(statements,my_table)
    
    else:
        return 'Exeption: did not inisiate with "calc"'


def exec_statements(statements, memory):
    """gets a list of statements"""

    if is_statements(statements):

        statement = first_statement(statements)
        memory = exec_statement(statement, memory)
        if rest_statements(statements):
            memory = exec_statements(rest_statements(statements),memory)
        return memory
    
    return memory


def exec_statement(statement, memory):
    """preformes the statement that is given"""

    if is_selection(statement):
        return exec_selection(statement,memory)
        
    elif is_output(statement):
        return exec_output(statement,memory)
        
    elif is_assignment(statement):
        return exec_assignment(statement,memory)

    elif is_repetition(statement):
        return exec_repition(statement,memory)

    elif is_input(statement):
        return exec_input(statement,memory)

    return memory


def exec_assignment(statement,memory):
    """gives a variable a value"""

    memory = copy.deepcopy(memory)

    memory[assignment_variable(statement)] = eval_expression(assignment_expression(statement),memory) # changed to eval

    return memory


def exec_output(statement,memory):
    """prints a variable and value or expression of statement"""

    if is_variable(output_expression(statement)):
        print(output_expression(statement),'=',eval_variable(output_expression(statement), memory))

    else:
        print(output_expression(statement))

    return memory


def exec_input(statement,memory):
    """gives user instruction to input a value into a variable in the terminal"""

    memory = copy.deepcopy(memory)

    memory[input_variable(statement)] = eval(input(f'Enter value for {input_variable(statement)}: '))

    return memory


def exec_selection(statement,memory):
    """preforms an selection depending on condition operator"""

    if eval_condition(selection_condition(statement), memory): # changed to eval
        return exec_statements([selection_true_branch(statement)],memory) 

    elif selection_has_false_branch(statement):
        return exec_statements([selection_false_branch(statement)],memory)
    
    return memory
    

def exec_repition(statement,memory):
    """preforms a loop while the condition is true"""

    while eval_condition(repetition_condition(statement), memory): # changed to eval
        memory = exec_statements(repetition_statements(statement), memory)

    return memory


def eval_expression(expression, memory):
    """returns int value of expression"""

    if is_binaryexpr(expression):
        return eval_binaryexpr(expression,memory)

    elif is_variable(expression): 
        return eval_variable(expression,memory)

    elif is_constant(expression):
        return eval_constant(expression,memory)


def eval_binaryexpr(expression,memory):

        left = eval_expression(binaryexpr_left(expression),memory)
        right = eval_expression(binaryexpr_right(expression),memory)
        operator = binaryexpr_operator(expression)
        
        if operator == '+':
            return left + right

        elif operator == '-':
            return left - right

        elif operator == '*':
            return left * right

        elif operator == '/':
            return left / right


def eval_condition(expression,memory):

        left = eval_expression(condition_left(expression),memory)
        right = eval_expression(condition_right(expression),memory)
        operator = condition_operator(expression)

        if operator == '>':
            return left > right

        elif operator == '<':
            return left < right
            
        elif operator == '=':
            return left == right


def eval_constant(expression,memory):
    """returns the number given"""
    return expression


def eval_variable(expression, memory):
    """returns the value of a variable"""
    return memory[expression]


if __name__ == "__main__":
    calc1 = ['calc', ['print', 2], ['print', 4]]
    calc2 = ['calc', ['if', [6, '>', 5], ['print', 2], ['print', 4]]]
    calc3 = ['calc', ['set', 'a', [3,'+',3]], ['print', 'a']]
    calc4 = ['calc', ['read', 'p1'],['print','p1']]
    calc5 = ['calc', ['set','n',0],['while',['n','<',6],['set','n',['n','+',1]],['print', "n"]]]
    calc6 = ["calc", ['print','a'], ["set", "a", 5]]
    calc7 = ["calc", ['if', [[2,'+',1],"<",[8,'/',2]],["print",'true'],['print','false']]]
    calc8 = ["calc", ['if', [[2,'+',1],"<",[8,'/',2]],
                        ["if",[[2,'<',5],'=',[3,'=',3]],
                            ['print','dubble selection'],
                        ['print','failed dubble']],
                    ['print','did not enter dubble']]]

    _loop_prog = [
        "calc",
        ["read", "n"],
        ["set", "sum", 0],
        [
            "while",
            ["n", ">", 0],
            ["set", "sum", ["sum", "+", "n"]],
            ["set", "n", ["n", "-", 1]],
        ],
        ["print", "sum"]]

    _if_set_prog = [
        "calc",
        ["read", "x"],
        ["if", ["x", ">", 0], ["set", "a", 1], ["set", "a", -1]],
        ["if", ["x", "=", 0], ["set", "a", 0]],]

    _loop_with_binexpr_prog = [
        "calc",
        ["read", "n"],
        ["set", "sum", 0],
        [
            "while",
            [["n", "-", 1], ">", 0],
            ["set", "sum", ["sum", "+", "n"]],
            ["set", "n", ["n", "-", 1]],
        ],
        ["print", "sum"],]

    calc_fib = ['calc',
            ['read', 'n'],
            ['set', 'last', 1],
            ['set', 'butlast', 1],
            ['set', 'result', 1],
            ['while', ['n', '>', 2],
                ['set', 'result', ['last', '+', 'butlast']],
                ['set', 'butlast', 'last'],
                ['set', 'last', 'result'],
                ['set', 'n', ['n', '-', 1]]],
            ['print', 'result']]

    exec_program(calc_fib)
