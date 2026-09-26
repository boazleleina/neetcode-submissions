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
        res = set()
        path = set()

        def dfs(r, c, node):
            #check if the character is out of bound and return False
            if (r<0) or (r >= row) or (c<0) or (c >= col) or ((r,c) in path) or (board[r][c] not in node.children):
                return False
            
            #character is valid, declare a node here
            node = node.children[board[r][c]]
            # check if the current node has a word
            if node.word != None:
                res.add(node.word)
            #insert the current cell to the path
            path.add((r,c))

            #recurse over all four neighboard
            dfs(r-1, c, node)
            dfs(r+1, c, node)
            dfs(r, c-1, node)
            dfs(r, c+1, node)

            #remove the cell from path
            path.remove((r,c))
        
        for r in range(row):
            for c in range(col):
                dfs(r,c,root)
        return list(res)
            
            
        