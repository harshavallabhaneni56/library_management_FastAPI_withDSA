import Node as nd

# Queue class has a head and tail variables
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    # adding elements to the end of the queue
    def enqueue(self, data):
        # checking if the queue is empty
        # if the queue is empty
        if self.tail is None and self.head is None:
            # head and tail is assigned to new node
            self.tail = self.head = nd.Node(data, None)
            return
        # else, new node is added to the next node after tail
        self.tail.next = nd.Node(data, None)
        # tail is set to new node
        self.tail = self.tail.next
        return

    # removing elements from the front of the queue
    def dequeue(self):
        # checking if the queue is empty
        # if the queue is empty, None is returned
        if self.head is None:
            return None
        # head is assigned to popped_value variable
        popped_value = self.head
        # setting head to next node
        self.head = self.head.next
        # if head is None, tail is also set to None
        if self.head is None:
            self.tail = None
        # 'popped_value' is returned
        return popped_value