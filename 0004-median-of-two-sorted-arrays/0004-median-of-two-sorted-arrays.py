class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        liste = []
        for num in nums1:
            liste.append(num)
        for num in nums2:
            liste.append(num)
        liste = sorted(liste)
        if len(liste) %2 == 0 :
            return (liste[int(len(liste)/2)] + liste[int(len(liste)/2) - 1])/2
        else:
            return liste[int(len(liste)/2)]