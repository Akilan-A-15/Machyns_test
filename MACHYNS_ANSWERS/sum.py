# 5)	Find sum of numbers in the given string. String: ‘1s2d3k45’

import re

string = '1s2d3k45'
numbers = re.findall(r'\d+', string)
numbers = [int(num) for num in numbers]
sum_numbers = sum(numbers)
print(f"The sum of the numbers in the string '{string}' is {sum_numbers}")
