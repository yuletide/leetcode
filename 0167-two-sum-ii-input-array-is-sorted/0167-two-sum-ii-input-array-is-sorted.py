class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1

        while (l<r):
            numL=numbers[l]
            numR=numbers[r]
            # print(numL, numR)
            if (numbers[l]+numbers[r]<target):
                # print('sum too small')
                l += 1
            elif (numL+numR>target):
                # print('sum too large')
                r -= 1
            elif (numL+numR == target):
                # print('equal')
                return [l+1, r+1]

