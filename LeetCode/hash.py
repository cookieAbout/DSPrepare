""" Решения с хэш """
from typing import List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        """ https://leetcode.com/problems/number-of-equivalent-domino-pairs/description/ """
        hash_pairs = {}
        # Brute force, слишком долго, падает на большом объеме
        # for i in range(len(dominoes)):
        #     for j in range(i + 1, len(dominoes)):
        #         cnt += int(
        #             (dominoes[i][0] == dominoes[j][1] and dominoes[i][1] == dominoes[j][0]) or
        #             (dominoes[i][0] == dominoes[j][0] and dominoes[i][1] == dominoes[j][1])
        #         )
        for i in range(len(dominoes)):
            pair = hash(frozenset(dominoes[i]))
            if pair in hash_pairs:
                hash_pairs[pair] += 1
            else:
                hash_pairs[pair] = 1
        return int(sum([i * (i - 1) / 2 for i in hash_pairs.values()]))

    def polinom_hash(self, s, p=31, m=10**9 + 9):
        """
        Полиномиальный хэш
        1 * p^0 + 2 * p^1 + 3 * p^2
        """
        hash_value = 0
        p_pow = 1  # p^0 = 1

        for char in s:
            # Преобразуем символ в число (например, 'a' → 1, 'b' → 2, и т.д.)
            char_code = ord(char) - ord('a') + 1
            hash_value = (hash_value + char_code * p_pow) % m
            p_pow = (p_pow * p) % m

        return hash_value


s = Solution()
# print(s.numEquivDominoPairs([[1, 2], [2, 1], [3, 4], [5, 6]]))
# print(s.numEquivDominoPairs([[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]]))