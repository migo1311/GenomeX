import tkinter as tk
from tkinter import ttk, scrolledtext
import string

# Lexer Definitions (adjusted for GenomeX specifications)
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

ALLOWED_CHARS = string.ascii_letters + string.digits + '_'


def classify_token(token):
    # Reserved words
    if token in RESERVED_WORDS:
        return f'ReservedWord({token})'
    # Check if valid identifier
    elif token[0].isupper() and all(c in ALLOWED_CHARS for c in token) and len(token) <= 20:
        return 'Identifier'
    # Check if integer literal
    elif token.isdigit() or (token.startswith('^') and token[1:].isdigit()):
        return 'IntegerLiteral'
    # Check if float literal
    elif '.' in token and token.replace('.', '', 1).isdigit():
        return 'FloatLiteral'
    # Check if string literal
    elif token.startswith('"') and token.endswith('"'):
        return 'StringLiteral'
    # Symbols
    elif token in SYMBOLS:
        return SYMBOLS[token]
    # Unknown
    else:
        return 'Unknown'


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


# GUI Code
def parse_code():
    input_code = input_text.get("1.0", tk.END).strip()
    output_text.delete('1.0', tk.END)
    tokens = tokenize_code(input_code)

    lexical_result.delete(*lexical_result.get_children())
    for idx, (lexeme, token) in enumerate(tokens, start=1):
        lexical_result.insert("", "end", values=(idx, lexeme, token))
        if token == 'Unknown':
            output_text.insert(tk.END, f"Error: Unrecognized token '{lexeme}'\n")


# Create the GUI
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
