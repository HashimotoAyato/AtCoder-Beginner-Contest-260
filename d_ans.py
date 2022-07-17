import numpy as np
from bisect import bisect

N, K = map(int, input().split())
P = list(map(int, input().split()))

stocks = []
tops = []
res = np.full(N, -1)

for i in range(N):
    idx = bisect(tops,P[i])
    
    if idx == len(tops):
        stocks.append([P[i]])
        tops.append(P[i])
    
    else:
        stocks[idx].append(P[i])
        tops[idx] = P[i]
    
    if len(stocks[idx]) == K:
        for j in stocks.pop(idx):
            res[j-1] = i + 1
        tops.pop(idx)
    
for i in range(len(res)):
    print(res[i])
