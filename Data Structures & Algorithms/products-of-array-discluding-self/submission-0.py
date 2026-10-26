class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lst = [1] * (len(nums))
        post = 1
        for i in range(1, len(nums)):
            lst[i] = lst[i-1] * nums[i-1]
        for i in range(len(nums) - 1, -1, -1):
            lst[i] *= post
            post *= nums[i]
        return lst