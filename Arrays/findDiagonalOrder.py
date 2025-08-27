from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        m = len(mat[0])

        def goUp(r, c, cnt):
            while r != 0 or c != n - 1:
                res.append(mat[r][c])
                r -= 1
                c += 1
                cnt -= 1
            return r, c, cnt

        def goDown(r, c, cnt):
            while c != 0 or r != n - 1:
                res.append(mat[r][c])
                r += 1
                c -= 1
                cnt -= 1
            return r, c, cnt

        res = []
        cnt = n * m
        cRow, cCol = 0, 0

        while cnt > 0:
            cRow, cCOl, cnt = goUp(cRow, cCol, cnt)
            if cnt < 0:
                break
            if cRow == 0:
                cCol += 1
            elif cCol == n - 1:
                cRow += 1
            cRow, cCOl, cnt = goDown(cRow, cCol, cnt)
            if cCol == 0:
                cRow += 1
            elif cRow == n - 1:
                cCol += 1
        return res
