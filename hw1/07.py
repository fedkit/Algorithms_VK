_ = int(input())
s = list(map(int, input().split()))
target = int(input())

if s == '':
    print(0, 0)
    exit()
    
n = len(s)

if n == 0:
    print(0, 0)
else:
    if target <= s[0]:
        print(0, 0)
    else:
        p = 1
        while p < n and s[p] < target:
            p *= 2

        left = p // 2
        right = min(p, n - 1)

        print(left, right)