N = input().split()
d1 = int(N[0])
d2 = int(N[1])
data = input().split()

rev_data = data[::-1]
for i in range(d1 - d2, d1):
    print(rev_data[i], end=' ')