def search_sorted_array(array, val):
    if array is None or val is None:
        raise TypeError('array or val cannot be None')
    if not array:
        return None
    return _search_sorted_array(array, val, start=0, end=len(array) - 1)


def _search_sorted_array(array, val, start, end):
    if end < start:
        return None
    mid = (start + end) // 2
    if array[mid] == val:
        return mid
    # Left side is sorted
    if array[start] < array[mid]:
        if array[start] <= val < array[mid]:
            return _search_sorted_array(array, val, start, mid - 1)
        else:
            return _search_sorted_array(array, val, mid + 1, end)
    # Right side is sorted
    elif array[start] > array[mid]:
        if array[mid] < val <= array[end]:
            return _search_sorted_array(array, val, mid + 1, end)
        else:
            return _search_sorted_array(array, val, start, mid - 1)
    # Duplicates
    else:
        if array[mid] != array[end]:
            return _search_sorted_array(array, val, mid + 1, end)
        else:
            result = _search_sorted_array(array, val, start, mid - 1)
            if result != None:
                return result
            else:
                return _search_sorted_array(array, val, mid + 1, end)