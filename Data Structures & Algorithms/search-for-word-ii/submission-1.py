class TrieNode:
    def __init__(self):
        self.children = {}
        self.EOW = False

    def addWord(self,word):
        root = self
        for i in word:
            if i not in root.children:
                root.children[i] = TrieNode()
            root = root.children[i]
        root.EOW = True
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for i in words:
            root.addWord(i)
        ROW,COL = len(board),len(board[0])
        res,visit = set(),set()
        def dfs(r,c,root,word):
            if (r<0 or c<0 or r>=ROW or c>=COL or
                (r,c) in visit or board[r][c] not in root.children):
                return False

            visit.add((r,c))
            word+=board[r][c]
            root = root.children[board[r][c]]

            if root.EOW == True:
                res.add(word)

            dfs(r+1,c,root,word)
            dfs(r-1,c,root,word)
            dfs(r,c+1,root,word)
            dfs(r,c-1,root,word)

            visit.remove((r,c))

        for r in range(ROW):
            for c in range(COL):
                dfs(r,c,root,"")
        return list(res)
