class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(2*len(nums)):
            if i < len(nums):
                answer.append(nums[i])
            else:
                answer.append(nums[i-len(nums)])
        return answer