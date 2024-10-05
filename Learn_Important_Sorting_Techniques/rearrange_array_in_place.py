def rearrange_array_in_place(arr):
    # Rearrange the array, keeping the original order, but moving negatives first
    i = 0
    for j in range(len(arr)):
        if arr[j] < 0:
            # Swap the negative element with the element at index i
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    return arr

# Example usage
input_array = [5, 4, 7, -2, -4, -1, 20]
rearranged_array = rearrange_array_in_place(input_array)
print(rearranged_array)
