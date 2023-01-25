class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        pre = 1
        post = 1
        #preA = []
        #postA = []
        
        for i,num in enumerate(nums):
            answer.append(pre)
            #preA.append(pre)
            pre = pre * num

        # wat
        for i,num in enumerate(reversed(nums)):
            #print(answer[-i-1])
            #print(num)
            #postA.append(post)
            answer[-i-1] = answer[-i-1]*post
            post = post * num
        #print(preA,postA)
        return answer
