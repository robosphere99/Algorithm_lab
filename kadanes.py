def max_subarray(arr):
    max_so_far = float('-inf') 
    max_ending_here = 0  
    start = 0  
    end = 0  
    s = 0  

    for i in range(len(arr)):
        max_ending_here += arr[i] 

        if max_so_far < max_ending_here:  
            max_so_far = max_ending_here  
            start = s 
            end = i  

        if max_ending_here < 0:
            max_ending_here = 0  
            s = i + 1 

    return arr[start:end+1], max_so_far 

arr = [-2,-5,5,3,1,-2,4,-1]
subarray, max_sum = max_subarray(arr)
print(f"The subarray with the maximum sum is {subarray} and the sum is {max_sum}")