# COMP 202 A2 Part 2
# Author: Hao Chen He
# Student ID: 260917762

from helpers import *

# More constants you'll want to use:
SPACE = '..\n..\n..'
HYPHEN = '..\n..\noo' 
APOSTROPHE = '..\n..\no.' 
QUOTES = '..\noo\noo'


############################ Functions

def convert_irregular(c):
    '''(str) -> str
    Convert the irregular characters to French Braille.
    Recall these are: space, hyphen, apostrophe, guillements
    Apostrophe could be represented by `, ’ or '.
    Hyphen could be represented by - or by –.
    Note the constants such as SPACE and HYPHEN above.

    >>> print(convert_irregular('-'))
    ..
    ..
    oo
    >>> convert_irregular('–')
    '..\\n..\\noo'
    >>> convert_irregular('`')
    '..\\n..\\no.'
    >>> convert_irregular("'")
    '..\\n..\\no.'
    >>> convert_irregular("’")
    '..\\n..\\no.'
    >>> convert_irregular("»")
    '..\\noo\\noo'
    '''
    #test if c is an irregular character
    if is_irregular(c):
        #test if c is a hyphen (2 types) then return hyphen in braille
        if c == "–" or c == "-":
            return HYPHEN
        #test if c is a space then return space in braille
        elif c == " ":
            return SPACE
        #test if c is an apostrophe (3 types) then return apostrophe in braille
        elif c == "'" or c == "’" or c == "`":
            return APOSTROPHE
        #if none of the above, then it's a quote and return quote in braille
        else: 
           return QUOTES
    
    return None


def decade_pattern(decade_position):
    '''(int) -> str
    Using position in Braille decade, get associated Braille pattern.
    Provided to students. Do not edit this function.

    >>> decade_pattern(0)
    'o.\\n..'
    >>> decade_pattern(9)
    '.o\\noo'
    '''
    DEC_SEQ = ['o.\n..', 'o.\no.', 'oo\n..', 'oo\n.o',
           'o.\n.o', 'oo\no.', 'oo\noo', 'o.\noo',
           '.o\no.', '.o\noo']
    return DEC_SEQ[decade_position]


def convert_digit(c):
    '''(str) -> str
    Convert string representation of digit
    to Braille. For this, put the decade value in the top two rows,
    and put '..' in the bottow row.
    Hints:
        - Remember: we provided the string DIGITS to you
        - For full credit, this should have fewer than 4 lines of code.

    >>> print(convert_digit('1'))
    o.
    ..
    ..
    >>> print(convert_digit('3'))
    oo
    ..
    ..
    >>> print(convert_digit('0'))
    .o
    oo
    ..
    '''
    #test if c is a digit
    if is_digit(c):
        #convert string representation of digit to Braille 
        return decade_pattern(int(c)-1) + "\n.." 
    return None
    

def convert_punctuation(c):
    '''(str) -> str
    Convert string representation of common punctuation
    to French Braille. For this put the decade value in the bottom
    two rows, and put '..' in the top row.
    Hints: 
        - Use the string PUNCTUATION we provided to you
        - Recall there are helper functions we gave you
        - For full credit, this should have fewer than 4 lines of code.
        - You should not have to manually enter any Braille strings

    >>> print(convert_punctuation(','))
    ..
    o.
    ..
    >>> print(convert_punctuation(';'))
    ..
    o.
    o.
    >>> print(convert_punctuation(':'))
    ..
    oo
    ..
    >>> print(convert_punctuation('"'))
    ..
    oo
    oo
    '''
    #test if c is in punctuation
    if is_punctuation(c):
        #convert punctuation into French braille
        for i, single_punctuation in enumerate(PUNCTUATION):
            if single_punctuation == c:
                return ("..\n" + decade_pattern(i)) 
    return None


############################# 


