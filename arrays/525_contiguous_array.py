from collections import defaultdict
from typing import List


def findMaxLength(self, nums: List[int]) -> int:
        sum_index = defaultdict(int)
        sum_index[0] = -1
        prefix = 0
        ans = 0
        for i in range(len(nums)):
            curr = nums[i]
            if curr == 0:
                prefix -= 1
            else:
                prefix += 1
            if prefix in sum_index:
                ans = max(ans,i-sum_index[prefix])
            else:
                sum_index[prefix] = i
        return ans