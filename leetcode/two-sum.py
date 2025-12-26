class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for i in range(len(nums)):
            if seen and target-nums[i] in seen:
                return [i,seen[target-nums[i]]]
            if not(nums[i] in seen):
                seen[nums[i]] = i