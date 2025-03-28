# lemonadeChange LeetCode# 860
class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        five_count = 0
        ten_count = 0
        cash_available = 0


        for bill in bills:
            if bill == 5:
                five_count += 1
            elif bill == 10:
                if five_count>0:
                    five_count-=1
                    ten_count+=1
                else:
                    return False
            elif bill == 20:
                if ten_count>0 and five_count>0:
                    ten_count-=1
                    five_count-=1
                elif five_count>=3:
                    five_count-=3
                else:
                    return False
        return True
