class Solution:
    def maxArea(self, heights: List[int]) -> int:
        main_area = 0 
        for h1 in range(len(heights)):
            for h2 in range(h1+ 1, len(heights)):
                main_area = max(main_area, min(heights[h1], heights[h2]) * (h2-h1))
        return main_area