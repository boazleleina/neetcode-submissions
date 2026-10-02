class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        seen = set()
        q = collections.deque()

        q.append(beginWord)
        count = 1

        while q:
            for _ in range(len(q)):
                current_word = q.popleft()
                if current_word == endWord:
                    return count
                for i in range(len(current_word)):
                    for ch in range(ord('a'), ord('z')+1):
                        candidate_word = current_word[:i] + chr(ch) + current_word[i+1:]
                        if candidate_word not in seen and candidate_word in wordList:
                            q.append(candidate_word)
                            seen.add(candidate_word)
            count += 1
        return 0