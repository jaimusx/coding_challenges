"""
From: https://codingbat.com/prob/p179960

For this problem, we'll round an int value up to the next multiple of 10 if its rightmost digit is 5 or more, so 15 rounds up to 20. 
Alternately, round down to the previous multiple of 10 if its rightmost digit is less than 5, so 12 rounds down to 10. 
Given 3 ints, a b c, return the sum of their rounded values. To avoid code repetition, write a separate helper "def round10(num):" and call it 3 times. 
Write the helper entirely below and at the same indent level as round_sum().

round_sum(16, 17, 18) → 60
round_sum(12, 13, 14) → 30
round_sum(6, 4, 4) → 10

Solution:
"""

def round_sum(a, b, c):
    return round10(a) + round10(b) + round10(c)
    
def round10(num):
    return num + (10 - num % 10) if num % 10 in range(5, 10) else num - num % 10

# Using round() built in function
def round_sum(a, b, c):
    return round(a, -1) + round(b, -1) + round(c, -1)

# Using string logic
def round_sum(a, b, c):
    return (a + (10 - int(str(a)[-1])) if str(a)[-1] in "56789" else a - int(str(a)[-1])) + (b + (10 - int(str(b)[-1])) if str(b)[-1] in "56789" else b - int(str(b)[-1])) + (c + (10 - int(str(c)[-1])) if str(c)[-1] in "56789" else c - int(str(c)[-1]))
