class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for number in nums:
            if number == target:
                return nums.index(number)
        return -1