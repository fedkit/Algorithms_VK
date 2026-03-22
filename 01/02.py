_ = int(input())
measurements = list(map(int, input().split()))
element = int(input())
answer = []
for i in measurements:
    if i != element:
        answer.append(i)
print(*answer)