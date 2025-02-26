class Solution:
    def arrangeWords(self, text: str) -> str:
        word_list = []
        for idx, word in enumerate(text.split(" ")):
            word_list.append((len(word), idx, word.lower()))
        word_list.sort()
        result = word_list[0][2][0].upper() + word_list[0][2][1:] + " "
        result += " ".join([word for _, _, word in word_list[1:]])

        return result
        