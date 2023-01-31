class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Complexity: Using sliding window: Goal is O(n)
        # Input: string
        # Output: Length of longest substring without repeating
        # Steps:

        # Vars:
        longestSeen = 0

        currentChars = set()

        left = 0
        right = 0

        # Steps
        # in each loop, move the right pointer to chomp
        # if new character breaks our uniqueness?
        # if new character increases string length ok
        while (right < len(s)):
            # print(f"{left} {s[left]} {right} {s[right]}")
            if s[right] in currentChars:
                # breaks unique
                while (s[left] != s[right]):
                    # shrink window until unique
                    currentChars.remove(s[left])
                    left += 1
                left += 1
            else:
                # add a unique character
                currentChars.add(s[right])  
                
            longestSeen = max(longestSeen, len(currentChars))
            right += 1
        return longestSeen



