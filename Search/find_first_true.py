def find_boundary(arr: list[bool]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    left, right = 0, len(arr) - 1
    boundary = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid]:
            boundary = mid
            right = mid - 1
        else:
            left = mid + 1
    return boundary

    
if __name__ == "__main__":
    arr = [False, False, True, True, True]
    res = find_boundary(arr)
    print(res)
