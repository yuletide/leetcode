class Solution:
    def findMin(self, nums: List[int]) -> int:
        # input nums: sorted array that has been rotated
        # output: minimum element of array
        # constraints: logn time
        # approach: binary search for a descending relationship to indicate beginning of sorted array

        l = 0 
        r = len(nums)-1

        # base case: check if array is already cycled
        # if ascending, then we can return first element
        if nums[0] < nums[-1]:
            return nums[0]
        # i = 0 
        while l<r:
            # i += 1 # mystery infinite loop. valid solution with this
            # search until we find the point of dissension
            # check middle element
            mid = l+(r-l)//2
            # print("mid", mid)
            # print("numsmid", nums[mid])

            # is mid the end or beginning of the sorted array
            # if nums[mid] < nums[mid+1]:
            #     return nums[mid]
            # elif nums[mid]

            if nums[mid] > nums[r]:
                # print("right half solution")
                l = mid + 1
            else:
                r = mid
            # else:
                # print(nums, "we are not running either branch")
                # print(nums[mid])

        return nums[l]