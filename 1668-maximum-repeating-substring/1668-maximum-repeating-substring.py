class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        sequence_len = len(sequence)
        word_len = len(word)
        
        if sequence_len == word_len:
            if "".join(sequence) == word: return 1
            else: return 0
        
        dp = [0] * sequence_len + [0]
        first_index = 0
        
        for last_index in range(word_len, sequence_len+1):
            if "".join(sequence[first_index:last_index]) == word:
                dp[last_index] = dp[first_index] + 1
            first_index += 1
        
        return max(dp)