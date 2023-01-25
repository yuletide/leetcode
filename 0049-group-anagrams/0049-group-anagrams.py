class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}
        for word in strs:
            wordCounter = Counter(word)
            key = json.dumps(sorted(wordCounter.items()))
            #print(key)
            if key in hash.keys():
                hash[key].append(word)
            else:
                hash[key] = [word]
        #print(hash)
        return hash.values()