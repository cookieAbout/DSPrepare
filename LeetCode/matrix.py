import heapq
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        https://leetcode.com/problems/set-matrix-zeroes/description/
        Do not return anything, modify matrix in-place instead.
        m == matrix.length
        n == matrix[0].length
        1 <= m, n <= 200
        -231 <= matrix[i][j] <= 231 - 1
        """

        def get_indices(array: List[int]) -> List[int]:
            """Возвращаю список индексов с 0 в строке"""
            return [i for i in range(len(array)) if array[i] == 0]

        zero_array = [0] * len(matrix[0])
        zero_column = []
        for idx, row in enumerate(matrix):
            if 0 in row:
                zero_column.extend(get_indices(row))
                matrix[idx] = zero_array

        for cl_idx in zero_column:
            for row in matrix:
                row[cl_idx] = 0
        print(matrix)

    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        """
        https://leetcode.com/problems/find-minimum-time-to-reach-last-room-i/description
        2 <= n == moveTime.length <= 50
        2 <= m == moveTime[i].length <= 50
        0 <= moveTime[i][j] <= 109
        """
        # Дейкстра
        n, m = len(moveTime), len(moveTime[0])
        goal = (n - 1, m - 1)
        dist = [[float("inf")] * m for _ in range(n)]
        dist[0][0] = 0
        heap = [(0, 0, 0)]
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # направления перемещения

        while heap:
            cost, x, y = heapq.heappop(heap)
            if (x, y) == goal:
                return cost
            if cost > dist[x][y]:
                continue

            for dx, dy in dir:
                nx, ny = x + dx, y + dy  # смотрим координаты соседей
                if 0 <= nx < n and 0 <= ny < m:
                    new_cost = max(cost, moveTime[nx][ny]) + 1

                    if new_cost < dist[nx][ny]:
                        dist[nx][ny] = new_cost
                        heapq.heappush(heap, (new_cost, nx, ny))

        return -1


s = Solution()
s.setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
s.setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]])
s.setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 0, 1, 5]])
print(s.minTimeToReach([[0, 4], [4, 4]]))
print(s.minTimeToReach([[0, 0, 0], [0, 0, 0]]))
