class MinStack:

    def __init__(self):
        self.sta=[]
        return

    def push(self, val: int) -> None:
        self.sta.insert(0,val)
        return

    def pop(self) -> None:
        self.sta.pop(0)

    def top(self) -> int:
        return self.sta[0]

    def getMin(self) -> int:
        return min(self.sta)
