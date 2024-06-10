from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0 
        
        wordSet = set(wordList)
        checkSet = set()
        q = deque()
        q.append((beginWord, 1))
        
        
        while q:
            word, cnt = q.popleft()
            if word == endWord:
                return cnt
            
            for i in range(len(word)):
                for j in range(97, 97+26+1):
                    newWord = word[:i] + chr(j) + word[i+1:]
                    if newWord not in checkSet and newWord in wordSet:
                        q.append((newWord, cnt+1))
                        checkSet.add(newWord)
        
        return 0