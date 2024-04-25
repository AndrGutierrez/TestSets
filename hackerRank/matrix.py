#!/bin/python3

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

response = ""
for i in range(m):
    for item in matrix:
        response +=item[i]

regex = r"\w([$&+,:;=?@#|'<>.^*()%!-].*?)\w"
print(response)
search = re.findall(regex, response)
print(search)
for s in search:
    response = response.replace(s, " ")
print(response)
