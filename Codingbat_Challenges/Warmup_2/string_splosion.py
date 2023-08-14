"""
From: https://codingbat.com/prob/p118366

Given a non-empty string like "Code" return a string like "CCoCodCode".

string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'

Solution:
"""

def string_splosion(str):
    return "".join([str[:i] for i, e in enumerate(str)]) + str  
