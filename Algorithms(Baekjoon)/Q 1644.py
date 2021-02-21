# 2021.02.21. Baekjoon algorithm problem #1644
# Sum of Consecutive Prime Numbers

prime_ox = [True for _ in range(4000001)]
# Sieve of Eratosthenes
for i in range(2, int(4000001 ** 0.5)):
    if prime_ox[i]:
        for j in range(i+i, 4000001, i):
            prime_ox[j] = False
prime_list = [i for i, j in enumerate(prime_ox) if j == True and i >=2 ]

prime_number = prime_list

sum_prime = [0] * (len(prime_number) + 1)
for i in range(len(prime_number)):
    sum_prime[i+1] = sum_prime[i] + prime_number[i]

N = int(input())

start = 0
end = 1
result = 0
if N==2:
    result = 1
while end >= start and prime_number[end-1] <= N:
    if end == start and sum_prime[end] == N:
        result += 1
        end += 1
    elif sum_prime[end] - sum_prime[start] < N:
        end +=1
    elif sum_prime[end] - sum_prime[start] > N:
        start +=1
    else:
        result +=1
        end +=1
print(result)