"""
From: https://codingbat.com/prob/p165321

Given a non-negative number "num", return True if num is within 2 of a multiple of 10. Note: (a % b) is the remainder of dividing a by b, so (7 % 5) is 2. See also: Introduction to Mod

near_ten(12) → True
near_ten(17) → False
near_ten(19) → True

Solution:
"""

def near_ten(num):
    return (num % 10 in range(8, 10)) or (num % 10 in range(0, 3))

# Using string logic
def near_ten(num):
    return str(num)[-1] in "01289"
