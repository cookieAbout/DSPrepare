"""Модуль задач с массивами"""

import heapq
from typing import List
from itertools import combinations, permutations


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        https://leetcode.com/problems/two-sum/
        2 <= nums.length <= 104
        -109 <= nums[i] <= 109
        -109 <= target <= 109
        """
        if len(nums) == 2:
            return [0, 1]

        res_list = [x for x in combinations(nums, r=2) if x[0] + x[1] == target]
        return [i for i, val in enumerate(nums) if val in res_list[0]]

    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        """
        https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i
        1 <= n == words.length == groups.length <= 100
        1 <= words[i].length <= 10
        groups[i] is either 0 or 1.
        words consists of distinct strings.
        words[i] consists of lowercase English letters.
        """
        cnt = 0
        for i in range(1, len(groups)):
            if groups[i] == groups[i - 1]:
                words.pop(i - cnt)
                cnt += 1
        return words

    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        https://leetcode.com/problems/subarray-sum-equals-k/
        1 <= nums.length <= 2 * 104
        -1000 <= nums[i] <= 1000
        -107 <= k <= 107
        """
        cnt, curr_sum = 0, 0
        d = {0: 1}

        for i in range(len(nums)):
            curr_sum += nums[i]
            cnt += d.get(curr_sum - k, 0)
            d[curr_sum] = d.get(curr_sum, 0) + 1

        return cnt

    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        """
        https://leetcode.com/problems/subarray-sums-divisible-by-k/
        sum(i,j) = prefix[j] − prefix[i−1]
        (prefix[j] − prefix[i−1]) mod k = 0
        prefix[j] mod k = prefix[i−1] mod k
        """
        cnt, curr_sum = 0, 0
        # частота появления остатка
        mod_count = {
            0: 1
        }  # Начинаем с mod_count[0] = 1, потому что пустая сумма — это 0, и она делится на любое k.

        for i in range(len(nums)):
            curr_sum += nums[i]
            mod = curr_sum % k
            if mod < 0:
                mod = (mod + k) % k
            cnt += mod_count.get(mod, 0)
            mod_count[mod] = mod_count.get(mod, 0) + 1

        return cnt

    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        https://leetcode.com/problems/search-insert-position/submissions/1614500571/
        1 <= nums.length <= 104
        -104 <= nums[i] <= 104
        nums contains distinct values sorted in ascending order.
        -104 <= target <= 104
        """
        try:
            return nums.index(target)
        except ValueError:
            if target >= nums[-1]:
                return len(nums)
            else:
                i = 0
                while i < len(nums):
                    if nums[i] <= target:
                        i += 1
                    else:
                        return i

    def countSubarrays(self, nums: List[int]) -> int:
        """
        https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition/description/
        3 <= nums.length <= 100
        -100 <= nums[i] <= 100
        """
        ln = len(nums)
        return sum(
            [
                (nums[i] + nums[i + 2]) * 2 == nums[i + 1]
                for i in range(ln)
                if i + 2 < ln
            ]
        )

    def removeDuplicates(self, nums: List[int]) -> int:
        """
        https://leetcode.com/problems/remove-duplicates-from-sorted-array/
        1 <= nums.length <= 3 * 104
        -100 <= nums[i] <= 100
        nums is sorted in non-decreasing order.
        """
        # return len(list(set(nums)))
        i, j = 0, 1
        while i <= j < len(nums):
            if nums[i] == nums[j]:
                j += 1
            else:
                i += 1
                nums[i] = nums[j]
        # print(nums)
        return i + 1

    def removeElement(self, nums: List[int], val: int) -> int:
        """
        https://leetcode.com/problems/remove-element/
        0 <= nums.length <= 100
        0 <= nums[i] <= 50
        0 <= val <= 100
        """
        l = len(nums)
        i, j = 0, 1
        cnt_in = nums.count(val)

        if cnt_in == 0:
            return l
        elif l == 1:
            nums.remove(val)
            return 0

        while i <= j < l:
            if nums[i] == val:
                for _i in range(j, l):
                    if nums[_i] != val:
                        nums[i], nums[_i] = nums[_i], nums[i]
                        break
                j = i + 1
            else:
                j += 1
            i += 1

        return nums.index(val)

    def plusOne(self, digits: List[int]) -> List[int]:
        """
        https://leetcode.com/problems/plus-one/description/
        1 <= digits.length <= 100
        0 <= digits[i] <= 9
        """
        return [int(res) for res in str(int("".join([str(i) for i in digits])) + 1)]

    def findNumbers(self, nums: List[int]) -> int:
        """https://leetcode.com/problems/find-numbers-with-even-number-of-digits/description/"""
        return sum([len(str(n)) % 2 == 0 for n in nums])

    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        """
        https://leetcode.com/problems/count-good-triplets/description/
        3 <= arr.length <= 100
        0 <= arr[i] <= 1000
        0 <= a, b, c <= 1000
        """
        res_list = []
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                for k in range(j + 1, len(arr)):
                    if (
                        abs(arr[i] - arr[j]) <= a
                        and abs(arr[j] - arr[k]) <= b
                        and abs(arr[i] - arr[k]) <= c
                    ):
                        res_list.append((arr[i], arr[j], arr[k]))
        return len(res_list)

    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        """
        https://leetcode.com/problems/three-consecutive-odds
        1 <= arr.length <= 1000
        1 <= arr[i] <= 1000
        """
        if len(arr) < 3:
            return False
        cnt = 0
        for i, v in enumerate(arr):
            if v % 2 == 0:
                cnt = 0
                continue
            cnt += 1
            if cnt == 3:
                return True
        return False

    def buildArray(self, nums: List[int]) -> List[int]:
        """
        https://leetcode.com/problems/build-array-from-permutation/
        1 <= nums.length <= 1000
        0 <= nums[i] < nums.length
        The elements in nums are distinct.
        """
        return [nums[nums[i]] for i in range(len(nums))]  # быстрее
        # return [nums[val] for i, val in enumerate(nums)]

    def countPairs(self, nums: List[int], k: int) -> int:
        """
        https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/description/
        1 <= nums.length <= 100
        1 <= nums[i], k <= 100
        """
        # print(dict(enumerate(nums)), dict(enumerate(nums[1:], start=1)))
        return sum(
            nums[i] == nums[j] and (i * j) % k == 0
            for i in range(len(nums))
            for j in range(i + 1, len(nums))
        )

    def totalNumbers(self, digits: List[int]) -> int:
        """
        https://leetcode.com/problems/unique-3-digit-even-numbers/description/
        Определить количество четных трехзначных чисел, которые можно составить из массива
        Каждая копия цифры может использоваться только один раз для каждого числа, и начальных нулей быть не может
        По списку четных чисел проверяем, возможно ли вообще собрать четные трехзначные числа
        :param digits:
        :return:
        """
        even_nums = [i for i in set(digits) if i % 2 == 0]
        if len(digits) < 3 or len(even_nums) == 0:
            return 0

        nums_res = set()
        for a, b, c in permutations(digits, 3):
            if a != 0 and c in even_nums:
                nums_res.add((a, b, c))
        return len(nums_res)

    def maxSum(self, nums: List[int]) -> int:
        """
        https://leetcode.com/contest/weekly-contest-441/problems/maximum-unique-subarray-sum-after-deletion/
        Все элементы в подмассиве были уникальны.
        Сумма элементов в подмассиве была максимальна.
        """
        max_num = max(nums)
        if max_num < 0:
            return max_num
        return sum([num for num in set(nums) if num > 0])

    def triangleType(self, nums: List[int]) -> str:
        """
        https://leetcode.com/problems/type-of-triangle/description/
        nums.length == 3
        1 <= nums[i] <= 100
        """
        nums = sorted(nums)
        f_side, s_side, th_side = nums[0], nums[1], nums[2]
        if f_side == s_side == th_side:
            return "equilateral"
        else:
            if (
                f_side + s_side > th_side
                and f_side + th_side > s_side
                and s_side + th_side > f_side
            ):
                return (
                    "isosceles" if f_side == s_side or s_side == th_side else "scalene"
                )
            return "none"


