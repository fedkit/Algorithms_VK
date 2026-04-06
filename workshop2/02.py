def f(matrix, x):
    i, j = 0, len(matrix) - 1
    count = 0

    while i < len(matrix) and j >= 0:
        if matrix[i][j] <= x:
            count += j + 1
            i += 1
        else:
            j -= 1

    return count

def solver(matrix, k):
    n = len(matrix)
    left, right = matrix[0][0], matrix[n - 1][n - 1]
    answer = right

    while left <= right:
        middle = (left + right) // 2
        if f(matrix, middle) >= k:
            answer = middle
            right = middle - 1
        else:
            left = middle + 1

    return answer


assert solver([[1, 2, 3],
               [4, 6, 7],
               [5, 8, 9]], 5) == 5

assert solver([[1, 10],
               [22, 23]], 3) == 22

assert solver([[-999]], 1) == -999