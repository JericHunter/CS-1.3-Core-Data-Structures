from hashtable import HashTable

class HashSet(object):
    "Initialize the new empty set, and add each element if the sequence is given"
    def __init__(self, elements=None):
        self.ht = HashTable()
        if elements is not None:
            for element in elements:
                self.add(element)
