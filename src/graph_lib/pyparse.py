""" Pyparse

This is modul for task parsing since most of the operations are same
"""

__author__ = 'Ales Lerch'

import os
import sys
import fileinput

def strip_param(param):
        return param.strip().replace('\n','')

def get_input_data(first_row_diffrent = True):
    """
    pokud je to prvni radek vloz jej do data_streamu jako pole jinak vkladej
    jako dalsi radky
    """
    data_stream = []
    for line in fileinput.input():
        if fileinput.isfirstline() and first_row_diffrent:
            data_stream.append([strip_param(line)])
        else:
            data_stream.append(strip_param(line))
    return data_stream


def parse_data_with_first_line(data, first_line_char, second_line_char,
        third_line_char):
    parse_data = []
    if first_line and data:
        (head, tail) = (data[0][0].split(first_line_char),data[1:])
        for element in tail:
            if third_line_char:
                (first,rest) = element.split(second_line_char)
                third = [strip_param(r) for r in rest.split(third_line_char)]
                parse_data.append((fist,third))
            else:
                row = [strip_param(ar) for ar in element.split()]
                parse_data.append(row)

        if third_line_char:
            return ((head,parse_data))
        else:
            return parse_data

def parse_data(data,first_char,second_char):
    parse_data = []
    for parse in data:
        (item, rest) = parse.split(first_char)
        item = [strip_param(it) for it in item.split(second_char)]
        parse_data.append(item)

    return parse_data

