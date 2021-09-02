import sys
DIGIT_MAP = ...


def convert(s):
  try:
    number = ''

    for token in s:
      number += DIGIT_MAP[token]
    x = int(number)

    print(f"conversion succeeded !! x = {x}")
 
  except KeyError:
    print("conversion failed!!")
    x = -1
    return x  
# except TypeError:
# print("conversion failed!!")
# x = -1  

print(convert("Three four".split()))  