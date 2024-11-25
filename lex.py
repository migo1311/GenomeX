import string
import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk

def is_identifier(token):
    if token[0].isupper():
        if len(token) <= 20 and all(c in string.ascii_letters + string.digits + '_' for c in token[1:]):
            return True
    return False

def is_string_literal(token):
    return token.startswith('"') and token.endswith('"') and len(token) > 1


def is_float_literal(token):
    if "." in token:
        try:
            float_value = float(token)
            
            whole_part, decimal_part = token.split('.')
            
            if -999999999 <= float_value <= 999999999 and \
               len(token.lstrip('-')) <= 9 and \
               len(decimal_part) <= 7:
                return True
            else:
                return False
        except ValueError:
            return False
    return False

def is_integer_literal(token):
    try:
        integer_value = int(token)
        if -999999999 <= integer_value <= 999999999 and len(token.lstrip('-')) <= 9:
            return True
        else:
            return False
    except ValueError:
        return False

delimiters = {',': 'COMMA', ';': 'SEMICOLON', '(': 'OPEN_PAREN', ')': 'CLOSE_PAREN', ':': 'COLON'}

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
    '>' : 'Equal Than',
    '<' : 'Greater Than',
    '>=' : 'Less Than or Equal',
    '<=' : 'Greater Than or Equal',
    '!=' : 'Not Equal',
    }
relational_operators_key = relational_operators.keys()

