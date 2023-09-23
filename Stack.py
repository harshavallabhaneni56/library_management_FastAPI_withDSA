import Node as nd

# stack has a variable top
class Stack:
    def __init__(self):
        self.top = None
    
    # returns the top value
    def peek(self):
        return self.top

    # adding element to the top of stack
    def push(self, data):
        # top is set to next
        next = self.top
        # new top is set to data and the current top is set to next
        new = nd.Node(data, next)
        # new top is updated as top
        self.top = new

    # removing elements from the top of the stack
    def pop(self):
        # if top is None, None is returned
        if not self.top:
            return None
        # top is set to popped_value
        popped_value = self.top
        # top is set to next value
        self.top = self.top.next
        # popped_value is removed
        return popped_value