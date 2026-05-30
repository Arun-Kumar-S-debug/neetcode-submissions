class MyQueue:

    def __init__(self):
        self.st1=[]
        self.st2=[]
        self.top=-1

    def push(self, x: int) -> None:
        self.st2.append(x)
        self.top+=1
        for i in self.st1:
            self.st2.append(i)
        self.st1.clear()
        for i in self.st2:
            self.st1.append(i)
        self.st2.clear()
        return None

    def pop(self) -> int:
        self.top-=1
        return self.st1.pop()

    def peek(self) -> int:
        return self.st1[self.top]

    def empty(self) -> bool:
        return self.top==-1
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()