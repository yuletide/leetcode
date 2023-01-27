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
            # print(i, sort[i], len(nums)-1)
            if (sort[i] == last):
                # print("duplicate skipping")
                # skip duplicates
                if (len(seq) > len(longestSeq)):
                    longestSeq = seq
                continue
            if (sort[i] == last+1):
                # print('sequence')
                # if we are counting a sequence
                seq.append(sort[i])
            else:
                # print('not sequence')
                # the sequence is over, if it is now the longest move it over
                if (len(seq) > len(longestSeq)):
                    longestSeq = seq
                seq = [sort[i]]

            if (i == len(nums)-1):
                # print('last item')
                if (len(seq) > len(longestSeq)):
                    longestSeq = seq
            last = sort[i]

        return len(longestSeq)