import time

def generate_square(n):
    return set(i*i for i in range(1,n+1))

def create_adj(n, squares):
    adj = {i: [] for i in range(1,n+1)}
    for i in range(1,n+1):
        for j in range(i+1,n+1):
            if i+j in squares:
                adj[i].append(j)
                adj[j].append(i)
    return adj

def square_sum(n):
    sq = generate_square(n)
    adj = create_adj(n, sq)
    paths = []

    def dfs(i, path):
        if len(visited) == n:
            paths.append(path)
            return True
        if i in visited:
            return False

        visited.add(i)
        
        for j in adj[i]:
            dfs(j, path+[i])
            
        visited.remove(i)

    visited = set()
    for i in range(1, n+1):
        dfs(i, [])
    return paths
        

for i in range(100):
    t = time.time()
    a = square_sum(i+1)
    print(i+1, a[0] if a else [], time.time()-t)
