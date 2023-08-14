"""
From: https://codingbat.com/prob/p113152

Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".

string_bits('Hello') → 'Hlo'
string_bits('Hi') → 'H'
string_bits('Heeololeo') → 'Hello'

Solution:
"""

def string_bits(str):
    return "".join([e for i, e in enumerate(str) if i % 2 == 0])
