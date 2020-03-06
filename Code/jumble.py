class Jumble(object):
    def __init__(self):
        self.dict = self.create_dict()

    def create_dict(self):
        f = open('/usr/share/dict/words', 'r')
        sortedict = {}
        for word in f:
            word = word.strip().lower()
            sort = ''.join(sorted(word))
            sortedict[sort] = word
        return sortedict

    def create_solver(self, words):
        # List to add solved words to
        output = []
        sorted_input = ''.join(sorted(words))
        # loop through the given words
        for word in words:
            if sorted_input in self.dict:
                return self.dict[sorted_input]
            else:
                return None
            # check to make sure there are words
            if self.dict[sorted_input] is not None:

                # if there is only one option for the given word
                if len(self.dict[sorted_input]) == 1:
                    # add the single word to our output array
                    output.extend(self.dict[sorted_input])
                else:
                    # add the full array of solved word options
                    output.append(self.dict[sorted_input])
        # return the final word list
        return output

if __name__ == "__main__":
    jumble = Jumble()
    words = ['shast', 'doore', 'ditnic', 'catili']
    self.dict[sorted_input] = jumble.create_solver(words)
    print(solved_words)
