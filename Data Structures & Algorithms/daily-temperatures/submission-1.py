class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp_lst = len(temperatures)
        result = []
        for i in range(temp_lst):
            count = 1
            j = i + 1

            while j < temp_lst:
                if temperatures[j] > temperatures[i]:
                    break
                j += 1
                count += 1
            count = 0 if j == temp_lst else count
            result.append(count)
        return result