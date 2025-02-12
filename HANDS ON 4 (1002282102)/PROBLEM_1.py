import heapq
def merge(arrays):
    min_heap = []
    result = []
    for i, arr in enumerate(arrays):
        if arr:
            heapq.heappush(min_heap,(arr[0],i,0))
            
    while min_heap:
        value , array_idx, element_idx = heapq.heappop(min_heap)
        result.append(value)
        if element_idx + 1 < len(arrays[array_idx]):
            next_value = arrays[array_idx][element_idx + 1]
            heapq.heappush(min_heap, (next_value, array_idx, element_idx + 1))
            
    return result
array1 = [[1,3,5,7],[2,4,6,8],[0,9,10,11]]
array2 = [ [1,3,7],[2,4,8],[9,10,11]]
print(merge(array1))
print(merge(array2))