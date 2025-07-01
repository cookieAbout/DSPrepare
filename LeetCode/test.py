class Solution:
    def possibleStringCount(self, word: str) -> int:
        """ https://leetcode.com/problems/find-the-original-typed-string-i/ """
        curr = word[0]
        cnt = 1
        for idx in range(1, len(word)):
            if word[idx] == curr:
                cnt += 1
            else:
                curr = word[idx]
        return cnt

s = Solution()
print(s.possibleStringCount('abbcccc'))
print(s.possibleStringCount('abcd'))
print(s.possibleStringCount('aaaa'))
print(s.possibleStringCount('ere'))
