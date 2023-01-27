class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
            
        # might not work since this makes it nlogn
        sort = sorted(nums)
        longestSeq = [sort[0]]
        last = sort[0]
        seq = [sort[0]]

        for i in range(1, len(nums)):
            # print(i, sort[i])
            if (sort[i] == last):
                # print("duplicate skipping")
                # skip duplicates
                continue
            if (sort[i] == last+1):
                print('sequence')
                # if we are counting a sequence
                seq.append(sort[i])
                if (len(seq) > len(longestSeq)):
                    longestSeq = seq
            else:
                # print('not sequence')
                # the sequence is over, if it is now the longest move it over
                if (len(seq) > len(longestSeq)):
                    longestSeq = seq
                seq = [sort[i]]
            last = sort[i]

        return len(longestSeq)