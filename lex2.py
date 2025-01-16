import tkinter as tk
from tkinter import ttk, scrolledtext

# Explicitly Defined Delimiters
delim_add = ['"', ' ', '^', '(', '1', '2', '3', '4', '5', '6', '7', '8', '9',
             'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
             'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

delim_arith = ['+', '-', '*', '/', '%', '(', ' ', '^', '1', '2', '3', '4',
               '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
               'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
               'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

delim_equal = ['=', ' ', '{', '0', '1', '2', '3', '4', '5', '6', '7', '8', 
               '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 
               'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 
               'X', 'Y', 'Z', '"']

delim_neg = ['^', ' ', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
             'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 
             'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
             'Y', 'Z', '(']

delim_logic = ['&&', '||', '!', ' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 
               'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 
               'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '^', '(']

delim_comp = ['==', '>', '<', '>=', '<=', '!=', ' ', 'A', 'B', 'C', 'D', 
              'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 
              'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', 
              '2', '3', '4', '5', '6', '7', '8', '9', '^', '(']

delim_id = [' ', '=', '<', '>', ';', '_', '!', '+', '[', '(', '&', '|', '-', '*', ',']

# Reserved Words and Symbols
RESERVED_WORDS = {
    'act', 'gene', 'dose', 'quant', 'seq', 'allele', 'express',
    'stimuli', 'if', 'else', 'elif', 'while', 'do', 'for', 'destroy',
    'contig', 'prod', 'dom', 'rec', 'clust', 'perms', '_G', '_L', 'void'
}

SYMBOLS = {
    '+': 'Addition', '-': 'Subtraction', '*': 'Multiplication',
    '/': 'Division', '%': 'Modulo', '(': 'OpenParen', ')': 'CloseParen',
    '{': 'OpenBrace', '}': 'CloseBrace', '[': 'OpenBracket',
    ']': 'CloseBracket', ';': 'Semicolon', '=': 'Assignment',
    '^': 'Negate', '&&': 'AND', '||': 'OR', '!': 'NOT',
}

# Token Classification
def classify_token(token):
    # Reserved words
    if token in RESERVED_WORDS:
        return f'ReservedWord({token})'
    # Arithmetic symbols
    elif token in delim_arith:
        return 'ArithmeticOperator'
    # Logical operators
    elif token in delim_logic:
        return 'LogicalOperator'
    # Relational symbols
    elif token in delim_comp:
        return 'ComparisonOperator'
    # Identifiers
    elif token[0].isupper() and all(c.isalnum() or c == '_' for c in token):
        return 'Identifier'
    # Integer literals
    elif token.isdigit():
        return 'IntegerLiteral'
    # String literals
    elif token.startswith('"') and token.endswith('"'):
        return 'StringLiteral'
    else:
        return 'Unknown'

# Tokenization Process
def tokenize_code(code):
    tokens = []
    current_token = ''
    for char in code:
        if char.isspace() or char in SYMBOLS:
            if current_token:
                tokens.append((current_token, classify_token(current_token)))
                current_token = ''
            if char in SYMBOLS:
                tokens.append((char, classify_token(char)))
        else:
            current_token += char
    if current_token:
        tokens.append((current_token, classify_token(current_token)))
    return tokens

# GUI Integration
def parse_code():
    input_code = input_text.get("1.0", tk.END).strip()
    output_text.delete('1.0', tk.END)
    tokens = tokenize_code(input_code)
    lexical_result.delete(*lexical_result.get_children())
    for idx, (lexeme, token) in enumerate(tokens, start=1):
        lexical_result.insert("", "end", values=(idx, lexeme, token))
        if token == 'Unknown':
            output_text.insert(tk.END, f"Error: Unrecognized token '{lexeme}'\n")

# GUI Setup
root = tk.Tk()
root.title("GenomeX Lexical Analyzer")

frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

input_text = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=60, height=10)
input_text.pack(side=tk.TOP, padx=10, pady=5)

lexical_result = ttk.Treeview(frame, columns=('ID', 'Lexeme', 'Token'), show='headings', height=15)
lexical_result.heading('ID', text='ID')
lexical_result.heading('Lexeme', text='Lexeme')
lexical_result.heading('Token', text='Token')

lexical_result.column('ID', width=50, anchor='center')
lexical_result.column('Lexeme', width=200, anchor='center')
lexical_result.column('Token', width=200, anchor='center')

lexical_result.pack(side=tk.RIGHT, fill=tk.Y, padx=10, pady=10)

parse_button = tk.Button(frame, text="Analyze", command=parse_code)
parse_button.pack(side=tk.LEFT, padx=10, pady=5)

output_text = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=60, height=10)
output_text.pack(side=tk.BOTTOM, padx=10, pady=5)

root.mainloop()
