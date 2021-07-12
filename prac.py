from collections import defaultdict
def solution(S,C):
    answer = []
    name_list = S.split(',')
    name_dic = defaultdict(int)
    for name in name_list:
        first_name = name.split()[0]
        last_name = name.split()[-1]
        index = ''
        if first_name+last_name in name_dic:
            name_dic[first_name+last_name] += 1
            index = str(name_dic[first_name+last_name])
        else:
            name_dic[first_name+last_name] = 1

        address = ' <'+first_name.lower()+'.'+last_name.replace('-','').lower()+index+'@'+C.lower()+'.com>'
        answer.append(name+address)
    return ','.join(answer)

print(solution('John Doe', 'Example'))

        
# def solution(S):
#     file_list = S.split('\n')
#     answer = 0
#     for file in file_list:
#         size = int(file.split()[0])
#         # date = int(file.split()[1])
#         month = file.split()[2]
#         year = int(file.split()[3])
#         # name = file.split()[-1]

#         if size < 240*(2**10):
#             continue
#         if year < 1990:
#             continue
#         if year == 1990 and month=='Jan':
#             continue

#         answer += 1
#     if answer == 0:
#         return 'NO FILES'
    
#     return str(answer)

    

# print(solution(' 779091968 23 Sep 2009 system.zip\n 284164096 14 Aug 2013 to-do-list.xml\n 714080256 19 Jun 2013 blockbuster.mpeg\n       329 12 Dec 2010 notes.html\n 444596224 17 Jan 1950 delete-this.zip\n       641 24 May 1987 setup.png\n    245760 16 Jul 2005 archive.zip\n 839909376 31 Jan 1990 library.dll'))
    




# def find_index_of_part(S,n):
#     cnt = 0
#     index_range = []

#     for i,v in enumerate(S):
#         if v=='a':
#             cnt += 1
#             if cnt == n:
#                 index_range.append(i)
#             elif cnt > n:
#                 index_range.append(i-1)
#                 break

#     return index_range
        

# def solution(S):
#     answer = 0
#     N = len(S)
#     reverse_S = S[::-1]
#     a_num = S.count('a')

#     if a_num % 3 != 0:
#         return 0
#     if a_num == 0:
#         return (N-1)*(N-2)//2
    
#     each_num = a_num // 3
#     first_part_index = find_index_of_part(S,each_num)
#     last_part_index = find_index_of_part(reverse_S,each_num)

#     answer = (first_part_index[1]-first_part_index[0]+1)*(last_part_index[1]-last_part_index[0]+1)

#     return answer

# print(solution("baaab"))



