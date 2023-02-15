class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        Input: matrix: m x n, target number
        Ouput: true/false if target is in matrix
        Constraints: O(logmn) tie
        - matrix is sorted in ascending order
        - n <= 100
        - values between +/-10^4


        Approach: 2d binary search. 
        1. first find the row its in, then the column
        2. binary search vertically: check the first value of the middle row. 
            If value is higher, check last value in that row
            Continue vertic

        Slow way: concatenate into one flat array and binary search, but that's O(n)
        '''

        l = 0
        r = len(matrix) - 1
        width = len(matrix[0])

        # iterative binary search
        # two pointers, if target is less than middle, set r pointer to middle -1 else set l pointer to middle + 1
        while l <= r:
            # print("lr",l,r)
            # m = l + ((r - l) // 2)  # (l + r) // 2 can lead to overflow
            middle = l + (r-l // 2)
            # print("searching middle", middle)

            if matrix[middle][0] == target:
                # print("found target")
                return True
            elif matrix[middle][0] < target and matrix[middle][width-1] >= target:
                row = matrix[middle]
                _l, _r = 0, width-1
                while _l <= _r:
                    _m = _l + (_r-_l // 2)
                    if row[_m] == target:
                        # print("found")
                        return True
                    elif row[_m] < target:
                        # print("target greater, search east")
                        _l = _m + 1
                    elif row[_m] > target:
                        _r = _m -1

                # print("target is in this row, binary search the row")
                break
            elif target > matrix[middle][0]:
                l = middle + 1
                # print("target is longer, search south")
            elif target < matrix[middle][0]:
                # print("target is smaller, search north")
                r = middle - 1

            # find the row first vertically


        # height = len(matrix)
        # width = len(matrix[0])

        # row = int(height/2)
        # searching = True
        # return self.searchVertical(matrix, target)

    
    # def searchVertical(self, matrix, target) -> bool:
    #     height = len(matrix)
    #     middle = int(height/2)
    #     print("search vertical", middle)
    #     if matrix[middle][0] == target:
    #         print("value found")
    #         return True
    #     elif matrix[middle][0] < target:
    #         print("row header less than")
    #     else:
    #         print("row header great than")

        

        
    #     # check middle row first
    #     # if (int(matrix[height/2]))

        
    # def searchRow(self, matrix, target, n) -> bool:
    #     pass
    #     # find a value within a row
