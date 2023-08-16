"""
From: https://codingbat.com/prob/p108886

Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.

sum67([1, 2, 2]) → 5
sum67([1, 2, 2, 6, 99, 99, 7]) → 5
sum67([1, 1, 6, 7, 2]) → 4

Solution:
"""

def sum67(nums):
    flag = False
    total = 0
    for i in nums:
        if flag and i != 7:
              continue
        if i == 6:
            flag = True
            continue
        if i == 7 and flag:
            flag = False
            continue
        total += i
    return total
