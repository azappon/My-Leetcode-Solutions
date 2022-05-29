class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1 + nums2 # create a list with all values (we need also the duplicates)
        merged.sort() # sort the values in increasing order
        lenght = len(merged) # compute the lenght value once to save memory later
        
        if not merged: # if the merged array is empty return 0
            return 0
        elif (lenght % 2) != 0: # if there is an odd number of element in the array return the value of the middle one
            return merged[int(lenght/2)]
        else: # otherwise compute the average between the two middle ones
            return ((merged[int(lenght/2)-1]) + (merged[int(lenght/2)])) / 2
