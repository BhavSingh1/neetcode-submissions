class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        pracset = set()
        
        for elm in nums:
            if elm in pracset:
                return True
            pracset.add(elm)
        return False
         