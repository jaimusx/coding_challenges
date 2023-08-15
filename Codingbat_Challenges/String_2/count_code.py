"""
From: https://codingbat.com/prob/p186048

Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.

count_code('aaacodebbb') → 1
count_code('codexxcode') → 2
count_code('cozexxcope') → 2

Solution:
"""

def count_code(str):
    counts = 0
    for i in "abcdefghijklmnopqrstuvwxyz":
        if str.count("co" + i + "e") >= 1:
          counts += str.count("co" + i + "e")
    return counts

# One-liner
def count_code(str):
    return sum([str.count("co" + i + "e") for i in "abcdefghijklmnopqrstuvwxyz" if str.count("co" + i + "e") >= 1])
