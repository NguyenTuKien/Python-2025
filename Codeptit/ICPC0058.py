from sys import stdin


def dfs(adj, used, cur, tar, ban):
    used[cur] = True
    if cur == tar :
        return True
    for next in adj[cur]:
        if next == ban and next != tar:
            continue
        if not used[next]:
            if dfs(adj, used, next, tar, ban):
                return True
    return False

def main():
    data = stdin.buffer.read().split()
    it = iter(data)

    for _ in range(int(next(it))):
        n, m, u, v, c = int(next(it)), int(next(it)), int(next(it)), int(next(it)), 0
        adj = [[] for _ in range(n + 1)]
        used = [False] * (n + 1)
        for _ in range(m):
            x, y = int(next(it)), int(next(it))
            adj[x].append(y)
        if not dfs(adj, used, u, v, -1):
            print(0)
        else :
            for i in range(1, n + 1):
                used = [False] * (n + 1)
                if not dfs(adj, used, u, v, i) : 
                    c += 1
                    # print(i, end='')
            print(c)

if __name__ == "__main__":
    main()
