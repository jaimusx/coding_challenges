"""
From: https://codingbat.com/prob/p190859

We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each). 
Return the number of small bars to use, assuming we always use big bars before small bars. Return -1 if it can't be done.

make_chocolate(4, 1, 9) → 4
make_chocolate(4, 1, 10) → -1
make_chocolate(4, 1, 7) → 2

Solution:
"""

def make_chocolate(small, big, goal):
    bigs = big if goal // 5 >= big else goal // 5
    diff = goal - (bigs * 5)
    return small - (small - diff) if small - diff >= 0 else -1
