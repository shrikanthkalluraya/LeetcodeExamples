# 2260. Minimum Consecutive Cards to Pick Up
'''
You are given an integer array cards where cards[i] represents the value of the ith card. A pair of cards are matching if the cards have the same value.

Return the minimum number of consecutive cards you have to pick up to have a pair of matching cards among the picked cards. If it is impossible to have matching cards, return -1.
'''
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        left = 0
        sub_array = {}
        min_len = len(cards) + 1

        for right in range(len(cards)):
            sub_array[cards[right]] = sub_array.get(cards[right], 0) + 1
            print(sub_array, left, right)
            while sub_array[cards[right]] > 1:
                min_len = min(min_len, right-left+1)
                sub_array[cards[left]] -= 1
                left += 1
        if min_len > len(cards):
            return -1
        return min_len
