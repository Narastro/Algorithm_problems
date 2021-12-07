# 2021.02.05. Baekjoon algorithm problem #9020
# Goldbach's conjecture


# Sieve of Eratosthenes
def isPrime(a:int):
  if(a<2):
    return False
  for i in range(2,a):
    if(a%i==0):
      return False
  return True

T=int(input())      # T is test case
for i in range(T):
    N = int(input())
    if isPrime(int(N/2)):        # if half of number is prime number, print that
        print("{} {}".format(int(N/2),int(N/2)))
    else:
        for j in range(1,int(N/2)):         # if else, find prime number by adding or decreasing 1
            if isPrime(int(N/2-j)) and isPrime(int(N/2+j)):
                print("{} {}".format(int(N / 2-j), int(N / 2+j)))
                break
