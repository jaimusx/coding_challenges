"""
From: https://codingbat.com/prob/p115413

Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".

hello_name('Bob') → 'Hello Bob!'
hello_name('Alice') → 'Hello Alice!'
hello_name('X') → 'Hello X!'

Solution:
"""

def hello_name(name):
    return "Hello " + name + "!"  # or -> return f"Hello {name}!"
