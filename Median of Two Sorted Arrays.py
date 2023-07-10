class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        list1=nums1+nums2
        list1.sort()
        length=len(list1)
        if length%2==1:
            return float(list1[((length+1)//2)-1])
        else:
            return (list1[length//2-1]+list1[(length//2)])/2 