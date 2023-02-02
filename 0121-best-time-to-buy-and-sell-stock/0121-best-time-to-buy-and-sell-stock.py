class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # prices[i] = price on i day
        # Sliding window has a window of data that can be processed
        # slide L and R both through input
        # commutative operations -- process ingoing and outgoing element from window
        # changes O(n^2) to O(n)

        # input: list of prices
        # output: maximum profit 
        # vars: min buy price, max sale price
        # steps: 
        # Brute force solution: two nested loops, buy on day 1, sell on day 2-n, buy on day 2, sell on day 3-n. We can do better
        # set two pointers to create a sliding window
        # left pointer starts at 0
        # right pointer starts at 1
        # move right pointer over 1 - save max profit
        # if right cell is less than left, we should move left pointer 
        # then move right pointer and check profit until end
         
        l, r = 0, 1
        # print(prices, l, r)
        max_profit = 0

        while r < len(prices):
            max_profit = max(max_profit, prices[r]-prices[l])
            # print(max_profit, l, r)
            if (prices[r]<prices[l]):
                l = r
            r +=1

        return max_profit