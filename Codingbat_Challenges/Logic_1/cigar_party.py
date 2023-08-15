"""
From: https://codingbat.com/python/Logic-1

When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper bound on the number of cigars. Return True if the party with the given values is successful, or False otherwise.

cigar_party(30, False) → False
cigar_party(50, False) → True
cigar_party(70, True) → True

Solution:
"""

def cigar_party(cigars, is_weekend):
    return (cigars in range(40, 61) and not is_weekend) or (cigars >= 40 and is_weekend)
