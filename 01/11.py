_ = int(input())
s = list(map(int, input().split()))
k = int(input())

s.sort()

n = len(s)

if s[-1] <= 0 and k % 2 == 1:
    answer = 1
    for i in range(n - 1, n - k - 1, -1):
        answer *= s[i]
    print(answer)
    exit()

left = 0
right = n - 1
answer = 1

if k % 2 == 1:
    answer *= s[right]
    right -= 1
    k -= 1

while k > 0:
    left_dop = s[left] * s[left + 1]
    right_dop = s[right] * s[right - 1]

    if left_dop > right_dop:
        answer *= left_dop
        left += 2
    else:
        answer *= right_dop
        right -= 2

    k -= 2

print(answer)