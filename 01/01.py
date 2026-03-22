_ = int(input())
marks = list(map(int, input().split()))
answer = []
for i in marks:
    if i != 0:
        answer.append(i)
answer += [0] * marks.count(0)
print(*answer)