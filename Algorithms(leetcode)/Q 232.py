# 2021.02.26. Leetcode algorithm problem #232
# Implement queue using Stacks

class MyQueue:
    def __init__(self):
        self.input = []
        self.output = []

    def push(self,x):
        self.input.append(x)

    def pop(self):
        self.peek()
        return self.output.pop()

    def peek(self):
        # output only once
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self):
        return self.input == [] and self.output == []


