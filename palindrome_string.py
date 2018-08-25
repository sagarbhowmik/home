class Word(object):
    def __init__(self, my_word):
        self.my_word = my_word
        print "Word entered: {}".format(my_word)

    def is_palindrom(self):
        """
        Returns whether given word is palindrome or not
        :param my_word: String input
        :return: Bool True/False if
        """
        if not self.my_word:
            return False
        for i in range(0, len(self.my_word) / 2):
            j = len(self.my_word) - 1 - i
            if self.my_word[i] != self.my_word[j]:
                return False
        return True


obj = Word("a")
print obj.is_palindrom()