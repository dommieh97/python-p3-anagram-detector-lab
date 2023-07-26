class Anagram:
    def __init__(self, word):
        self.word = word
        self.sorted_word = sorted(word)

    def match(self, possible_anagrams):
        matches = []
        for anagram in possible_anagrams:
            if sorted(anagram) == self.sorted_word:
                matches.append(anagram)
        return matches