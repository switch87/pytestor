# Copyright (C) 2015  Gert Pellin
import re


def bracket_compare(string):
    """
    compare if there are the same amount of opening and closing brackets in the line of code
    :return:
    """
    count_open, count_close = find_brackets_inside_quotes(string)
    count_open = - count_open + len(re.findall(r'\(|\[|\{', string))
    count_close = - count_close + len(re.findall(r'\)|\[|\{', string))
    if count_close == count_open:
        return True
    else:
        return False


def find_brackets_inside_quotes(string):
    """
    count brackets inside quoted strings
    :param string:
    :return:
    """
    quotes = re.match(r'^.*(\".*\"|\'.*\')', string)
    if quotes is not None:
        o, c = find_brackets_inside_quotes(string[quotes.endpos + 1:])
        substring = quotes.string
        return len(re.findall(r'\(|\[|\{', substring)) + o, len(re.findall(r'\)|\]|\}', substring)) + c
    return 0, 0


