DIGIT_MAP = ...  
def convert(s):
    if not isinstance(s, list):
       raise TypeError(
         "Arguement must be a list"
       )

    try: 
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        return int(number)
    except(KeyError, TypeError) as e:
      print(f"conversion error: {e!r},file=sys.stderr") 
               