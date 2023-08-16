"""
Write a function named format_number that takes a non-negative number as its only parameter.

Your function should convert the number to a string and add commas as a thousands separator.

For example, calling format_number(1000000) should return "1,000,000".

Solution:
"""
def format_number(num):
  result = ""
  for i, e in enumerate(str(num)[::-1]):
      if i != 0 and (i % 3) == 0:
          result += ","
      result += e
  return result[::-1]


# Using built-in format()
def format_number(num):
    return "{:,}".format(num)
