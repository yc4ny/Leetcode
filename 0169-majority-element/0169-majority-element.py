class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        track = {} 
        for number in nums:
            if number in track:
                track[number] += 1
            else:
                track[number] = 1
        majority = 0
        cur_val = 0 
        
        for key, val in track.items():
            if val > cur_val:
                cur_val = val 
                majority = key 
        
        return majority
            