def solver(s):
    chars = set()
    answer = 0
    left, right = 0, 0

    while right < len(s):
        while s[right] in chars:
            chars.remove(s[left])
            left += 1
        chars.add(s[right])
        answer = max(answer, right - left + 1)
        right += 1

    return answer

assert solver('12345665') == 6
assert solver('') == 0
assert solver('kkkkkkkkkk') == 1
assert solver('nghrngrhwerturn') == 6
assert solver('2@2') == 2