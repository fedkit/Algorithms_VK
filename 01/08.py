def quick_sort(s):
    if len(s) <= 1:
        return s
    t = s[0]
    l = quick_sort([i for i in s if i < t])
    c = quick_sort([i for i in s if i == t])
    r = quick_sort([i for i in s if i > t])

    return l + c + r

_ = int(input())
s = list(map(int, input().split()))

print(*quick_sort(s))