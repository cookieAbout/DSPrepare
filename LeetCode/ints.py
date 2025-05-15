""" Числовые задачи """


class Solution:

    def numTilings(self, n: int) -> int:
        """
        https://leetcode.com/problems/domino-and-tromino-tiling/
        1 <= n <= 1000
        """
        if n == 1:
            return 1
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] * 2 + dp[i - 3]
        return dp[n] % 1000000007

    def isPalindrome(self, x: int) -> bool:
        """ https://leetcode.com/problems/palindrome-number/description/ """
        return str(x) == str(x)[::-1]

    def countSymmetricIntegers(self, low: int, high: int) -> int:
        """
        https://leetcode.com/problems/count-symmetric-integers/description/
        1 <= low <= high <= 104
        """
        count_symmetric_int = 0
        for int_for_check in range(low, high + 1):
            str_int = str(int_for_check)
            len_s = len(str_int)
            if len_s % 2 == 0 and (
                    sum([int(f) for f in str_int[:int(len_s / 2)]]) == sum([int(f) for f in str_int[int(len_s / 2):]])
            ):
                count_symmetric_int += 1

        return count_symmetric_int

    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        """ https://leetcode.com/problems/maximum-containers-on-a-ship/description/ """
        max_count_by_weighs = int(maxWeight / w)
        container_count = n * n

        return max_count_by_weighs if max_count_by_weighs < container_count else container_count


s = Solution()
print(s.numTilings(3))   # 5
# print(s.numTilings(99))  # 337638801  4698828092747101051698088766615493
print(s.isPalindrome(121))
print(s.isPalindrome(123))
print(s.countSymmetricIntegers(1, 100))
print(s.countSymmetricIntegers(1200, 1230))
print(s.maxContainers(2, 3, 15))
print(s.maxContainers(3, 5, 20))
