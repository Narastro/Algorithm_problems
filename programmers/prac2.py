import heapq

def solution(array):
    answer = [0]*len(array)
    heap = []
    pre_i =[]
    for i,v in enumerate(array):
        heapq.heappush(heap,(-v,i))
    v_m, index = heapq.heappop(heap)
    answer[index] = -1
    pre_val = v_m
    pre_i.append(index)
    dup = 0
    while heap:
        v_m, index = heapq.heappop(heap)
        if v_m == pre_val:
            dup += 1
            if len(pre_i)>1:
                answer[index] = \
                    sorted(pre_i[:-dup],key=lambda x: (abs(x-index), x), reverse=True)[-1]
                pre_i.append(index)
            else:
                answer[index] = -1
                pre_i.append(index)
        else:
            dup = 0
            pre_i.sort(key=lambda x: (abs(x-index),x),reverse=True)
            answer[index] = pre_i[-1]
            pre_i.append(index)
            pre_val = v_m

    return answer


print(solution(	[7, 4, 4,4, 6, 9,9,6]))
