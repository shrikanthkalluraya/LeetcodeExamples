class Solution:
    def romanToInt(self, s: str) -> int:
        # res = 0
        # i = 0
        # n = len(s)
        # while i < n:
        #     c = s[i]
            
        #     if c == 'I':
        #         if i != n-1 and s[i+1] == 'V':
        #             res += 4
        #             i += 1
        #         elif i != n-1 and s[i+1] =='X':
        #             res += 9
        #             i += 1
        #         else:
        #             res += 1
        #     elif c == 'V':
        #         res += 5
        #     elif c == 'X':
        #         if i != n-1 and s[i+1] == 'L':
        #             res += 40
        #             i += 1
        #         elif i != n-1 and s[i+1] =='C':
        #             res += 90
        #             i += 1
        #         else:
        #             res += 10
        #     elif c == 'L':
        #         res += 50
        #     elif c == 'C':
        #         if i != n-1 and s[i+1] == 'D':
        #             res += 400
        #             i += 1
        #         elif i != n-1 and s[i+1] =='M':
        #             res += 900
        #             i += 1
        #         else:
        #             res += 100
        #     elif c == 'D':
        #         res += 500
        #     elif c == 'M':
        #         res += 1000
        #     i += 1
        #     print(res)
        # return res

        roman_to_integer = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        s = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")
        return sum(map(lambda x: roman_to_integer[x], s))
