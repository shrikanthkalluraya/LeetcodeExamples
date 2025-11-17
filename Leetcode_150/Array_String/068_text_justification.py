# 068 - Text Justification
# https://leetcode.com/problems/text-justification/

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        line_words = []
        n = len(words)
        line_length = 0
        
        for idx in range(n):
            line_words.append(words[idx])
            line_length += len(words[idx])
            
            if idx != n-1 and line_length + len(line_words) + len(words[idx+1]) > maxWidth:
                line = self.get_line(maxWidth, line_length, line_words)
                line_words = []
                line_length = 0
                res.append(line)
        res.append(self.get_line_without_padding(maxWidth, line_length, line_words))
        
        return res
    
    def get_line(self, maxWidth, line_length, line_words):
        padding = maxWidth - line_length
        if len(line_words) == 1:
            even_pads = padding
            extra_pads = 0
        else:
            even_pads = padding // (len(line_words) - 1)
            extra_pads = padding % (len(line_words) - 1)
        line = line_words[0]
        
        if len(line_words) == 1:
            line = line + (' ' * even_pads)
            return line
        for idx in range(1, len(line_words)):
            line = line + (' ' * even_pads) + (' ' if extra_pads > 0 else '') + line_words[idx]
            extra_pads -= 1
        
        return line
    
    def get_line_without_padding(self, maxWidth, line_length, line_words):
        padding = maxWidth - line_length - (len(line_words) - 1)
        return " ".join(line_words) + (' ' * padding)
