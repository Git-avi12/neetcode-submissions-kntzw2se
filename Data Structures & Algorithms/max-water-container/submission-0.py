class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_hei=0
        for i in range(len(heights)):
            for j in range(len(heights)):
                if i!=j:
                    water = min(heights[i],heights[j])
                    max_hei = max(max_hei,water*abs(i-j))
        return max_hei
