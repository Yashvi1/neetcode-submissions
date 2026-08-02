class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)


    def pop(self) -> None:
        del self.stack[-1]
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        # min = float('inf')
        return min(self.stack)
        # for element in self.stack:
        #     if min > element:
        #         min = element
        # return min

        
