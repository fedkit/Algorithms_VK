_ = int(input())
s = list(map(int, input().split()))
target = int(input())
answer = len(s)
for i in range(len(s)):
    if s[i] == target:
        answer = i
        break
    if s[i] > target:
        answer = i 
        break
print(answer)