logical_operators = {
    '&&' : 'AND',
    '||' : 'OR',
    '!' : 'NOT',
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
    ';' : 'Semi-colon', 
    '_' : 'Identifier Separator' , 
    '(' : 'Open Parenthesis',
    ')' : 'Closed Parenthesis',
    '{' : 'Open Curly Brace',
    '}' : 'Closed Curly Brace',
    '[' : 'Open Square Brace',
    ']' : 'Closed Square Brace',
    '#' : 'Pound',
    '\n' : 'Newline',
    ' ' : 'Space'
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

delim_gen = [" "]

#Dito if else para sa lahat ng possible na tokens
def process_token(token, count, output_text, lexical_result, 
                  mathematical_operators, assignment_operators, relational_operators, 
                  logical_operators, data_type, other_symbols, reserved_words):
    
    if token in mathematical_operators:
        output_text.insert(tk.END, f"Data Type: {mathematical_operators[token]}\n")
        lexical_result.insert('', 'end', values=(count, token, mathematical_operators[token]))
        output_text.insert(tk.END, f"Token: {token}\n")
        return count + 1

    if token in assignment_operators:
        output_text.insert(tk.END, f"Operator: {assignment_operators[token]}\n")
        lexical_result.insert('', 'end', values=(count, token, assignment_operators[token]))
        output_text.insert(tk.END, f"Token: {token}\n")
        return count + 1

    if token in relational_operators:
        output_text.insert(tk.END, f"Operator: {relational_operators[token]}\n")
        lexical_result.insert('', 'end', values=(count, token, relational_operators[token]))
        output_text.insert(tk.END, f"Token: {token}\n")
        return count + 1

    if token in logical_operators:
        output_text.insert(tk.END, f"Operator: {logical_operators[token]}\n")
        lexical_result.insert('', 'end', values=(count, token, logical_operators[token]))
        output_text.insert(tk.END, f"Token: {token}\n")
        return count + 1

    if token in data_type:
        output_text.insert(tk.END, f"Data Type: {data_type[token]}\n")
        lexical_result.insert('', 'end', values=(count, token, data_type[token]))
        output_text.insert(tk.END, f"Token: {token}\n")
        return count + 1

    if token in other_symbols:
        display_token = "\\n" if token == "\n" else token
        output_text.insert(tk.END, f"Data Type: {other_symbols[token]}\n")
        lexical_result.insert('', 'end', values=(count, display_token, other_symbols[token]))
        output_text.insert(tk.END, f"Token: {display_token}\n")
        return count + 1

    if token in reserved_words:
        output_text.insert(tk.END, f"Data Type: {reserved_words[token]}\n")
        lexical_result.insert('', 'end', values=(count, token, reserved_words[token]))
        output_text.insert(tk.END, f"Token: {token}\n")
        return count + 1

    if is_string_literal(token):
        output_text.insert(tk.END, f"Identifier: {token}\n")
        lexical_result.insert('', 'end', values=(count, token, "String Literal"))
        output_text.insert(tk.END, f"Token: {token}\n")
        return count + 1

    if is_identifier(token):
        output_text.insert(tk.END, f"Identifier: {token}\n")
        lexical_result.insert('', 'end', values=(count, token, "Identifier"))
        output_text.insert(tk.END, f"Token: {token}\n")
        return count + 1

    if is_float_literal(token):
        output_text.insert(tk.END, f"Float: {token}\n")
        lexical_result.insert('', 'end', values=(count, token, "Float Literal"))
        output_text.insert(tk.END, f"Token: {token}\n")
        return count + 1

    if is_integer_literal(token):
        output_text.insert(tk.END, f"Integer: {token}\n")
        lexical_result.insert('', 'end', values=(count, token, "Integer Literal"))
        output_text.insert(tk.END, f"Token: {token}\n")
        return count + 1

    return count

#Basa ng text to token
def parse_program():
    output_text.delete(1.0, tk.END)  # Clear the output area
    program = input_text.get(1.0, tk.END).strip().splitlines(keepends=True) 
    
    for item in lexical_result.get_children():
        lexical_result.delete(item)
    
    count = 1  

    for line in program:
        output_text.insert(tk.END, f"Line# {count}\n{line}\n")
        tokens = []  
        token = "" 

        for char in line:
            if char in delim_gen or char in other_symbols_key:
                if token: 
                    count = process_token(token, count, output_text, lexical_result, 
                                        mathematical_operators, assignment_operators, relational_operators, 
                                        logical_operators, data_type, other_symbols, reserved_words)
                    token = "" 
                
                count = process_token(char, count, output_text, lexical_result, 
                    mathematical_operators, assignment_operators, relational_operators, 
                    logical_operators, data_type, other_symbols, reserved_words)

            else:
                token += char  
        
        if token:  
            count = process_token(token, count, output_text, lexical_result, 
                                mathematical_operators, assignment_operators, relational_operators, 
                                logical_operators, data_type, other_symbols, reserved_words)

        for token in tokens:
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
            if is_string_literal(token):
                output_text.insert(tk.END, f"String Literal: {token}\n")
                output_text.insert(tk.END, "_ _ _ _ _ _ _ _ _ _ _ _ _ _\n")
            if is_identifier(token):
                output_text.insert(tk.END, f"Identifier: {token}\n")
                output_text.insert(tk.END, "_ _ _ _ _ _ _ _ _ _ _ _ _ _\n")
            if is_float_literal(token):
                output_text.insert(tk.END, f"Float: {token}\n")
                output_text.insert(tk.END, "_ _ _ _ _ _ _ _ _ _ _ _ _ _\n")
            if is_integer_literal(token):
                output_text.insert(tk.END, f"Integer: {token}\n")
                output_text.insert(tk.END, "_ _ _ _ _ _ _ _ _ _ _ _ _ _\n")

root = tk.Tk()
root.title("GenomeX")

frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

lexical_result = ttk.Treeview(frame, columns=('ID', 'Lexeme', 'Token'), show='headings', height=15)
lexical_result.heading('ID', text='ID')
lexical_result.heading('Lexeme', text='Lexeme')
lexical_result.heading('Token', text='Token')

lexical_result.column('ID', width=50, anchor='center')
lexical_result.column('Lexeme', width=150, anchor='center')
lexical_result.column('Token', width=150, anchor='center')

lexical_result.pack(side=tk.RIGHT, fill=tk.Y, padx=10, pady=10)

input_text = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=40, height=10)
input_text.pack(side=tk.TOP, padx=10, pady=10)

parse_button = tk.Button(frame, text="Run", command=parse_program)
parse_button.pack(side=tk.TOP, padx=10, pady=5)

output_text = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=40, height=15)
output_text.pack(side=tk.TOP, padx=10, pady=10)

root.mainloop()