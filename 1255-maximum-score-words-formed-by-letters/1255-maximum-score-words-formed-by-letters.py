from collections import Counter

class Solution:
    def _can_make(self, word):
        word_counter = Counter(word)
        for char in word:
            if word_counter[char] > self.counter[char]: 
                return False
        return True 
    
    def _backtracking(self, idx, score):
        if idx >= len(self.words):
            self.result = max(self.result, score)
            return
        
        self._backtracking(idx+1, score)
        
        if self._can_make(self.words[idx]):
            _score = 0
            
            for char in self.words[idx]:
                self.counter[char] -= 1
                _score += self.score[ord(char) - ord('a')]
            
            self._backtracking(idx+1, score+_score)
            
            for char in self.words[idx]:
                self.counter[char] += 1
            
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        self.words = words
        self.result = 0
        self.score = score
        self.counter = Counter(letters)
        self._backtracking(0, 0)
        
        return self.result