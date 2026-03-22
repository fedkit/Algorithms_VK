_ = int(input())
s = list(map(int, input().split()))
answer = -1
dct = {}
for i in s:
    if i not in dct:
        dct[i] = 1
    else:
        dct[i] += 1
        
for i in dct:
    if dct[i] > len(s) // 2:
        answer = i 
print(answer)