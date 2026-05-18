bin_matrix = [list(map(int, input().split()))]

for i in range(1, len(bin_matrix[0])):
    s = list(map(int, input().split()))
    bin_matrix.append(s)

dist = [[-1] * len(bin_matrix) for _ in range(len(bin_matrix))]

queue = []
head = 0

for i in range(len(bin_matrix)):
    for j in range(len(bin_matrix[0])):
        if bin_matrix[i][j] == 0:
            dist[i][j] = 0
            queue.append((i, j))

while head < len(queue):
    x, y = queue[head]
    head += 1

    for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < len(bin_matrix) and 0 <= ny < len(bin_matrix[0]):
            if dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))

for i in dist:
    print(*i)
    