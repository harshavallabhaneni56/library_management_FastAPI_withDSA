import Node as nd

class LinkedList:
    # Linked List class has variables head and tail
    def __init__(self):
        self.head = None
        self.tail = None

    # inserts the data at the beginning of linked list
    def beginning_insert(self, data):
         # if the linked list is empty, data is added at the beginning and 
         # tail is also pointed to that node
        if self.head is None:
            self.head = nd.Node(data, None)
            self.tail = self.head
            return
        # new node is created and it's next is set to head
        new_node = nd.Node(data, self.head)
        # head is set to the new node, thereby adding the data at the beginning
        self.head = new_node

    # inserts the data at the end of linked list
    def end_insert(self, data):
        # if the linked list is empty, data is added at the beginning
        if self.head is None:
            self.beginning_insert(data)
            return
        # data is added at the end and tail's next value is set to None
        self.tail.next = nd.Node(data, None)
        self.tail = self.tail.next

    # takes in user_id, iterates through the linked list and returns the user node
    # if it matches the linked list
    def get_author_by_id(self, user_id):
        node = self.head
        while node:
            if node.data["id"] is int(user_id):
                return node.data
            node = node.next
        return None

    # printing out the data in the linked list
    def display_ll(self):
        out = ""
        node = self.head
        # if no value is present in the linked list, None is printed
        if node is None:
            print(None)
        # iterating through linked list and adding each value to the output variable
        while node:
            out += f" {str(node.data)} ->"
            node = node.next
        out += " None"
        # out is printed
        print(out)

    # converting linked list to list
    def convert_ll_to_list(self):
        # output list declared and initialized
        out = []
        # if no value is present in the linked list, empty out list is returned
        if self.head is None:
            return out
        # iterating through linked list and adding each value to the out list
        node = self.head
        while node:
            out.append(node.data)
            node = node.next
        # 'out' list is returned
        return out