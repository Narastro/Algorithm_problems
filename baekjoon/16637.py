# 2021.12.29. Baekjoon algorithm problem #16637
# 괄호 추가하기

import re

N = int(input())
s = input()

num_regex = re.compile('\d')
exp_regex = re.compile('[^0-9]')
numbers = num_regex.findall(s)
exp = exp_regex.findall(s)
