"""Модуль задач со строками"""

from string import ascii_lowercase
from itertools import groupby
from typing import List


class Solution:
    def romanToInt(self, s: str) -> int:
        rome_to_int = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        lens = len(s)
        if lens == 1:
            return rome_to_int[s]

        res_num, rome = 0, 0
        while rome < lens:
            rome_key_val = rome_to_int[s[rome]]
            if rome + 1 < lens and rome_key_val < rome_to_int[s[rome + 1]]:
                res_num += rome_to_int[s[rome + 1]] - rome_key_val
                rome += 2
            else:
                res_num += rome_key_val
                rome += 1
        return res_num

    def strStr(self, haystack: str, needle: str) -> int:
        """
        https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
        1 <= haystack.length, needle.length <= 104
        haystack and needle consist of only lowercase English characters
        """
        try:
            return haystack.index(needle)
        except ValueError:
            return -1

    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        https://leetcode.com/problems/longest-common-prefix/description/
        1 <= strs.length <= 200
        0 <= strs[i].length <= 200
        strs[i] consists of only lowercase English letters if it is non-empty.
        """
        shortest = min(strs, key=len)
        if len(strs) < 1:
            return ""

        for word in strs:
            while not word.startswith(shortest):
                shortest = shortest[:-1]
        return shortest

    def isValid(self, s: str) -> bool:
        """
        https://leetcode.com/problems/valid-parentheses/description/
        1 <= s.length <= 104
        :param s:  consists of parentheses only '()[]{}'.
        :return: is right order
        """
        len_s = len(s)
        if len_s % 2 > 0:
            return False

        par_dict = {
            "(": ")",
            "{": "}",
            "[": "]",
        }

        pars = []
        for par in s:
            if par in par_dict:
                pars.append(par)
            elif len(pars) == 0 or par_dict[pars.pop()] != par:
                return False
        return len(pars) == 0

    def lengthOfLastWord(self, s: str) -> int:
        """
        https://leetcode.com/problems/length-of-last-word/description/
        1 <= s.length <= 104
        s consists of only English letters and spaces ' '.
        There will be at least one word in s.
        """
        trim_s = s.strip()
        return trim_s[::-1].index(" ") if " " in trim_s else len(trim_s)

    def addBinary(self, a: str, b: str) -> str:
        """
        https://leetcode.com/problems/add-binary/description/
        1 <= a.length, b.length <= 104
        a and b consist only of '0' or '1' characters.
        Each string does not contain leading zeros except for the zero itself.
        """
        return "{0:b}".format(int(a, 2) + int(b, 2))

    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        """
        https://leetcode.com/contest/weekly-contest-437/problems/find-special-substring-of-length-k/
        1 <= k <= s.length <= 100
        s consists of lowercase English letters only.
        """
        if k == 1 and len(s) == 1:
            return True

        for group_key, group_val in groupby(s):
            res = list(group_val)
            if len(res) == k:
                return len(res) == k
        return False

    def reverseDegree(self, s: str) -> int:
        """https://leetcode.com/problems/reverse-degree-of-a-string/description/"""
        res = 0
        for sch in range(len(s)):
            res += abs(ascii_lowercase.index(s[sch]) - 26) * (sch + 1)
        return res

    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        """https://leetcode.com/problems/find-words-containing-character/"""
        # return [idx for idx, val in enumerate(words) if x in list(val)]  # Лучше по памяти
        return [
            idx for idx, val in enumerate(words) if val.find(x) != -1
        ]  # лучше по скорости


s = Solution()
print(s.romanToInt("III"))
print(s.romanToInt("LVIII"))
print(s.romanToInt("MCMXCIV"))
print(s.romanToInt("IV"))
# print(s.strStr('sadbutsad', 'sad'))
# print(s.strStr('leetcode', 'leeto'))
print(s.longestCommonPrefix(["flower", "flow", "flight"]))
print(s.longestCommonPrefix(["dog", "racecar", "car"]))
print(s.isValid("()[]{}"))
print(s.isValid("(]"))
print(s.lengthOfLastWord("Hello World"))
print(s.lengthOfLastWord("   fly me   to   the moon  "))
print(s.addBinary("11", "1"))
print(s.addBinary("1010", "1011"))
print(s.hasSpecialSubstring("abc", 2))
print(s.hasSpecialSubstring("aaabaaa", 3))
print(s.reverseDegree("abc"))
print(s.reverseDegree("zaza"))
print(s.findWordsContaining(["abc", "bcd", "aaaa", "cbc"], "a"))
print(s.findWordsContaining(["abc", "bcd", "aaaa", "cbc"], "Z"))
