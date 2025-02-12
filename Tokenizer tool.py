import tkinter as tk
from tkinter import ttk

# Define lists of keywords, operators, special characters, and separators
header = ['#include<stdio.h>', '#include<conio.h>']
keywords = ['auto', 'break', 'case', 'char', 'const', 'continue', 'default', 'do', 'double', 'else', 'enum', 'extern',
            'float', 'for', 'goto', 'if', 'int', 'long', 'register', 'return', 'short', 'signed', 'sizeof', 'static',
            'struct', 'switch', 'typedef', 'union', 'unsigned', 'void', 'volatile', 'while', 'include']
operators = ['+', '-', '*', '/', '%', '++', '--', '==', '!=', '>', '<', '>=', '<=', '&&', '||', '!', '&', '|', '^', '~',
             '<<', '>>', '=', '+=', '-=', '*=']
special_chars = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '=', '{', '}', '[', ']', ':', ';',
                 '<', '>', ',', '?', '/', '\\']
separators = [' ', ';', '\t', '\n']

functions = ['main', 'printf', 'scanf']


# Define a function to tokenize the input program
def tokenize_program():
    # Get the program text from the input box
    program_text = input_box.get('1.0', 'end-1c')

    # Spliting the program text into tokens
    tokens = []
    current_token = ''
    for char in program_text:
        if char in special_chars or char in operators or char in separators or char in header:
            if current_token:
                tokens.append(current_token)
            if char not in separators:
                tokens.append(char)
            current_token = ''
        else:
            current_token += char

    # Add the last token if there is one
    if current_token:
        tokens.append(current_token)

    # Identifying the type of each token
    token_types = []
    for token in tokens:
        if token in keywords:
            token_types.append('Keyword')
        elif token in operators:
            token_types.append('Operator')
        elif token in special_chars:
            token_types.append('Special Character')
        elif token.isdigit():
            token_types.append('Numeric Literal')
        elif token in functions:
            token_types.append('Functions')
        elif token in header:
            token_types.append('Header')
        else:
            token_types.append('Identifier')

    # Clear the table
    for row in table.get_children():
        table.delete(row)

    # Populate the table with the tokens and their types
    for i in range(len(tokens)):
        table.insert('', 'end', values=([i+1], tokens[i], token_types[i]))

def analyze_symbol():
    program_text = input_box.get('1.0', 'end-1c')
    tokens = []
    current_token = ''


def reset():
    input_box.delete('1.0', 'end')
    for row in table.get_children():
        table.delete(row)


# Create the GUI
root = tk.Tk()
root.title('Tokenization Tool')

# Create the input box for the program text
input_box = tk.Text(root, height=10, width=50)
input_box.grid(row=0, column=0, padx=10, pady=10)

# Create the button to tokenize the program
tokenize_button = tk.Button(root, text='Tokenize', command=tokenize_program)
tokenize_button.grid(row=1, column=0, padx=10, pady=10)

# Create the table to display the tokens and their types
table = ttk.Treeview(root, columns=('Serial', 'Token', 'Data Type'))
table.heading('Serial', text='Serial')
table.heading('Token', text='Token')
table.heading('Data Type', text='Data Type')
table.grid(row=0, column=1, rowspan=3, padx=10, pady=10)


# Create the button to symbolize the program
symbolize_button = tk.Button(root, text='Symbolize', command=analyze_symbol)
symbolize_button.grid(row=5, column=0, padx=10, pady=10)

# Create the symbol table
table_symbol = ttk.Treeview(root, columns=('Symbol', 'Data Type'))
table_symbol.heading('Symbol', text='Symbol')
table_symbol.heading('Data Type', text='Data Type')
table_symbol.grid(row=5, column=1, rowspan=3, padx=10, pady=10)


# Create the button to reset the program
delete_button = tk.Button(root, text='Reset', command=reset)
delete_button.grid(row=7, column=0, padx=10, pady=10)


root.mainloop()