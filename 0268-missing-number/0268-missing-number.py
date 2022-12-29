class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 100:
            values = [0] * (n+1)
            exist = values

            for i in range(n+1):
                values[i] = i

            for i in range(n+1):
                for j in range(n):
                    if values[i] == nums[j]:
                        exist[i] = -1

            for i in range(n+1):
                if exist[i] != -1:
                    return exist[i] 
        else:   
            nums.sort()
            for i in range (len(nums)):
                if nums[i] != nums[i+1] -1:
                    return nums[i] + 1