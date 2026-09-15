class Stack:

    def __init__(self):
        self.st = []

    def push(self, val):
        self.st.append(val)

    def empty(self):
        if len(self.st) == 0:
            return 1
        else:
            return 0

    def peek(self):
        if self.empty():
            print("Empty")
            return
        else:
            return self.st[-1]
    def pop(self):
        if self.empty():
            print("Empty")
            return
        else:
            return self.st.pop()   
            

    def size(self):
        return len(self.st)



s = Stack()

s.push(10)
s.push(20)
s.push(30)

print("Size:", s.size())
print("Top:", s.peek())
print("Size:", s.size())
print("Top:", s.pop())
print("Size:", s.size())

print("Is empty:", s.empty())