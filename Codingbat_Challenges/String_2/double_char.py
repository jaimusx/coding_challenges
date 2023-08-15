"""
From: https://codingbat.com/prob/p170842

Given a string, return a string where for every char in the original, there are two chars.

double_char('The') → 'TThhee'
double_char('AAbb') → 'AAAAbbbb'
double_char('Hi-There') → 'HHii--TThheerree'

Solution:
"""

def double_char(str):
    return "".join([i + i for i in str])
