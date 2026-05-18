numbers = list(map(int, input().split()))
tails = []

for i in numbers:
    left, right = 0, len(tails)
    while left < right:
        mid = (left + right) // 2
        if tails[mid] < i:
            left = mid + 1
        else:
            right = mid

    if left == len(tails):
        tails.append(i)
    else:
        tails[left] = i

print(len(tails))