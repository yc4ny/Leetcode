class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        bool = False
        for i in range(len(arr)-1):
            for j in range(i+1,len(arr)):
                if arr[i] *2 == arr[j]:
                    bool = True
                if arr[j] * 2 == arr[i]:
                    bool = True
        
        return bool