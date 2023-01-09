# COMP 202 Assignment 2 Part 3
# Author: HAO CHEN HE
# Student ID: 260917762

import doctest

INCOMPLETE = -1


def ostring_to_raisedpos(s):
    ''' (str) -> str
    Convert a braille letter represented by '##\n##\n##' o-string format
    to raised position format. Provided to students. Do not edit this function.

    Braille cell dot position numbers:
    1 .. 4
    2 .. 5
    3 .. 6
    7 .. 8 (optional)

    >>> ostring_to_raisedpos('..\\n..\\n..')
    ''
    >>> ostring_to_raisedpos('oo\\noo\\noo')
    '142536'
    >>> ostring_to_raisedpos('o.\\noo\\n..')
    '125'
    >>> ostring_to_raisedpos('o.\\noo\\n..\\n.o')
    '1258'
    '''
    res = ''
    inds = [1, 4, 2, 5, 3, 6, 7, 8]
    s = s.replace('\n', '')
    for i, c in enumerate(s):
        if c == 'o':
            res += str(inds[i])
    return res 


def raisedpos_to_binary(s):
    ''' (str) -> str
    Convert a string representing a braille character in raised-position
    representation  into the binary representation.
    TODO: For students to complete.

    >>> raisedpos_to_binary('')
    '00000000'
    >>> raisedpos_to_binary('142536')
    '11111100'
    >>> raisedpos_to_binary('14253678')
    '11111111'
    >>> raisedpos_to_binary('123')
    '11100000'
    >>> raisedpos_to_binary('125')
    '11001000'
    '''
    #variable with no value
    binary_string = ''
    #for loop iterating through each of the values in range (1, 9)   
    for i in range(1, 9):
        #converting numbers into binary 
        if str(i) in s:
            binary_string += "1"
        else:
            binary_string += "0"
            
    return binary_string

def binary_to_hex(s):
    '''(str) -> str
    Convert a Braille character represented by an 8-bit binary string
    to a string representing a hexadecimal number.

    TODO: For students to complete.

    The first braille letter has the hex value 2800. Every letter
    therafter comes after it.

    To get the hex number for a braille letter based on binary representation:
    1. reverse the string
    2. convert it from binary to hex
    3. add 2800 (in base 16)

    >>> binary_to_hex('00000000')
    '2800'
    >>> binary_to_hex('11111100')
    '283f'
    >>> binary_to_hex('11111111')
    '28ff'
    >>> binary_to_hex('11001000')
    '2813'
    '''
    #find length of s
    s_length = len(s)
    #reverse the string 
    reversed_binary= s[s_length: :-1]

    #convert my binary number into decimal 
    decimal = int(reversed_binary, 2)

    #convert into hex
    binary_to_hex = hex(decimal + int("2800", 16))
    #remove the 0x in front of the wanted output
    remove_0x = binary_to_hex[2: 6]
    
    return remove_0x

def hex_to_unicode(n):
    '''(str) -> str
    Convert a braille character represented by a hexadecimal number
    into the appropriate unicode character.
    Provided to students. Do not edit this function.

    >>> hex_to_unicode('2800')
    '⠀'
    >>> hex_to_unicode('2813')
    '⠓'
    >>> hex_to_unicode('2888')
    '⢈'
    '''
    # source: https://stackoverflow.com/questions/49958062/how-to-print-unicode-like-uvariable-in-python-2-7
    return chr(int(str(n),16))


def is_ostring(s):
    '''(str) -> bool
    Is s formatted like an o-string? It can be 6-dot or 8-dot.
    TODO: For students to complete.

    >>> is_ostring('o.\\noo\\n..')
    True
    >>> is_ostring('o.\\noo\\n..\\noo')
    True
    >>> is_ostring('o.\\n00\\n..\\noo')
    False
    >>> is_ostring('o.\\noo')
    False
    >>> is_ostring('o.o\\no\\n..')
    False
    >>> is_ostring('o.\\noo\\n..\\noo\\noo')
    False
    >>> is_ostring('\\n')
    False
    >>> is_ostring('A')
    False
    '''
    #for a character in s, return False if it does not have o, . or \n
    for char in s:
        if char != 'o' and char != '.' and char != '\n':
            return False   
            
    #if at index 2 to 3, there is no "\n", return false
    index = s.find('\n', 2, 3)
    if index == -1:
            return False 
        
    #create new_s without '\n'
    new_s=s.replace('\n' , '')
    
    
    #Return true if total_length of new_s (without '\n')is 6 or 8
    total_length = len(new_s)      
    if total_length==6 or total_length==8:
        return True
    else:
        return False

def ostring_to_unicode(s):
    '''
    (str) -> str
    If s is a Braille cell in o-string format, convert it to unicode.
    Else return s.

    Remember from page 4 of the pdf:
    o-string -> raisedpos -> binary -> hex -> Unicode

    TODO: For students to complete.

    >>> ostring_to_unicode('o.\\noo\\n..')
    '⠓'
    >>> ostring_to_unicode('o.\\no.\\no.\\noo')
    '⣇'
    >>> ostring_to_unicode('oo\\noo\\noo\\noo')
    '⣿'
    >>> ostring_to_unicode('oo\\noo\\noo')
    '⠿'
    >>> ostring_to_unicode('..\\n..\\n..')
    '⠀'
    >>> ostring_to_unicode('a')
    'a'
    >>> ostring_to_unicode('\\n')
    '\\n'
    '''
    ostring_to_unicode = hex_to_unicode(binary_to_hex(raisedpos_to_binary(ostring_to_raisedpos(s))))

    #return conversion of ostring into unicode if string is an ostring
    if is_ostring(s):
        return ostring_to_unicode
    #return string as is if not an ostring 
    else:
        return s

if __name__ == '__main__':
    doctest.testmod()
