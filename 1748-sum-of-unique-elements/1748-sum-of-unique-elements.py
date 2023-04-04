class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        sum = 0 
        for i in range(len(nums)):
            if nums[i] in nums[i+1:] or nums[i] in nums[:i]:
                continue
            else:
                sum += nums[i]
        return sum 