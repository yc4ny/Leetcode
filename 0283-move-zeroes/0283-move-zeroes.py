class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a=0
        for i in range(len(nums)):
            if(nums[i]!=0):
                nums[a],nums[i]=nums[i],nums[a]
                a+=1
        return(nums)