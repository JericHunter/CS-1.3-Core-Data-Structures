#!python

def contains(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found.
    Time Complexity: O(p * t) -- p being length of pattern and t being length of text
    """
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement contains here (iteratively and/or recursively)

    return find_index(text, pattern) != None


def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found.
    Time Complexity: O(p * t) -- p being length of pattern and t being length of text
    """
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_index here (iteratively and/or recursively)
    if len(pattern) > len(text):
       return None
    if pattern == '':
       return 0
    for i, letter in enumerate(text):
        if letter == pattern[0]:
            for x, letter2 in enumerate(pattern):
                current_index = x + i
                if current_index > len(text)-1 or text[current_index] != letter2:
                   break
            else:
               return i
    return None

def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found.
    Time Complexity: O(p * t) -- p being length of pattern and t being length of text
    """
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    if len(pattern) > len(text):
        return []
    if pattern == '':
        return [i for i in range(len(text))]
    index = []
    for i, letter in enumerate(text):
        if letter == pattern[0]:
            for x, letter2 in enumerate(pattern):
                curr_index = x + i
                if curr_index > len(text)-1 or text[curr_index] != letter2:
                    break
            else:
                index.append(i)
    return index

def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, index))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
