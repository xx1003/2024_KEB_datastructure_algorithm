# graph = [
#     [0, 1, 0, 1, 0],
#     [1, 0, 1, 1, 0],
#     [0, 1, 0, 0, 1],
#     [1, 1, 0, 0, 1],
#     [0, 0, 1, 1, 0]
# ]

graph = [
    [0, 1, 1, 0, 0, 0],
    [1, 0, 0, 1, 0, 0],
    [1, 0, 0, 1, 0, 0],
    [0, 1, 1, 0, 1, 1],
    [0, 0, 0, 1, 0, 1],
    [0, 0, 0, 1, 1, 0]
]


def dfs(g, i, visited):
    visited[i] = 1
    print(chr(ord('A')+i), end=' ')
    for j in range(len(g)):
        if g[i][j] == 1 and visited[j] == 0:
            dfs(g, j, visited)


visited = [0] * len(graph)
dfs(graph,0, visited)

