## 1번
# 
 def find_num(num):
    f = 0
    for i in range(1,num+1):
        if num%i == 0:
            f += 1
    return f%2==0

def solution(left, right):
    numbers = [i for i in range(left,right+1)]
    answer = 0
    for num in numbers:
        if find_num(num):
            answer += num
        else:
            answer -= num
    return answer

##################################



## 2번
def fff(num):
    num_bit = format(num,'b')[::-1]
    for i in range(len(num_bit)):
        if i==len(num_bit)-1:
            break
        elif num_bit[i:i+2] == '01':
            return num + 2**i
        elif num_bit[i:i+2]=='00':
            return num + 2**i
        elif num_bit[i:i+2] == '10':
            return num + 2**i
    
    answer = 1
    for j in range(len(num_bit)-1):
        answer += 2**j

    return num + answer


def solution(numbers):
    answer = []
    for num in numbers:
        answer.append(fff(num))
        # k = num +1
        # while ff(num,k):
        #     k += 1
        # answer.append(k)

    return answer


print(solution([2,7]))

#######################333

##3번

