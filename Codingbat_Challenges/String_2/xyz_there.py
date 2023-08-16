"""
From: https://codingbat.com/prob/p149391

Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.

xyz_there('abcxyz') → True
xyz_there('abc.xyz') → False
xyz_there('xyz.abc') → True

Solution:
"""

def xyz_there(str):
    return "xyz" in str.replace(".xyz", "")
