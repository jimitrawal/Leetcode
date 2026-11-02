class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        i=0
        j=0
        for x in nums:
            temp = max(i+x,j)
            i = j
            j = temp
        return j