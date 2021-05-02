from sympy.parsing.latex import parse_latex
from sympy.printing.preview import preview
from sympy import simplify
from os import remove

def str_to_raw(s):
    raw_map = {8:r'\b', 7:r'\a', 12:r'\f', 10:r'\n', 13:r'\r', 9:r'\t', 11:r'\v'}
    return r''.join(i if ord(i) > 32 else raw_map.get(ord(i), i) for i in s)

def get_latex(string):
    return parse_latex(str_to_raw(string))

'''
preview(expr1, viewer='file', filename='output.png')

if (input("delete? ") == "y"):
    remove("output.png")
'''

if __name__ == '__main__':
    string1 = "\frac{1}{10}+x"
    string2 = "\frac{1+10x}{10}"

    expr1 = parse_latex(str_to_raw(string1))
    expr2 = parse_latex(str_to_raw(string2))

    print(simplify(expr1 - expr2) == 0)