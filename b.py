N, X, Y, Z = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

passed = []

for i in range(X):
    val = max(A)
    idx = A.index(val)
    passed.append(idx + 1)
    A[idx] = -1
    B[idx] = -1


for i in range(Y):
    val = max(B)
    idx = B.index(val)
    passed.append(idx + 1)
    A[idx] = -1
    B[idx] = -1

C = [A[i]+B[i] for i in range(N)]
for i in range(Z):
    val = max(C)
    idx = C.index(val)
    passed.append(idx + 1)
    C[idx] = -1

passed.sort()

for i in range(len(passed)):
    print(passed[i])