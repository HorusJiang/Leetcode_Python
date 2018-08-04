class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # left,right = 0,len(A) -1
        # while left<right:
        #     mid = (left + right)//2
        #     if A[mid-1] < A[mid] and A[mid] <A[mid+1]:
        #         left = mid
        #     elif A[mid - 1] > A[mid] and A[mid] > A[mid+1]:
        #         right = mid
        #     else:
        #         break
        # return mid
        
        # Note 3: A is a mountain, as defined above.
        return A.index(max(A))

        