"""
From: https://codingbat.com/prob/p194053

Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside and the longer string on the inside. 
The strings will not be the same length, but they may be empty (length 0).

combo_string('Hello', 'hi') → 'hiHellohi'
combo_string('hi', 'Hello') → 'hiHellohi'
combo_string('aaa', 'b') → 'baaab'

Solution:
"""

def combo_string(a, b):
    return (a if len(a) < len(b) else b) + (a if len(a) > len(b) else b) + (a if len(a) < len(b) else b)
