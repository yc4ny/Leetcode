class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        steps = []
        bool = True 
        val = 1
        
        while(bool):
            temp = val
            for i in range(len(nums)):
                steps.append(temp + nums[i])
                temp = temp + nums[i]
        
            if all(i >= 1 for i in steps):
                bool = False
                    
            else:
                val += 1
                steps = []
        
        return val