class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.strip().split(' ')
        idx = 0
        print(words)
        while idx < len(words):
            if words[idx] == '':
                del words[idx]
            else:
                words[idx] = words[idx].strip()
                idx += 1
        print(words)
        rev_words = reversed(words)
        return " ".join(rev_words)
