from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        two_sum = []
        index_value = {}
        for i in range(len(nums)):
            value = nums[i]
            sub_value = target - value
            if sub_value in index_value:
                return [i,index_value[sub_value]]