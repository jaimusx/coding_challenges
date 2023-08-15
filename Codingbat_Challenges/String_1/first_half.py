"""
From: https://codingbat.com/prob/p107010

Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".

first_half('WooHoo') → 'Woo'
first_half('HelloThere') → 'Hello'
first_half('abcdef') → 'abc'

Solution:
"""

def first_half(str):
    return str[:len(str) / 2]
