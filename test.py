# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
#
# def solution(A):
#     # write your code in Python 3.6
#     min_pos = 1
#     A.sort()
#
#     for val in A:
#         if val > min_pos:
#             return min_pos
#         elif val == min_pos:
#             min_pos += 1
#
#     return min_pos


def solution(A):
    # write your code in Python 3.6
    min_n = min(A)
    min_n = 1 if min_n < 1 else min_n
    max_n = max(A)

    if max_n < 1 or min_n > 1:
        return 1

    s = set(A)

    for num in range(min_n, max_n):
        if num not in s:
            return num

    return max_n + 1


print(solution([1, 3, 4, 5, 6, 2]))
print(solution([3, 6, 7, 4]))
print(solution([3, 6, 7, -1]))
print(solution([-1, 100, -120, -120, 1, 2]))

