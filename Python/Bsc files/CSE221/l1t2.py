T = int(input())
data = []

for i in range(T):
    temp = input().split()
    data.append(temp)
for j in range(T):
    task = data[j][2]
    n1 = float(data[j][1])
    n2 = float(data[j][3])
    if task == '+':
        result = n1 + n2
    elif task == '-':
        result = n1 - n2
    elif task == '*':
        result = n1 * n2
    elif task == '/':
        result = n1 / n2    
    print(f"{result:.6f}")