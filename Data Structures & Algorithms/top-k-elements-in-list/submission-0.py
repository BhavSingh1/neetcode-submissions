class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = {}

        for num in nums:
            if num not in num_dict:
                num_dict[num] = 1
            else:
                num_dict[num] += 1
        
        sort_nums = sorted(num_dict, key = num_dict.get, reverse = True)

        return sort_nums[:k]
