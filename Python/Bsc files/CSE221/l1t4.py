T = int(input())
data = []
for i in range(T):
    N = int(input())
    data.append(N * (N + 1) // 2)
for k in data:
    print(k)