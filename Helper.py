# Import necessary sympy methods to parse latex and compare latex equations.
from sympy.parsing.latex import parse_latex
from sympy import simplify
# Import os.remove() function to remove a file that is no longer needed
from os import remove

# parse_inputs function to retrieve parameters from a string in a list.
def parse_inputs(string):

    params = []
    param = ''
    sentence = False
    for index in range(len(string)):
        if string[index] == '\"' or string[index] == '\'':
            if sentence:
                params.append(param)
                param = ''
            sentence = not sentence
        else:
            if sentence or (not sentence and string[index] != ' '):
                param = param + string[index]

        if not sentence and len(param) > 0 and string[index] == ' ':
            params.append(param)
            param = ''

        if not(param in params) and index + 1 == len(string):
            params.append(param)

    return params

# str_to_raw function to convert a provided string input to a raw_string, which maintains escape characters for LaTeX.
def str_to_raw(s):
    raw_map = {8:r'\b', 7:r'\a', 12:r'\f', 10:r'\n', 13:r'\r', 9:r'\t', 11:r'\v'}
    return r''.join(i if ord(i) > 32 else raw_map.get(ord(i), i) for i in s)

# get_latex function to convert the string to a raw string, and then parse it into LaTeX.
def get_latex(string):
    return parse_latex(str_to_raw(string))