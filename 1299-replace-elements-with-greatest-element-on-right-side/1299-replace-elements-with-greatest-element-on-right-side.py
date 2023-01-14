class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if (len(arr) == 1): return [-1]
        #To sort the list in ascending order. Its time complexity is O(NlogN).
        # copy all remaining items to new array
        replaced = []

        sorted = arr.copy()
        sorted.sort(reverse=True)
        for i, num in enumerate(arr):
            # print(num, i)=
            sorted.remove(num)
            if i >= len(arr)-1:
                replaced.append(-1)
            else:
                replaced.append(sorted[0])
        return replaced
