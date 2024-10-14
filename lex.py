import string
import tkinter as tk
from tkinter import scrolledtext

def is_identifier(token):
    if token[0].isupper():
        if len(token) <= 20 and all(c in string.ascii_letters + string.digits + '_' for c in token[1:]):
            return True
    return False

def is_string_literal(token):
    return token.startswith('"') and token.endswith('"')

def is_integer_literal(token):
    if "." not in token:
        integer_value = int(token)

        if -999999999 <= integer_value <= 999999999 and len(token.lstrip('-')) <= 9:
            return True
        else:
            pass

def is_float_literal(token):
    float_value = float(token)

    if -999999999 <= float_value <= 999999999 and len(token.lstrip('-')) <= 9:
        if "." in token:
            return True

mathematical_operators = {
    '+' : 'Addition op',
    '-' : 'Subtraction op',
    '/' : 'Division op',
    '*' : 'Multiplication op',
    '%' : 'Modulo op',
    }
mathematical_operators_key = mathematical_operators.keys()

assignment_operators = {
    '=' : 'Assignment op',
    '^' : 'Negate op',
    }
assignment_operators_key = assignment_operators.keys()

relational_operators = {
    '==' : 'Assignment op',
    '>' : 'Negate op',
    '<' : 'Negate op',
    '>=' : 'Negate op',
    '<=' : 'Negate op',
    '!=' : 'Negate op',
    }
relational_operators_key = relational_operators.keys()

logical_operators = {
    '&&' : 'Assignment op',
    '||' : 'Negate op',
    '!' : 'Negate op',
    }
logical_operators_key = logical_operators.keys()

data_type = {
    'dose' : 'integer type', 
    'quant': 'Floating point' , 
    'seq' : 'Character type', 
    'allele' : 'boolean' 
    }
data_type_key = data_type.keys()

other_symbols = { 
    '"' : 'Double Quote', 
    ';' : 'Semi-colon', 
    '_' : 'Identifier Separator' , 
    '(' : 'Open Parenthesis',
    ')' : 'Closed Parenthesis',
    '{' : 'Open Curly Brace',
    '}' : 'Closed Curly Brace',
    '[' : 'Open Square Brace',
    ']' : 'Closed Square Brace',
    '#' : 'Pound'
    }
other_symbols_key = other_symbols.keys()

reserved_words = {
    'if': 'IF_STATEMENT',  
    'else': 'ELSE_STATEMENT', 
    'prod': 'RETURN_STATEMENT',  
    'act': 'DEFINE_STATEMENT',  
    'gene': 'MAIN_STATEMENT',  
    'express': 'PRINT_STATEMENT',   
    'stimuli': 'INPUT_STATEMENT',
    'for': 'FOR_STATEMENT',
    'while': 'WHILE_STATEMENT',
    'destroy': 'BREAK_STATEMENT',
    'contig': 'CONTINUE_STATEMENT',
    'dom': 'TRUE_STATEMENT',
    'rec': 'FALSE_STATEMENT',
    'clust': 'ARRAY_STATEMENT',
    'perms': 'CONST_STATEMENT',
    }
reserved_words_key = reserved_words.keys()

def parse_program():
    count = 0
    output_text.delete(1.0, tk.END)  # Clear the output area
    program = input_text.get(1.0, tk.END).strip().splitlines()  # Get the user input from the Text widget

    for line in program:
        count += 1
        program = input_text.get(1.0, tk.END).strip().splitlines()

        tokens = line.split(' ')
        output_text.insert(tk.END, f"Tokens are: {tokens}\n")
        output_text.insert(tk.END, f"Line# {count} properties:\n")

        for token in tokens:
            if is_string_literal(token):
                output_text.insert(tk.END, f"String Literal: {token}\n")
            if is_identifier(token):
                output_text.insert(tk.END, f"Identifier: {token}\n")
            if is_integer_literal(token):
                output_text.insert(tk.END, f"Integer Literal: {token}\n")
            if token in mathematical_operators_key:
                output_text.insert(tk.END, f"Operator: {mathematical_operators[token]}\n")
            if token in assignment_operators_key:
                output_text.insert(tk.END, f"Operator: {assignment_operators[token]}\n")
            if token in relational_operators_key:
                output_text.insert(tk.END, f"Operator: {relational_operators[token]}\n")
            if token in logical_operators_key:
                output_text.insert(tk.END, f"Operator: {logical_operators[token]}\n")
            if token in data_type_key:
                output_text.insert(tk.END, f"Data Type: {data_type[token]}\n")
            if token in other_symbols_key:
                output_text.insert(tk.END, f"Punctuation: {other_symbols[token]}\n")
            if token in reserved_words_key:
                output_text.insert(tk.END, f"Reserve Words: {reserved_words[token]}\n")
        output_text.insert(tk.END, "_ _ _ _ _ _ _ _ _ _ _ _ _ _\n")

    for value in token:
        result = is_integer_literal(token)
        output_text.insert(tk.END, f"Integer Literal: {value}: {result}\n")
    
    for value in token:
        result = is_float_literal(token)
        output_text.insert(tk.END, f"Float Literal: {value}: {result}\n")

# Creating the tkinter UI
root = tk.Tk()
root.title("Lexical Analyzer")

# Create a Text widget for code input
input_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=10)
input_text.pack(pady=10)

# Create a button to trigger the lexical analyzer
parse_button = tk.Button(root, text="Run", command=parse_program)
parse_button.pack(pady=5)

# Create a ScrolledText widget to display the results
output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=15)
output_text.pack(pady=10)

# Start the tkinter main loop
root.mainloop()