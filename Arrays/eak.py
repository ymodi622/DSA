def find_peak_position(arr):
    # Handle edge cases
    if not arr:
        return -1
    if len(arr) == 1:
        return 1
    
    low = 0
    high = len(arr) - 1
    
    # If array is strictly increasing, return first position
    mid = (low + high) // 2
    if arr[low] < arr[mid] and arr[mid] < arr[high]:
        return 1
    
    res = -1
    while low <= high:
        mid = (low + high) // 2
        print(arr[low], arr[mid], arr[high])
        
        # If strictly increasing in this segment
        if arr[low] < arr[mid] and arr[mid] < arr[high]:
            res = arr[high]
            break
        # If peak is in left half
        elif arr[low] > arr[mid] and arr[low] > arr[high]:
            res = max(res, arr[low])
            high = mid - 1
        # If peak is in right half
        elif arr[low] < arr[mid] and arr[mid] > arr[high]:
            res = max(res, arr[mid])
            low = mid + 1
    
    # Return 1-based index of peak element
    return arr.index(res) + 1 if res != -1 else -1

# Test cases
print(find_peak_position([1, 2, 3]))  # Should return 1 for strictly increasing
print(find_peak_position([3, 2, 1]))  # Should handle decreasing
print(find_peak_position([1, 3, 2]))  # Should find peak at 3