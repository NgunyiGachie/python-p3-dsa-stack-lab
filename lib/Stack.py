class Stack:
    def __init__(self, items=[], limit=100):
        self.items = items
        self.limit = limit
        self.limit = max(limit, len(self.items)) 

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if not self.full():
            self.items.append(item)
        else:
            raise Exception("Stack is full")


    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.items.pop()
        
    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            return None
    
    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) >= self.limit

    def search(self, target):
        for i in range(len(self.items)):
            if self.items[i] == target:
                return i
        return -1
