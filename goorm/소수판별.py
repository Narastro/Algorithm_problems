# 2021.12.20. goorm.io
# 소수 판별

def find_prime_num(num):
    if num <= 1:
        return False

    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False

    return True


user_input = int(input())
print(find_prime_num(user_input))
