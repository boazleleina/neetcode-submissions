class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        def _insert(w):
            node = root
            for c in w:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.word = w
        
        for w in words:
            _insert(w)
        
        row, col = len(board), len(board[0])
        res = []
        path = set()

        def dfs(r, c, node):
            #check if the character is out of bound and return False
            if (r<0) or (r >= row) or (c<0) or (c >= col) or ((r,c) in path) or (board[r][c] not in node.children):
                return False
            
            #get the character
            ch = board[r][c]
            #character is valid, declare a node here
            child = node.children[ch]
            # check if the current node has a word
            if child.word != None:
                res.append(child.word)
                #change word to None after we get it
                child.word = None
            #insert the current cell to the path
            path.add((r,c))

            #recurse over all four neighboard
            dfs(r-1, c, child)
            dfs(r+1, c, child)
            dfs(r, c-1, child)
            dfs(r, c+1, child)

            #remove the cell from path
            path.remove((r,c))

            #if child branch is dead the prune it, no more words in the branch
            if not child.children and child.word == None:
                del node.children[ch]
           

        
        for r in range(row):
            for c in range(col):
                dfs(r,c,root)
        return res
            
            
        