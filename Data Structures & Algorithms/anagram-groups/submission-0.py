class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = dict()

        for s in strs:
            val = ''.join(sorted(s))
            if val not in anagrams:
                anagrams[val] = [s]
            else:
                anagrams[val].append(s)            
        return list(anagrams.values())