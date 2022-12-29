class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        output = []
        for i in range(n):
            output.append(nums[i::n])
        final = []
        rang = len(nums) // n 
        for i in range(len(output)):
            for j in range(rang):
                final.append(output[i][j])
        return final