n = int(input())
arr = list(map(int, input().split()))

q = int(input())

for _ in range(q):
    x = int(input())

    low, high = 0, n - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == x:
            print(mid + 1)   # 1-based rank
            break
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
