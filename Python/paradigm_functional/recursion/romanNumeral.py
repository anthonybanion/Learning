# Description: This module provides functions to convert Roman numerals to Integer using recursion.
# File: romanNumeral.py
# Create Date: 11/04/2025

def roman_to_int(s):
  """
  Convert a Roman numeral to an integer using recursion.
  
  :param s: A string representing the Roman numeral
  :return: An integer representation of the Roman numeral
  """
  roman_values = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50,
    'C': 100, 'D': 500, 'M': 1000
  }
  
  if not s:
    return 0
  
  # If the current Roman numeral is smaller than the next one,
  # it means we need to subtract its value (e.g., IV = 4, IX = 9).
  if len(s) > 1 and roman_values[s[0]] < roman_values[s[1]]:
    return roman_to_int(s[1:]) - roman_values[s[0]]
  else:
    # Otherwise, add the value of the current Roman numeral.
    return roman_values[s[0]] + roman_to_int(s[1:])

# Example usage
if __name__ == "__main__":
  roman_numeral = "MCMXCIV"  # Example Roman numeral
  integer_value = roman_to_int(roman_numeral)
  print(f"The integer value of the Roman numeral {roman_numeral} is {integer_value}.")
# Output: The integer value of the Roman numeral MCMXCIV is 1994.
