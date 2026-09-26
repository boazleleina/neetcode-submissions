class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root

        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end = True

    def search(self, word: str) -> bool:
       
        def bfs(index, node):
            if index == len(word):
                return node.is_end
            
            char = word[index]

            if char == ".":
                #check all the children
                for child in node.children.values():
                    #recurse through the children node
                    if bfs(index+1, child):
                        #the values match so return true
                        return True
                return False
            else:
                if char not in node.children:
                    return False
                return bfs(index+1, node.children[char])
        return bfs(0, self.root)