def search_sorted_array(array, val, start, end):
    if array is None or val is None:
        return('array or val cannot be None')
    if not array:
        return None
    if end < start:
        return None
    mid = (start + end) // 2
    if array[mid] == val:
        return mid
    # Left side is sorted
    if array[start] < array[mid]:
        if array[start] <= val < array[mid]:
            return search_sorted_array(array, val, start, mid - 1)
        else:
            return search_sorted_array(array, val, mid + 1, end)
        # Right side is sorted
    elif array[start] > array[mid]:
        if array[mid] < val <= array[end]:
            return search_sorted_array(array, val, mid + 1, end)
        else:
            return search_sorted_array(array, val, start, mid - 1)
        # Duplicates
    else:
        if array[mid] != array[end]:
            return search_sorted_array(array, val, mid + 1, end)
        else:
            result = search_sorted_array(array, val, start, mid - 1)
            if result != None:
                return result
            else:
                return search_sorted_array(array, val, mid + 1, end)

a= [1,2,3,4,5] 
print(search_sorted_array(a,3,1,5))