"""
From: https://codingbat.com/prob/p124676

Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.

near_hundred(93) → True
near_hundred(90) → True
near_hundred(89) → False

Solution:
"""

def near_hundred(n):
    return abs(100 - n) in range(0, 11) or abs(200 - n) in range(0, 11)
