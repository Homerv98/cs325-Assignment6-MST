# Homero
# MST implementation
# Bridge Builder

def connect_bridges(G):
    n = len(G)

    if n == 0:
        return []

    visited = [False] * n
    visited[0] = True

    mst = []

    # An MST has n - 1 edges
    while len(mst) < n - 1:
        min_cost = float('inf')
        start = -1
        end = -1

        # Check all visited islands
        for i in range(n):
            if visited[i]:

                # Find bridges to unvisited islands
                for j in range(n):
                    if (not visited[j] and
                            G[i][j] != 0 and
                            G[i][j] < min_cost):

                        min_cost = G[i][j]
                        start = i
                        end = j

        # No bridge found: graph is disconnected
        if end == -1:
            return []

        # Add the cheapest bridge to the MST
        mst.append((start, end, min_cost))
        visited[end] = True

    return mst


G = [
  [0, 8, 5, 0, 0, 0, 0],
  [8, 0, 10, 2, 18, 0, 0],
  [5, 10, 0, 3, 0, 16, 0],
  [0, 2, 3, 0, 12, 30, 14],
  [0, 18, 0, 12, 0, 0, 4],
  [0, 0, 16, 30, 0, 0, 26],
  [0, 0, 0, 14, 4, 26, 0]
]

print(connect_bridges(G))