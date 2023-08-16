"""
Write a function that takes a list of lists and flattens it into a one-dimensional list.

Name your function flatten. It should take a single parameter and return a list.

For example, calling:

flatten([[1, 2], [3, 4]])

Should return the list:

[1, 2, 3, 4]

Solution:
"""

def flatten(arr):
    return [item for sublist in [item for item in arr] for item in sublist]
