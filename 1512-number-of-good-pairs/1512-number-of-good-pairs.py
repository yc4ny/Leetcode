class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        answer = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i < j:
                    if nums[i] == nums[j]:
                        answer +=1 
                        
        return answer