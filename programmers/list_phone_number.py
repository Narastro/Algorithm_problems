# 2021.04.18. 2021 Programmers High score kit
# List of phone number

from collections import defaultdict
def solution(phone_book):
    phone_book.sort(key=lambda x:len(x))
    discovered = defaultdict(int)
    for phone in phone_book:
        discovered[phone]+=1
        for i in range(1, len(phone)):
            if phone[:i] in discovered:
                return False
    return True
