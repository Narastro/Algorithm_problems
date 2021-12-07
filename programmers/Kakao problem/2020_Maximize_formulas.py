# 2021.04.15. 2020 KAKAO Internship
# Maximize formulas

from itertools import permutations

def solution(expression):
    answer = 0
    # 1. for each permutations
    for operators in permutations(['+','-','*'],3):
        # 2. Divide by last operator
        exp_list = expression.split(operators[2])

        for i in range(len(exp_list)):
            # 3. Divide by second operator
            exp_list[i] = exp_list[i].split(operators[1])
            # 4. if first operator is in there, Wrap it in parentheses.
            for j in range(len(exp_list[i])):
                if operators[0] in exp_list[i][j]:
                    exp_list[i][j] = '(' + exp_list[i][j] + ')'
            # 5. Wrap it in parentheses and attach the second operator.
            exp_list[i][0] = '(' + exp_list[i][0]
            exp_list[i][-1] = exp_list[i][-1] + ')'
            exp_list[i] = operators[1].join(exp_list[i])
        # 6. Attach the last operator.
        s = operators[2].join(exp_list)
        # 7. Maximum absolute value calculated by eval function
        answer  = max(abs(eval(s)),answer)
    return answer
