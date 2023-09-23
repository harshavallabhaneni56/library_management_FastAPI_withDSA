import Node as nd

# Data class helps maintain the values as key,value (dict)
class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

# hashtable class has variables size_table
class HashTable:
    def __init__(self, size_table):
        self.size_table = size_table
        self.hashTable = [None] * size_table

    # function for custom hash function is created by adding ascii value of the key
    # and multiple it to the total output_hash calculated to avoid collision
    # The modulo of output_hash and hashTable size is used to get the index
    def hash_function(self, key):
        output_hash = 0
        for i in key:
            output_hash += ord(i)
            output_hash = (output_hash * ord(i)) % self.size_table
        return output_hash

    # using the hash_function to find the index in hashTable
    def add_key_value_to_hash_table(self, key, value):
        # key is passed to hash_function to get the index
        hashed_index = self.hash_function(key)
        # checks if a value is present in the hashTable at index hashed_index
        # if no value is present
        if self.hashTable[hashed_index] is None:
            # a new node is created as dict(Data object) and value is set as None
            self.hashTable[hashed_index] = nd.Node(Data(key, value), None)
        # if value is present at hashed_index
        else:
            # iterates through the the linked list in value till it reaches the end
            node = self.hashTable[hashed_index]
            while node.next:
                node = node.next
            # a new node is created as dict(Data object) and value is set as None
            # this node is added to the end
            node.next = nd.Node(Data(key, value), None)

    # get value by passing key
    def get_value_by_key(self, key):
        # key is passed to hash_function to get the index
        hashed_index = self.hash_function(key)
        # checks if a value is present in the hashTable at index hashed_index
        # if value is present
        if self.hashTable[hashed_index] is not None:
            node = self.hashTable[hashed_index]
            # if only one value is present
            if node.next is None:
                # returns the value
                return node.data.value
            # if there are multiple values present
            while node.next:
                # checks if each key in linked list is equal to the input key
                if key == node.data.key:
                    # if the ket is found, the corresponding value is returned
                    return node.data.value
                node = node.next
            # checks for last value
            if key == node.data.key:
                return node.data.value
        # if key does not match, None is returned
        return None