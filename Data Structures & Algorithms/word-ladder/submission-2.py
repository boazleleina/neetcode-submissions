class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        wordList = set(wordList)

        if endWord not in wordList:
            return 0
        
        seen = set()
        q = collections.deque()

        q.append(beginWord)
        seen.add(beginWord)
        count = 1

        while q:
            for _ in range(len(q)):
                current_word = q.popleft()
                if current_word == endWord:
                    return count
                for i in range(len(current_word)):
                    for alp in range(ord('a'), ord('z')+1):
                        candidate = current_word[:i] + chr(alp) + current_word[i+1:]
                        if candidate in wordList and candidate not in seen:
                            seen.add(candidate)
                            q.append(candidate)
            count +=1
        
        return 0
