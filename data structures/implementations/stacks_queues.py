'''
class implementation
'''
class Stack():
    # First In Last Out
    def __init__(self):
        self.arr = []
    
    def push(self, x):
        self.arr.append(x)

    def peek(self):
        return self.arr[-1]
    
    def pop(self):
        return self.arr.pop()
        

class Queue():
    # First In First Out
    def __init__(self):
        self.arr = []
    
    def push(self, x):
        self.arr.append(x)

    def peek(self):
        return self.arr[0]
    
    def pop(self):
        return self.arr.pop(0)

'''
example questions
'''
# Next [Greater] Element: return array of elements that match a certain property at a given index
def nextGreaterElement(arr): 
    stack = []
    answer = [-1]*len(arr)

    for idx, curr in enumerate(arr):
        if stack:
            while stack and curr > stack[-1][1]:
                f, found = stack.pop()
                answer[f] = curr

        stack.append([idx,curr])
        
    # with loops allowed
    for curr in arr:
        if stack:
            while stack and curr > stack[-1][1]:
                f, found = stack.pop()
                answer[f] = curr
    
    return answer
        
