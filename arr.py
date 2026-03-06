class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        f=nums[0]
        nums.pop(0)
        nums.sort()
        return f+nums[0]+nums[1]
