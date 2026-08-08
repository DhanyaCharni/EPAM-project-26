from collections import deque

N, M, D = map(int, input().split())

graph = [[] for _ in range(N + 1)]


for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

distance = [-1] * (N + 1)


queue = deque()
queue.append(1)
distance[1] = 0

while queue:
    city = queue.popleft()

    for neighbor in graph[city]:
        if distance[neighbor] == -1:
            distance[neighbor] = distance[city] + 1
            queue.append(neighbor)

count = 0
for i in range(1, N + 1):
    if distance[i] != -1 and distance[i] <= D:
        count += 1

print(count)