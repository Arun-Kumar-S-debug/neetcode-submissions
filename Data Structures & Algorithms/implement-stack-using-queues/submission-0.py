class MyStack:

    def __init__(self):
        self.que1=[]
        self.que2=[]

    def push(self, x: int) -> None:
        if len(self.que1)==0:
            self.que1.append(x)
            return None
        else:
            self.que2.append(x)
            for i in self.que1:
                self.que2.append(i)
            self.que1.clear()
            for i in self.que2:
                self.que1.append(i)
            self.que2.clear()
        return None


    def pop(self) -> int:
        if len(self.que1)==0:
            return None
        return self.que1.pop(0)

    def top(self) -> int:
        if len(self.que1)==0:
            return None
        return self.que1[0]

    def empty(self) -> bool:
        if len(self.que1)==0:
            return True
        return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()