T = int(input())
num = []
for i in range(T):
    temp = int(input())
    num.append(temp)
for j in range(T):
    if num[j]%2 == 0:
        print(f"{num[j]} is an Even number.")
    else:
        print(f" {num[j]} is an Odd number.")