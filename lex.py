import re
import tkinter as tk
from tkinter import scrolledtext

operators = {'=' : 'Assignment op','+' : 'Addition op','-' : 'Subtraction op','/' : 'Division op','*' : 'Multiplication op','<' : 'Lessthan op','>' : 'Greaterthan op' }
operators_key = operators.keys()

data_type = {'int' : 'integer type', 'float': 'Floating point' , 'char' : 'Character type', 'long' : 'long int' }
data_type_key = data_type.keys()

punctuation_symbol = { ':' : 'colon', ';' : 'semi-colon', '.' : 'dot' , ',' : 'comma' }
punctuation_symbol_key = punctuation_symbol.keys()

identifier = { 'a' : 'id', 'b' : 'id', 'c' : 'id' , 'd' : 'id' }
identifier_key = identifier.keys()

reserved_words = {
    'if': 'IF_STATEMENT',  
    'else': 'ELSE_STATEMENT', 
    'prod': 'RETURN_STATEMENT',  
    'act': 'DEFINE_STATEMENT',  
    'gene': 'MAIN_STATEMENT',  
    'dose': 'INTEGER_STATEMENT',  
    'quant': 'FLOAT_STATEMENT',  
    'seq': 'STRING_STATEMENT', 
    'allele': 'BOOLEAN_STATEMENT',   
    'express': 'PRINT_STATEMENT',   
    'stimuli': 'INPUT_STATEMENT',
}
reserved_words_key = reserved_words.keys()

integer_literals = {
    '0': 'INTEGER_LITERAL',
    '1': 'INTEGER_LITERAL',
    '2': 'INTEGER_LITERAL',
    '3': 'INTEGER_LITERAL',
    '4': 'INTEGER_LITERAL',
    '5': 'INTEGER_LITERAL',
    '6': 'INTEGER_LITERAL',
    '7': 'INTEGER_LITERAL',
    '8': 'INTEGER_LITERAL',
    '9': 'INTEGER_LITERAL',
}
integer_literals_key = integer_literals.keys()

dataFlag = False

def parse_program():
    count = 0
    output_text.delete(1.0, tk.END)  # Clear the output area
    program = input_text.get(1.0, tk.END).strip().splitlines()  # Get the user input from the Text widget

    for line in program:
        count += 1
        output_text.insert(tk.END, f"Line# {count}\n{line}\n")

        tokens = line.split(' ')
        output_text.insert(tk.END, f"Tokens are: {tokens}\n")
        output_text.insert(tk.END, f"Line# {count} properties:\n")

        for token in tokens:
            if token in operators_key:
                output_text.insert(tk.END, f"Operator: {operators[token]}\n")
            if token in data_type_key:
                output_text.insert(tk.END, f"Data Type: {data_type[token]}\n")
            if token in punctuation_symbol_key:
                output_text.insert(tk.END, f"Punctuation: {punctuation_symbol[token]}\n")
            if token in identifier_key:
                output_text.insert(tk.END, f"Identifier: {identifier[token]}\n")
            if token in reserved_words_key:
                output_text.insert(tk.END, f"Reserve Words: {reserved_words[token]}\n")
            if token in integer_literals_key:
                output_text.insert(tk.END, f"Integer Literal: {integer_literals[token]}\n")
        output_text.insert(tk.END, "_ _ _ _ _ _ _ _ _ _ _ _ _ _\n")

# Creating the tkinter UI
root = tk.Tk()
root.title("Lexical Analyzer")

# Create a Text widget for code input
input_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=10)
input_text.pack(pady=10)
input_text.insert(tk.END, "Type your code here...")  # Placeholder text

# Create a button to trigger the lexical analyzer
parse_button = tk.Button(root, text="Run", command=parse_program)
parse_button.pack(pady=5)

# Create a ScrolledText widget to display the results
output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=15)
output_text.pack(pady=10)

# Start the tkinter main loop
root.mainloop()