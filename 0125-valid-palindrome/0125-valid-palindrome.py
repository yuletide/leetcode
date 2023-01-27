class Solution:
    def isPalindrome(self, s: str) -> bool:
        

        # two pointers method
        l = 0
        r = len(s)-1
        # print(s[l],s[r])

        while(l<r):
            # print(l,r, s[l], s[r])
            # can use ascii values but thats silly
            while not s[l].isalnum() and l<r:
                l = l+1
            
            while not s[r].isalnum() and r>l:
                r = r-1
            # print(l,r, s[l], s[r])

            if s[l].lower() == s[r].lower():
                # print('still palindrome')
                l += 1
                r -= 1
            else:
                return False
        return True
        