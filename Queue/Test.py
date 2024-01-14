class MyStack:

    def __init__(self):
        self.myQueue = []
        self.myQueue_temp = []
        

    # only push to back
    def push(self, x: int) -> None:
        self.myQueue.append(x)
        
    
    # pop from front
    def pop(self) -> int:
        if self.myQueue:
            i = 0
            the_len = len(self.myQueue)
            while i < the_len - 1:
                val = self.myQueue.pop(0)
                self.myQueue_temp.append(val)
                i += 1
                
            res = self.myQueue.pop(0)
            self.myQueue, self.myQueue_temp = self.myQueue_temp, self.myQueue
            return res
    
        
    
    # peek from front
    def top(self) -> int:
        if self.myQueue:
            val = 0
            while self.myQueue:
                val = self.myQueue.pop(0)
                self.myQueue_temp.append(val)
            self.myQueue, self.myQueue_temp = self.myQueue_temp, self.myQueue
            return val
    

    def empty(self) -> bool:
        return len(self.myQueue) == 0
        


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
print(obj.top())   # Output: 2
print(obj.pop())   # Output: 2
print(obj.empty()) # Output: False