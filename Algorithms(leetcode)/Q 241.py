# 2021.05.24. Leetcode algorithm problem #241
# Different Ways to Add Parentheses


def solution(ss):
    def compute(left,right,op):
        results =[]
        for l in left:
            for r in right:
                results.append(eval(str(l)+op+str(r)))
        return results

    if ss.isdigit():
        return [int(ss)]

    results = []
    for index, value in enumerate(ss):
        if value in "-+*":
            left = solution(ss[:index])
            right = solution(ss[index+1:])
            results.extend(compute(left,right,value))
    return results


print(solution('2*3-4*5'))
