class MinStack: 
    
    def __init__(self):
        self.min = []
        # self.max = [float('inf')]
        self.stack = deque([])

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.min.append(val)
        elif val <= self.min[-1]:
            self.min.append(val)
        
        self.stack.append(val)
        # print(f"pushed {val} stack: {self.stack} min: {self.min}")
        
        # if val > self.max[-1]:
        #     self.max.append(val)

    def pop(self) -> None:
        final = self.stack[-1]
        # print('removing', final, self.stack, self.min)
        self.stack.pop()
        if self.min[-1] == final:
            self.min.pop()
        # print('removed', self.stack, self.min)
        # if self.max == final:
        #     self.max.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        # print("get min", self.min[-1])
        return self.min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()