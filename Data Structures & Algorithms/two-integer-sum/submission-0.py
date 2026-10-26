class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_val = {}

        for i, elm in enumerate(nums):
            diff = target - elm
            if diff in prev_val:
                return[prev_val[diff], i]
            prev_val[elm] = i