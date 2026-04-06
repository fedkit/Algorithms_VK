_ = int(input())
s = list(map(int, input().split()))
min_diff, current_diff = None, None
answer1, answer2 = None, None
for i in range(1, len(s)):
    if min_diff is None:
        min_diff = abs(s[i-1] - s[i])
        answer1, answer2 = s[i-1], s[i]
    current_diff = abs(s[i-1] - s[i])
    if current_diff < min_diff:
        min_diff = abs(s[i-1] - s[i])
        answer1, answer2 = s[i-1], s[i]
print(answer1, answer2)
