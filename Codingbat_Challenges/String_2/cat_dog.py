"""
From: https://codingbat.com/prob/p164876

Return True if the string "cat" and "dog" appear the same number of times in the given string.

cat_dog('catdog') → True
cat_dog('catcat') → False
cat_dog('1cat1cadodog') → True

Solution:
"""

def cat_dog(str):
    return str.count("cat") == str.count("dog")
