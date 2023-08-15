"""
From: https://codingbat.com/prob/p118406

We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big bricks (5 inches each). 
Return True if it is possible to make the goal by choosing from the given bricks. 
This is a little harder than it looks and can be done without any loops.

make_bricks(3, 1, 8) → True
make_bricks(3, 1, 9) → False
make_bricks(3, 2, 10) → True

Soultion:
"""

def make_bricks(small, big, goal):
    return  5 * big + small >= goal and small >= goal % 5

# Using a loop
def make_bricks(small, big, goal):
     t_small = small * 1
     t_big = big * 5
     final = goal

     while final > 0:
         if t_big == final:
             return True
         if final > 5 and t_big > 0:
             final -= 5
             t_big -= 5
         elif final >= 1 and t_small > 0:
             final -= 1
             t_small -= 1
         else:
             break
     return final == 0