s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))
print(s.twoSum([3, 2, 4], 6))
print(s.getLongestSubsequence(["tu", "rv", "bn"], [0, 0, 0]))
print(s.getLongestSubsequence(["e", "a", "b"], [0, 0, 1]))
print(s.getLongestSubsequence(["c"], [0]))
print(s.getLongestSubsequence(["c", "f", "y", "i"], [1, 0, 1, 1]))
# print(s.countInterestingSubarrays([3, 2, 4], 2, 1))  # [3], [3, 2], [3, 2, 4]
# print(s.countInterestingSubarrays([3, 1, 9, 6], 3, 0))
# print(s.subarraySum([1, 1, 1], 2))  # 2 [[0, 1], [1, 2]] - по индексам
# print(s.subarraySum([1, 2, 3], 3))  # 2 [[0, 1], [2]]
# print(s.subarraysDivByK([4, 5, 0, -2, -3, 1], 5))
# print(s.subarraysDivByK([5], 9))
print(s.searchInsert([1, 3, 5, 6], 5))
print(s.searchInsert([1, 3, 5], 4))
print(s.countSubarrays([1, 2, 1, 4, 1]))
print(s.countSubarrays([1, 1, 1]))
print(s.countSubarrays([8, -10, -4]))
print(s.removeDuplicates([1, 1, 2]))
print(s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
print(s.removeElement([3, 3], 5))
print(s.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
# print(s.plusOne([4, 3, 2, 1]))
# print(s.plusOne([9]))
print(s.findNumbers([12, 345, 2, 6, 7896]))
print(s.countGoodTriplets([3, 0, 1, 1, 9, 7], 7, 2, 3))
print(s.countGoodTriplets([1, 1, 2, 2, 3], 0, 0, 1))
print(s.threeConsecutiveOdds([2, 6, 4, 1]))
print(s.threeConsecutiveOdds([1, 2, 34, 3, 4, 5, 7, 23, 12]))
print(s.buildArray([0, 2, 1, 5, 3, 4]))  # [0,1,2,4,5,3]
print(s.buildArray([5, 0, 1, 2, 3, 4]))  # [4,5,0,1,2,3]
print(s.countPairs([3, 1, 2, 2, 2, 1, 3], 2))
print(s.countPairs([1, 2, 3, 4], 1))
print(s.totalNumbers([1, 2, 3, 4]))
print(s.totalNumbers([0, 2, 2]))
print(s.maxSum([1, 2, 3, 4, 5]))  # 15
print(s.maxSum([1, 0, 1, 1]))  # 1
print(s.triangleType([3, 3, 3]))  # equilateral
print(s.triangleType([3, 4, 5]))  # scalene
print(s.triangleType([3, 3, 5]))  # isosceles
print(s.triangleType([8, 4, 4]))  # none
