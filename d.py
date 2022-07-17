import numpy as np
N, K = map(int, input().split())
P = list(map(int, input().split()))

ans = np.zeros(N, dtype=int)

for i in range(N):
    mount = [P[i]]
    idx = [i]
    for t in range(i+1, N+1):
        if len(mount) == K:
            for j in range(len(mount)):
                ans[mount[j]-1] = t
                P[idx[j]] = 1000000
            break
        elif t == N:
            break
        elif P[t] == 1000000:
            continue
        elif P[t] <  mount[-1]:
            mount.append(P[t])
            idx.append(t)

for i in range(N):
    if ans[i] == 0:
        print(-1)
    else:
        print(ans[i])

print(P)
print(ans)


    
