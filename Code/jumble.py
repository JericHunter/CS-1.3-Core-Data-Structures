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

    def create_word_solver(self,word):
        sorted_input = ''.join(sorted(word))

        if sorted_input in self.dict:
            return self.dict[sorted_input]
    def create_solver(self, words):
        # List to add solved words to
        solved = []
        # loop through the given words
        for word in words:
            solved_words = self.create_word_solver(word)
            # check to make sure there are words
            if solved_words:
                if len(solved_words) == 1:
                    solved.prepend(solved_words)
                else:
                    solved.append(solved_words)
        # return the word list
        return solved

if __name__ == "__main__":
    jumble = Jumble()
    words = ['shast', 'doore', 'ditnic', 'bureek']
    solved_words = jumble.create_solver(words)
    print(solved_words)
