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


def is_float_literal(token):
    if "." in token:
        try:
            float_value = float(token)
            
            # Split token by the decimal point to count decimal places
            whole_part, decimal_part = token.split('.')
            
            # Check conditions: number range, total length, and decimal places
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

end_statement = {
    ';': 'End Statement',  
    }
end_statement_key = end_statement.keys()

def parse_program():
    output_text.delete(1.0, tk.END)  # Clear the output area
    program = input_text.get(1.0, tk.END).strip().splitlines() 
    
    for item in lexical_result.get_children():
        lexical_result.delete(item)
    
    count = 1  

    for line in program:
        output_text.insert(tk.END, f"Line# {count}\n{line}\n")
        tokens = []  
        token = "" 

        for char in line:
            #Space Delim
            if char == ' ':

                if token:

                    if token in mathematical_operators_key:
                        output_text.insert(tk.END, f"Data Type: {mathematical_operators[token]}\n")
                        tokens.append(token)
                        output_text.insert(tk.END, f"Token: {token}\n")
                        lexical_result.insert('', 'end', values=(count, token, mathematical_operators[token]))
                        count += 1  

                    if token in assignment_operators_key:
                        output_text.insert(tk.END, f"Operator: {assignment_operators[token]}\n")
                        tokens.append(token)
                        output_text.insert(tk.END, f"Token: {token}\n")
                        lexical_result.insert('', 'end', values=(count, token, assignment_operators[token]))
                        count += 1  

                    if token in relational_operators_key:
                        output_text.insert(tk.END, f"Operator: {relational_operators[token]}\n")
                        tokens.append(token)
                        output_text.insert(tk.END, f"Token: {token}\n")
                        lexical_result.insert('', 'end', values=(count, token, relational_operators[token]))
                        count += 1  

                    if token in logical_operators_key:
                        output_text.insert(tk.END, f"Operator: {logical_operators[token]}\n")
                        tokens.append(token)
                        output_text.insert(tk.END, f"Token: {token}\n")
                        lexical_result.insert('', 'end', values=(count, token, logical_operators[token]))
                        count += 1  

                    if token in data_type_key:
                        output_text.insert(tk.END, f"Data Type: {data_type[token]}\n")
                        tokens.append(token)
                        output_text.insert(tk.END, f"Token: {token}\n")
                        lexical_result.insert('', 'end', values=(count, token, data_type[token]))
                        count += 1  

                    if token in other_symbols_key:
                        output_text.insert(tk.END, f"Data Type: {other_symbols[token]}\n")
                        tokens.append(token)
                        output_text.insert(tk.END, f"Token: {token}\n")
                        lexical_result.insert('', 'end', values=(count, token, other_symbols[token]))
                        count += 1  

                    if token in reserved_words_key:
                        output_text.insert(tk.END, f"Data Type: {reserved_words[token]}\n")
                        tokens.append(token)
                        output_text.insert(tk.END, f"Token: {token}\n")
                        lexical_result.insert('', 'end', values=(count, token, reserved_words[token]))
                        count += 1  

                    if is_string_literal(token):
                        output_text.insert(tk.END, f"Identifier: {token}\n")
                        tokens.append(token)
                        output_text.insert(tk.END, f"Token: {token}\n")
                        lexical_result.insert('', 'end', values=(count, token, "String Literal"))
                        count += 1  

                    if is_identifier(token):
                        output_text.insert(tk.END, f"Identifier: {token}\n")
                        tokens.append(token)
                        output_text.insert(tk.END, f"Token: {token}\n")
                        lexical_result.insert('', 'end', values=(count, token, "Identifier"))
                        count += 1  

                    if is_float_literal(token):
                        output_text.insert(tk.END, f"Float: {token}\n")
                        tokens.append(token)
                        output_text.insert(tk.END, f"Token: {token}\n")
                        lexical_result.insert('', 'end', values=(count, token, "Float Literal"))
                        count += 1  

                    if is_integer_literal(token):
                        output_text.insert(tk.END, f"Integer: {token}\n")
                        tokens.append(token)
                        output_text.insert(tk.END, f"Token: {token}\n")
                        lexical_result.insert('', 'end', values=(count, token, "Integer Literal"))
                        count += 1  


                token = ""  
                
            else:
                token += char

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

# Lexical Table
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

# Create the table (Treeview) on the left side
lexical_result = ttk.Treeview(frame, columns=('ID', 'Lexeme', 'Token'), show='headings', height=15)
lexical_result.heading('ID', text='ID')
lexical_result.heading('Lexeme', text='Lexeme')
lexical_result.heading('Token', text='Token')

# Set column widths
lexical_result.column('ID', width=50, anchor='center')
lexical_result.column('Lexeme', width=150, anchor='center')
lexical_result.column('Token', width=150, anchor='center')

# Pack the Treeview (table) on the left side
lexical_result.pack(side=tk.RIGHT, fill=tk.Y, padx=10, pady=10)

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
