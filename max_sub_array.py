def max_crossing_sum(arr, low, mid, high):
   
    left_sum = float('-inf')
    total = 0
    for i in range(mid, low - 1, -1):
        total += arr[i]
        if total > left_sum:
            left_sum = total
    
    
    right_sum = float('-inf')
    total = 0
    for i in range(mid + 1, high + 1):
        total += arr[i]
        if total > right_sum:
            right_sum = total
    
    return left_sum + right_sum

def max_subarray_sum(arr, low, high):
    
    if low == high:
        return arr[low]
    
    mid = (low + high) // 2

    left_sum = max_subarray_sum(arr, low, mid)
    right_sum = max_subarray_sum(arr, mid + 1, high)
    cross_sum = max_crossing_sum(arr, low, mid, high)
    
    return max(left_sum, right_sum, cross_sum)

arr = [-2, -3, 4, -1, -2, 1, 5, -3]
max_sum = max_subarray_sum(arr, 0, len(arr) - 1)
print(f"Maximum sum: {max_sum}")
