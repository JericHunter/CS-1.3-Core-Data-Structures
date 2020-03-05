from sets import HashSet
import unittest


class SetTest(unittest.TestCase):

    def test_init(self):
        elements = ['S','H','A','U','N','E','L','L']
        s = HashSet(elements)
        assert s.ht.length() == 7
        assert s.size() == 7

    def test_add(self):
        s = HashSet()
        assert s.add('S') == True
        assert s.add('H') == True
        assert s.add('A') == True
        assert s.size() == 3

        assert s.add('A') == False
        assert s.add('H') == False
        assert s.add('S') == False

        assert s.size() == 3

    def test_remove(self):
        s = HashSet()
        s.add('S')
        s.add('H')
        s.add('A')

        s.remove('A')
        assert s.size() == 2

        s.remove('H')
        assert s.size() == 1

        s.remove('S')
        assert s.size() == 0

        with self.assertRaises(KeyError):
            s.remove('S')

    def test_contains(self):
        s = HashSet()

        s.add('S')
        assert s.contains('S') == True
        assert s.contains('H') == False

        s.add('H')
        assert s.contains('H') == True
        assert s.contains('S') == True

    def test_union(self):
        s1 = HashSet(['J', 'E', 'R', 'I'])
        s2 = HashSet(['H', 'U', 'N', 'T'])
        s3 = s1.union(s2)
        assert s3.contains('J') == True
        assert s3.contains('E') == True
        assert s3.contains('R') == True
        assert s3.contains('I') == True
        assert s3.contains('H') == True
        assert s3.contains('U') == True
        assert s3.contains('N') == True
        assert s3.contains('T') == True
        assert s3.size() == 8

    def test_intersection(self):
        s1 = HashSet(['J', 'E', 'R', 'I'])
        s2 = HashSet(['H', 'T', 'E', 'R'])
        s3 = s1.intersection(s2)
        assert s3.contains('E') == True
        assert s3.contains('R') == True
        assert s3.size() == 2

    def test_difference(self):
        s1 = HashSet(['J', 'I', 'E', 'R'])
        s2 = HashSet(['H', 'N', 'E', 'R'])
        s3 = s1.difference(s2)

        assert s3.contains('N') == True
        assert s3.contains('H') == True
        assert s3.size() == 2

    def test_is_subset(self):
        s1 = HashSet(['J', 'I', 'H'])
        s2 = HashSet(['J', 'I'])
        s3 = HashSet(['J', 'H'])
        s4 = HashSet(['H', 'F'])

        assert s1.is_subset(s2) == True
        assert s1.is_subset(s3) == True
        assert s1.is_subset(s4) == False


if __name__ == '__main__':
    unittest.main()
