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
        output_text.insert(tk.END, f"Line# {count}\n{line}\n")
        tokens = []  # List to hold tokens
        token = ""  # Current token being constructed

        # Read each character in the line
        for char in line:
            if char in delimiters:
                # If a delimiter is found, add current token to tokens list
                if token:
                    tokens.append(token)
                    output_text.insert(tk.END, f"Token: {token}\n")
                    tree.insert('', 'end', values=(count, token, "SampleType"))

                tokens.append(char)
                output_text.insert(tk.END, f"Delimiter: {char}\n")
                tree.insert('', 'end', values=(count, char, delimiters[char]))

                token = ""  # Reset token
            elif char == ' ':
                # If space is found, finalize the token and start a new one
                if token:
                    tokens.append(token)
                    output_text.insert(tk.END, f"Token: {token}\n")
                    tree.insert('', 'end', values=(count, token, "SampleType"))
                token = ""  # Reset token for next word
            else:
                # Keep adding to the current token
                token += char

        # Handle the last token at the end of the line
        if token:
            tokens.append(token)
            output_text.insert(tk.END, f"Token: {token}\n")
            tree.insert('', 'end', values=(count, token, "SampleType"))

        for token in tokens:
            if token in mathematical_operators_key:
                output_text.insert(tk.END, f"Operator: {mathematical_operators[token]}\n")
            elif token in assignment_operators_key:
                output_text.insert(tk.END, f"Operator: {assignment_operators[token]}\n")
            elif token in relational_operators_key:
                output_text.insert(tk.END, f"Operator: {relational_operators[token]}\n")
            elif token in logical_operators_key:
                output_text.insert(tk.END, f"Operator: {logical_operators[token]}\n")
            elif token in data_type_key:
                output_text.insert(tk.END, f"Data Type: {data_type[token]}\n")
            elif token in other_symbols_key:
                output_text.insert(tk.END, f"Punctuation: {other_symbols[token]}\n")
            elif token in reserved_words_key:
                output_text.insert(tk.END, f"Reserve Words: {reserved_words[token]}\n")
            elif is_string_literal(token):
                    output_text.insert(tk.END, f"String Literal: {token}\n")
            elif is_identifier(token):
                    output_text.insert(tk.END, f"Identifier: {token}\n")
            elif is_integer_literal(token):
                    output_text.insert(tk.END, f"Integer Literal: {token}\n")
        output_text.insert(tk.END, "_ _ _ _ _ _ _ _ _ _ _ _ _ _\n")

    for value in token:
        result = is_integer_literal(token)
        output_text.insert(tk.END, f"Integer Literal: {value}: {result}\n")
    
    for value in token:
        result = is_float_literal(token)
        output_text.insert(tk.END, f"Float Literal: {value}: {result}\n")

# Create the main root window
root = tk.Tk()
root.title("Lexical Analyzer with Table")

# Create a frame to hold the table and the text widgets
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

# Create the table (Treeview) on the left side
tree = ttk.Treeview(frame, columns=('Line', 'Token', 'Type'), show='headings', height=15)
tree.heading('Line', text='Line#')
tree.heading('Token', text='Token')
tree.heading('Type', text='Type')

# Set column widths
tree.column('Line', width=50, anchor='center')
tree.column('Token', width=150, anchor='center')
tree.column('Type', width=150, anchor='center')

# Pack the Treeview (table) on the left side
tree.pack(side=tk.RIGHT, fill=tk.Y, padx=10, pady=10)

# Create a Text widget for code input on the right side
input_text = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=40, height=10)
input_text.pack(side=tk.TOP, padx=10, pady=10)

# Create a button to trigger the lexical analyzer
parse_button = tk.Button(frame, text="Run", command=parse_program)
parse_button.pack(side=tk.TOP, padx=10, pady=5)

# Create a ScrolledText widget to display the results on the right side
output_text = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=40, height=15)
output_text.pack(side=tk.TOP, padx=10, pady=10)

# Start the tkinter main loop
root.mainloop()