def decade_ending(dec_num):
    '''(int) -> str
    For one of the four decades of standard letters in French Braille,
    return the associated bottom-row (see page 3 of pdf.)

    >>> decade_ending(0)
    '..'
    >>> decade_ending(1)
    'o.'
    >>> decade_ending(2)
    'oo'
    >>> decade_ending(3)
    '.o'
    '''
    #if it's decade 0, return ..
    if dec_num == 0:
        return ("..")
    #if it's decade 1, return o.
    elif dec_num == 1:
        return ("o.")
    #if it's decade 2, return oo
    elif dec_num == 2:
        return ("oo")
    #if it's decade 3, return .o
    elif dec_num == 3:
        return (".o")
    #if it's anything other than 0,1,2 or 3, return none    
    else:
        return None


def letter_row(c):
    '''(str) -> int
    For a standard letter in French Braille, return
    the number of the decade it belongs to. (See table on page 3 of pdf.)
    Provided to students. Do not edit this function.

    >>> letter_row('a')
    0
    >>> letter_row('w')
    3
    >>> letter_row('n')
    1
    >>> letter_row('N')
    1
    '''
    c = c.lower() # convert
    for i, decade in enumerate(LETTERS):
        if c in decade:
            return i


def letter_column(c):
    '''(str) -> int
    For a standard letter in French Braille, return
    its position within its decade. (See table on page 3 of pdf.)
    Provided to students. Do not edit this function.

    >>> letter_column('a')
    0
    >>> letter_column('b')
    1
    >>> letter_column('v')
    1
    >>> letter_column('w')
    9
    >>> letter_column('W')
    9
    '''
    c = c.lower() # convert
    for decade in LETTERS:
        if c in decade:
            return decade.find(c)


def convert_letter(c):
    '''(str) -> str
    For one of the standard letters in French Braille,
    return its Braille representation.

    >>> print(convert_letter('a'))
    o.
    ..
    ..
    >>> print(convert_letter('b'))
    o.
    o.
    ..
    >>> print(convert_letter('p'))
    oo
    o.
    o.
    >>> print(convert_letter('ç'))
    oo
    o.
    oo
    >>> print(convert_letter('ô'))
    oo
    .o
    .o
    >>> print(convert_letter('A'))
    o.
    ..
    ..
    >>> print(convert_letter('Œ'))
    .o
    o.
    .o
    '''
    #test if it's a letter
    if is_letter(c):
        #define new variables
        #to get braille ending
        row_number = letter_row(c)
        braille_ending = decade_ending(row_number)
        #to get 1st two rows in braille 
        column_number = letter_column(c)
        braille_pattern = decade_pattern(column_number)
        
        #return braille after conversion
    return (braille_pattern + "\n" + braille_ending)


def char_to_braille(c):
    '''(str) -> str
    Convert a character, c, into French Braille.
    If c is a character we don't know how to convert, return 
    the same character as before.

    >>> print(char_to_braille('-'))
    ..
    ..
    oo
    >>> print(char_to_braille('w'))
    .o
    oo
    .o
    >>> print(char_to_braille('1'))
    o.
    ..
    ..
    >>> print(char_to_braille('?'))
    ..
    o.
    .o
    >>> char_to_braille('.')
    '..\\noo\\n.o'
    >>> char_to_braille('a')
    'o.\\n..\\n..'
    >>> char_to_braille('n')
    'oo\\n.o\\no.'
    >>> char_to_braille('Z')
    'o.\\n.o\\noo'
    >>> char_to_braille('Œ')
    '.o\\no.\\n.o'
    >>> char_to_braille(' ')
    '..\\n..\\n..'
    >>> char_to_braille('ß')
    'ß'
    >>> char_to_braille('\\n')
    '\\n'
    '''
    #test if c is one of the known characters
    if is_known_character(c):
        #test if it's a letter
        if is_letter(c):
            #convert into braille if it is a letter
            return convert_letter(c)
        #test if it's an irregular character
        if is_irregular(c):
            #convert into braille if it is an irregular character
            return convert_irregular(c)
        #test if it's a punctuation 
        if is_punctuation(c):
            #convert into braille if it is a punctuation
            return convert_punctuation(c)
        #test if it's a digit
        if is_digit(c):
            #convert into braille if it is a digit
            return convert_digit(c)
        
    #if it's not a known character, then return character as it is
    else:
        return c
        
    return char_to_braille(c)


if __name__ == '__main__':
    doctest.testmod()
