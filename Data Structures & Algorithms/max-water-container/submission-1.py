class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_hei=0
        l=0
        r=len(heights)-1
        while l<r:
            water = min(heights[l],heights[r])
            max_hei = max(max_hei,water*(r-l))
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return max_hei

