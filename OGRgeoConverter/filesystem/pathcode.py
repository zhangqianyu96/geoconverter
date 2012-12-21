'''
Creates and handles pathcodes.
A pathcode is unique an can be translated into a file or folder path.
'''

import datetime
import string
import random
import re

def get_pathcode_regex():
    #         year   month   day   hour  minute  second  code    total: 24 characters
    return r'(\d{4})(\d{2})(\d{2})(\d{2})(\d{2})(\d{2})(\w{10})'

def get_bounded_pathcode_regex():
    return r'^' + get_pathcode_regex() + r'$'

def get_random_pathcode():
    return __get_date_string() + __get_random_code()

def __get_date_string():
    now = datetime.datetime.now()
    
    year = now.strftime('%Y')
    month = now.strftime('%m')
    day = now.strftime('%d')
    hour = now.strftime('%H')
    minute = now.strftime('%M')
    second = now.strftime('%S')
    
    return year + month + day + hour + minute + second

def __get_random_code():
    length = 10
    characters=string.ascii_lowercase + string.digits
    return ''.join(random.choice(characters) for i in range(length))

def is_pathcode(code):
    return re.match(get_bounded_pathcode_regex(), code) != None

def split_pathcode(path_code):
    '''
    Splits a pathcode and returns its components (year, month, ...) as list
    If the argument is not a valid pathcode an empty list is returned.
    '''
    if is_pathcode(path_code):
        splitted_pathcode = re.split(get_bounded_pathcode_regex(), path_code)
        # First and last string in list is empty (see Python doc for re.split)
        return splitted_pathcode[1:len(splitted_pathcode)-1]
    else:
        return []

def join_pathcode(*args):
    '''
    Joins a list to a pathcode.
    If the joined string is not a valid pathcode an empty string is returned
    '''
    joined_pathcode = ''.join(args)

    if is_pathcode(joined_pathcode):
        return joined_pathcode
    else:
        return ''