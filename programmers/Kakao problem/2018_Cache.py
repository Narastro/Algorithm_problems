# 2021.04.01. 2018 KAKAO Blind Recruitment
# Cache

from collections import deque
def solution(cacheSize, cities):
    time = 0
    # 1. Specify the queue size in advance
    cache = deque(maxlen=cacheSize)
    # 2. For each city, searching in cache
    for city in cities:
        city = city.lower()
        # 2-1. In cache
        if city in cache:
            cache.remove(city)
            cache.append(city)
            time += 1
        # 2-2. Not in cache
        else:
            cache.append(city)
            time += 5
    return time


print(solution(3,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", \
                  "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))