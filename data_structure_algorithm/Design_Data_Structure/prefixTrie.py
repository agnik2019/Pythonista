class Trienode:
    def __init__(self):
        self.children = {}
        self.endsHere = False
class Trie(object):
    def __init__(self):
        self.root = Trienode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = Trienode()
            cur = cur.children[c]
        cur.endsHere = True
        
    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endsHere

    def startsWith(self, word):
        """
        :type prefix: str
        :rtype: bool
        """
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
        

word = "Birdman"
prefix = "Bird"
# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert(word)
param_2 = obj.search(word)
param_3 = obj.startsWith(prefix)
print(f"{param_2}   {param_3}")