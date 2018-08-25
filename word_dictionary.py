import re


class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.word_dictionary = {}
        print(type(self.word_dictionary))

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        current = self.word_dictionary
        for char in word:
            if char not in current:
                current[char] = {}
            current = current[char]
        current["end"] = "end"

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        current = self.word_dictionary
        for char in word:
            if char not in current and char != '.':
                return False
            elif char == '.':
                for each k in current.keys():


            current = current[char]
        if "end" in current:
            return True
        return False


# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord("bad")
obj.addWord("bab")
obj.addWord("mad")
print(obj.word_dictionary)
print(obj.search("pad"))
print(obj.search("bad"))
print(obj.search(".ad"))
print(obj.search("b.."))
obj.addWord("a")
obj.addWord("ab")
print "------------------------------"
print obj.search("a")
print obj.search("a.")
print obj.search("ab")
print obj.search(".a")
print obj.search(".b")
print obj.search("ab.")
print obj.search(".")
print obj.search("..")


    #b': {'a': {'b': {'end': 'end'}, 'd': {'end': 'end'}}}, 'm': {'a': {'d': {'end': 'end'}}}}




