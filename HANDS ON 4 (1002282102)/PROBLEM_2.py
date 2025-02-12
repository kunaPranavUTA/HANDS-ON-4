def remove_duplicates(arr):
    if not arr:
        return []
    j = 0
    for i in range(1, len(arr)):
        if arr[i] != arr[j]:
            j += 1
            arr[j] = arr[i]
            
    return arr[:j + 1]
arr1 = [2,2,2,2,2]
arr2 = [1,2,2,3,4,4,4,5,5]
print(remove_duplicates(arr1))
print(remove_duplicates(arr2))