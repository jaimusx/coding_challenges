"""
From: https://codingbat.com/prob/p143951

Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the values, it does not count towards the sum.

lone_sum(1, 2, 3) → 6
lone_sum(3, 2, 3) → 2
lone_sum(3, 3, 3) → 0

Solution:
"""

def lone_sum(a, b, c):
    if a == b == c:
        return 0
    if a != b and a != c and b != c:
        return a + b + c
    return sum(i for i in [x for x in [a, b, c] if [a, b, c].count(x) == 1])
