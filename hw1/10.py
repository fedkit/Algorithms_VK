s = input()
answer, count = '', -1
dct = {}

for i in s:
    if i not in dct:
        dct[i] = 1
    else:
        dct[i] += 1

for i in dct:
    if dct[i] > count:
        answer = i
        count = dct[i]
print(count)