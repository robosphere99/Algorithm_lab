def bubble_sort(arr) :
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
arr = [3,5,2,7,1,9,12,20,0,-5]
bubble_sort(arr)
print(arr)
