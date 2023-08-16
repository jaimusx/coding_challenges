"""
From: https://codingbat.com/prob/p167025

Return the sum of the numbers in the array, returning 0 for an empty array. 
Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.

sum13([1, 2, 2, 1]) → 6
sum13([1, 1]) → 2
sum13([1, 2, 2, 1, 13]) → 6

Solution:
"""

def sum13(nums):
    fl = []
    for i, e in enumerate(nums):
        if e == 13:
            continue
        if i != 0:
            if nums[i - 1] == 13:
                continue
        fl.append(e)
    return sum(i for i in fl)
