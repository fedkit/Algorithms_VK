_ = int(input())
s = list(map(int, input().split()))
answer = -1
for i in range(len(s)):
    if s[i] % 2 == 0:
        answer = s[i]
print(answer)