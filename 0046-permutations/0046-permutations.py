class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        for x in itertools.permutations(nums, len(nums)):
            result.append(x)
        
        return result