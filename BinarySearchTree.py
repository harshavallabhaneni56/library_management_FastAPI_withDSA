import BinarySearchNode as bsn

# BinarySearchTree class has variable root
class BinarySearchTree:
    def __init__(self):
        self.root = None

    # function to check where the new data should be inserted 
    def insert_helper(self, data, node):
        # if the data to be inserted is less than the node's value
        if data["id"] < node.data["id"]:
            # if the left node is empty, the new value is inserted there
            if not node.left:
                node.left = bsn.Node(data)
            # else, insert_helper method is called recursively by passing the left node
            else:
                self.insert_helper(data, node.left)
        # if the data to be inserted is greater than the node's value
        elif data["id"] > node.data["id"]:
            # if the right node is empty, the new value is inserted there
            if not node.right:
                node.right = bsn.Node(data)
            # else, insert_helper method is called recursively by passing the right node
            else:
                self.insert_helper(data, node.right)
        # since bst does not allow duplicates, if the data to be inserted is equal than the node's value
        # no change is made
        else:
            return

    # method to insert data
    def insert(self, data):
        # checks if the root is None
        # if it is, value is added to root
        if not self.root:
            self.root = bsn.Node(data)
        # else, insert_helper function is called
        else:
            self.insert_helper(data, self.root)

    # # helper function for search
    # def search_helper(self, input_id, node):
    #     # if the input_id is equal to the node's value
    #     if input_id == node.data["id"]:
    #         # node value is returned
    #         return node.data
    #     # if input_id is less than node's value and if left node exists
    #     if input_id < node.data["id"] and node.left is not None:
    #         # the search helper method is called recursively with left node
    #         return self.search_helper(input_id, node.left)
    #     # if input_id is greater than node's value and if right node exists
    #     if input_id > node.data["id"] and node.right is not None:
    #         # the search helper method is called recursively with right node
    #         return self.search_helper(input_id, node.right)
    #     # False is returned if the above conditions are not met
    #     return False

    # helper function for search
    def search_helper(self, input_id, node):
        input_id = int(input_id)
        # if the node has no left or right child
        if node.left == None and node.right == None:
            return False
        # if the input_id is equal to the node's value
        if input_id == node.data["id"]:
            # node value is returned
            return node.data
        # print(type(input_id))
        # print(type(node.data["id"]))
        # if input_id is less than node's value
        if input_id < node.data["id"]:
            if input_id == node.left.data["id"]:
                return node.left.data
            # the search helper method is called recursively with left node
            return self.search_helper(input_id, node.left)
        # if input_id is greater than node's value 
        if input_id > node.data["id"]:
            if input_id == node.right.data["id"]:
                return node.right.data
            # the search helper method is called recursively with right node
            return self.search_helper(input_id, node.right)

    # method to insert data
    def search(self, input_id):
        # checks if the root is None
        # if it is not, False is returned
        if not self.root:
            return False
        # else, search_helper method is called
        else:
            return self.search_helper(input_id, self.root)