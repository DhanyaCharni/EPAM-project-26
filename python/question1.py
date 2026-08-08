N, K = map(int, input().split())

keys = [0] + list(map(int, input().split()))

tree = [[] for _ in range(N + 1)]


for _ in range(N - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

trusted_count = 0


def dfs(node, parent, current_xor):
    global trusted_count

   
    current_xor ^= keys[node]

    if current_xor >= K:
        trusted_count += 1

    
    for child in tree[node]:
        if child != parent:
            dfs(child, node, current_xor)

dfs(1, 0, 0)


print(trusted_count)
