from collections import defaultdict


def findKthNumber(m, n, k):
    st = 0
    for i in range(1, m + 1):
        if i * n < k:
            st += 1
            k -= n
        else:
            break
    st += 1
    k -= n
    tmpSt = st
    mul = 1
    print(k, st)
    while k > 0:
        k -= 1
        if k == 0:
            return st
        st += mul
        if st == m:
            mul += 1
            st = tmpSt * mul


# print(findKthNumber(2, 3, 6))
# print(findKthNumber(3, 3, 5))
# print(findKthNumber(3, 1, 3))
print(findKthNumber(4, 3, 9))
