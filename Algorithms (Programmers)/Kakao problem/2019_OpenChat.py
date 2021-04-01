# 2021.04.01. 2019 KAKAO Blind Recruitment
# Open Chat

from collections import defaultdict

def solution(records):
    # 1. Initialization
    answer = []
    ans_str = []
    users = defaultdict(str)
    # 2. Put the results value in ans_str list
    for record in records:
        command = record.split()[0]
        user_id = record.split()[1]
        if command == 'Leave':
            ans_str.append([user_id,'L'])
        else:
            nickname = record.split()[2]
            if command == 'Enter':
                users[user_id] = nickname
                ans_str.append([user_id,'E'])
            # 2-1. Nickname change using dictionary
            elif command == 'Change':
                users[user_id] = nickname
    # 3. Process the commands of 'E' or 'L'
    for s in ans_str:
        if s[1]=='E':
            answer.append(users[s[0]]+'님이 들어왔습니다.')
        elif s[1]=='L':
            answer.append(users[s[0]] + '님이 나갔습니다.')

    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))