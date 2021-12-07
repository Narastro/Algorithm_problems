# 2021.03.02. Leetcode algorithm problem #347
# Top K Frequent Elements

import collections

def top_K_Frequent(nums,k):
    return list(zip(*collections.Counter(nums).most_common(k)))[0]