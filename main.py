import sys
from math import floor

list_qs = [234, 23434234, 234234, 12341234, 1234, 123443, 6345756, 876, 2357, 46, 71, 348, 24556513, 73667, 234, 781,
           346128, 12, 23, 46]

# list_hs = [234, 23434234, 234234, 12341234, 1234, 123443, 6345756, 876, 2357, 46, 71, 348, 24556513, 73667, 234, 781,
#            346128, 12, 23, 46]

list_hs = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]


def recursive_digit_sum(digit):
    # print(f"recursive_digit_sum({digit})")
    lenn = len(str(digit))
    if lenn == 2:
        # print(f"# if lenn == 2: recursive_digit_sum({int(str(digit)[0])}) + ({int(str(digit)[-1])})")
        return recursive_digit_sum(int(str(digit)[0])) + (int(str(digit)[-1]))
    elif lenn == 1:
        # print(f"# elif lenn == 1: {str(digit)[0]}")
        return int(str(digit)[0])
    else:
        # print(f"# else: recursive_digit_sum({digit // 10}) + ({int(str(digit)[-1])})")
        return recursive_digit_sum(digit // 10) + (int(str(digit)[-1]))


# Быстрая сортировка
def quicksort(i: int, j: int):
    # print(f"# quicksort({i}, {j})")
    pivotindex = findpivot(i, j)
    # print(f"# i = findpivot({i}, {j}) = {pivotindex}")
    if pivotindex != -1:
        pivot = list_qs[pivotindex]
        # print(f" pivot = lst[{pivotindex}] = {pivot}")
        k = partition(i, j, pivot)
        # print(f" k = partition({i}, {j}, {pivot}) = {k}")
        quicksort(i, k - 1)
        quicksort(k, j)


def findpivot(i: int, j: int):
    firstkey = list_qs[i]
    for k in range(i + 1, j):
        if recursive_digit_sum(list_qs[k]) > recursive_digit_sum(firstkey):
            return k
        elif recursive_digit_sum(list_qs[k]) < recursive_digit_sum(firstkey):
            return i
    return -1


def partition(i: int, j: int, pivot: int):
    left = i
    right = j
    while left <= right:
        while recursive_digit_sum(list_qs[left]) >= recursive_digit_sum(pivot):
            left += 1
        while recursive_digit_sum(list_qs[right]) < recursive_digit_sum(pivot):
            right -= 1
        if left < right:
            temp = list_qs[right]
            list_qs[right] = list_qs[left]
            list_qs[left] = temp
    return left


# Пирамидальная сортировка
def heapsort():
    n = len(list_hs) - 1
    for i in range(floor(n / 2), 1, -1):
        print(f"# (i = {i})")
        pushdown(i, n)
    for i in range(n, 2, -1):
        list_hs[1], list_hs[i] = list_hs[i], list_hs[1]
        pushdown(1, i - 1)


def pushdown(first: int, last: int):
    print(f"# pushdown({first}, {last})")
    r = first
    print(f"# r={r}")
    print(f"# r <= last / 2 = {r <= last / 2}")
    while r <= last / 2:
        if last == 2 * r:
            if list_hs[r] > list_hs[2 * r]:
                list_hs[r], list_hs[2 * r] = list_hs[2 * r], list_hs[r]
            r = last
        elif list_hs[r] > list_hs[2 * r] and list_hs[2 * r] <= list_hs[2 * r + 1]:
            list_hs[r], list_hs[2 * r] = list_hs[2 * r], list_hs[r]
            r = 2 * r
        elif list_hs[r] > list_hs[2 * r + 1] and list_hs[2 * r + 1] <= list_hs[2 * r]:
            list_hs[r], list_hs[2 * r + 1] = list_hs[2 * r + 1], list_hs[r]
            r = 2 * r + 1
        else:
            r = last


# quicksort(0, 19)
# print(list_qs)
heapsort()
print(list_hs)
