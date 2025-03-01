def bubbleSort(arr):
    N = len(arr)
    for i in range(N-1):
        flag = False
        for j in range(N-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = True
        if not flag:
            break