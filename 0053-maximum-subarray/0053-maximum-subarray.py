class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = -999999
        end = 0 
        
        for i in range(len(nums)):
            end = end + nums[i]
            if end > maximum:
                maximum = end
                
            if end < 0:
                end = 0 
        
        return maximum