class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # binary search!
        # recursive -- 
        # input: sorted array
        # output: index of target or -1

        # steps
        # check the item at len(list)/2
        # if item is greater than our target, then binary search the left half of the list
        # if item is less than target, search the right half
        def recurse(_nums: List[int], startIndex: int) -> int:
            # print("recurse", _nums, startIndex)
            if len(_nums) == 1:
                return startIndex if _nums[0] == target else -1
            
            pivot = int(len(_nums) / 2)
            print("pivot", pivot, _nums[pivot])
            if _nums[pivot] == target:
                # print('found item at pivot')
                return startIndex + pivot
            elif _nums[pivot] < target:
                # print('target greater than pivot searching right half', _nums[pivot:], startIndex)
                return recurse(_nums[pivot:], startIndex + pivot)
            else:
                # print('searchign left half')
                return recurse(_nums[:pivot], startIndex)

        return recurse(nums, 0)
