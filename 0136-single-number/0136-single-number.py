class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic:
                dic[nums[i]] = dic[nums[i]],nums[i]
            else:
                dic[nums[i]] = [nums[i]]
        for key,val in dic.items():
            if len(val) == 1:
                return val[0]