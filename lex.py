import string
import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk

def is_identifier(token):
    error_messages = []  

    if token[0].isupper():
        if len(token) <= 20 and all(c in string.ascii_letters + string.digits + '_' for c in token[1:]):
            return True
    
    if token[0].islower():  
        error_messages.append(f"starts with lowercase letter")
    
    if token[0].isdigit():  
        error_messages.append(f"starts with a number")
    
    if token[0] == "_":  
        error_messages.append(f"starts with an underscore")

    if '-' in token:
        error_messages.append(f"contains a hyphen")

    if len(token) > 20:
        error_messages.append(f"exceeds the maximum length of 20 characters")

    if error_messages:
        output_text.insert(tk.END, f"Error: Identifier '{token}' " + " and ".join(error_messages) + ".\n")
        return False
    
    return False

def is_integer_literal(token):
    if ',' in token:
        output_text.insert(tk.END, f"Error: Integer '{token}' contains an invalid comma (',').\n")
        return False
    
    if token.count('^') > 1:
        output_text.insert(tk.END, f"Error: Integer '{token}' contains multiple carets ('^').\n")
        return False
    
    if ' ' in token:
        output_text.insert(tk.END, f"Error: Integer '{token}' contains an invalid space.\n")
        return False
    
    if token.startswith('-') and token[1:].isdigit():
        output_text.insert(tk.END, f"Error: Integer '{token}' incorrect negation.\n")
        return False
    
    if token.startswith('^') and token[1:].isdigit():
        return "Negative Integer"
    
    if token.isdigit():
        return "Positive Integer"
    
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
    'dose' : 'dose', 
    'quant': 'quant' , 
    'seq' : 'seq', 
    'allele' : 'allele' 
    }
data_type_key = data_type.keys()

other_symbols = { 
    ';' : 'Semi-colon', 
    #'_' : 'Identifier Separator' , 
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
    
    token = token.lstrip('0') or '0' 
    integer_result = is_integer_literal(token) 

    if integer_result == "Negative Integer":
        lexical_result.insert('', 'end', values=(count, token, "Negative Integer Literal"))
        return count + 1
    
    if integer_result == "Positive Integer":
        lexical_result.insert('', 'end', values=(count, token, "Integer Literal"))
        return count + 1
    
    if is_identifier(token):  
        lexical_result.insert('', 'end', values=(count, token, "Identifier"))
        return count + 1
    
    if token in mathematical_operators:
        lexical_result.insert('', 'end', values=(count, token, mathematical_operators[token]))
        return count + 1

    if token in assignment_operators:
        lexical_result.insert('', 'end', values=(count, token, assignment_operators[token]))
        return count + 1

    if token in relational_operators:
        lexical_result.insert('', 'end', values=(count, token, relational_operators[token]))
        return count + 1

    if token in logical_operators:
        lexical_result.insert('', 'end', values=(count, token, logical_operators[token]))
        return count + 1

    if token in data_type:
        lexical_result.insert('', 'end', values=(count, token, data_type[token]))
        return count + 1

    if token in other_symbols:
        display_token = "\\n" if token == "\n" else token
        lexical_result.insert('', 'end', values=(count, display_token, other_symbols[token]))
        return count + 1

    if token in reserved_words:
        lexical_result.insert('', 'end', values=(count, token, reserved_words[token]))
        return count + 1

    if is_string_literal(token):
        lexical_result.insert('', 'end', values=(count, token, "String Literal"))
        return count + 1

    if is_float_literal(token):
        lexical_result.insert('', 'end', values=(count, token, "Float Literal"))
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
            if is_identifier(token) == True:
                output_text.insert(tk.END, f"Identifier: {token}\n")
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
