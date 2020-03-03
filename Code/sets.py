from hashtable import HashTable

class HashSet(object):
    """Initialize the new empty set, and add each element if the sequence is given"""
    def __init__(self, elements=None):
        self.ht = HashTable()
        if elements is not None:
            for element in elements:
                self.add(element)

    def size(self):
        """This property tracks the number of elements in constant time"""
        return self.ht.size

    def contains(self, element):
        """Returns a boolean to indicate whether an element is in this set"""
        return self.ht.contains(element)
