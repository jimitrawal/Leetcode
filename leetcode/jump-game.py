class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maximum = 0
        for i in range(len(nums)):
            if i <= maximum:
                if maximum <= nums[i]+i:
                    maximum = nums[i]+i
            else:
                return False
        return True