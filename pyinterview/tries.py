class TrieNode:
    def __init__(self, letter=None):
        self.letter = letter
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode("*")

    def add_word(self, word: str) -> None:
        itr = self.root
        for letter in word:
            if letter not in itr.children:
                itr.children[letter] = TrieNode(letter)
            itr = itr.children[letter]
        itr.is_end_of_word = True

    def search(self, word: str) -> bool:
        itr = self.root
        for letter in word:
            if letter not in itr.children:
                return False
            itr = itr.children[letter]
        return itr.is_end_of_word

    def starts_with(self, word: str) -> bool:
        itr = self.root
        for letter in word:
            if letter not in itr.children:
                return False
            itr = itr.children[letter]
        return True
