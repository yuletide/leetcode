class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        #print(counter)
        #print(sorted(counter.keys()))
        # [key for key, _ in counter.most_common()]
        #sort = sorted(counter.items(), )
        arr = [key for key, _ in counter.most_common()]
        return arr[:k]
        