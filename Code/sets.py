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

    def add(self, element):
        """Add an element to this set if it is not already present"""
        if self.contains(element):
            return False
        else:
            self.ht.set(element,1)
            return True

    def remove(self, element):
        """Remove the element from this set"""
        self.ht.delete(element)

    def union(self, other_set):
        new_set = HashSet()

        for item in self.ht.keys():
            new_set.add(item)

        for item in other_set.ht.keys():
            new_set.add(item)

        return new_set

    def intersection(self, other_set):
        """Returns a new set that is the intersection of this set and other_set"""
        new_set = HashSet()

        for item in self.ht.keys():
            if other_set.contains(item):
                new_set.add(item)

        for item in other_set.ht.keys():
            if self.contains(item):
                new_set.add(item)

        return new_set


    def difference(self, other_set):
        """Returns a new set that is the difference of this set and other_set"""
        new_set = HashSet()

        for item in other_set.ht.keys():
            if self.contains(item) == False:
                new_set.add(item)

        return new_set

    def is_subset(self, other_set):
        """Returns a boolean indicating whether other_set is a subset of this set"""
        for item in other_set.ht.keys():
            if self.contains(item) == False:
                return False

        return True
