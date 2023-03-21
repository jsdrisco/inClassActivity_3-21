
def remove_duplicates(arr):
    # Sort the input array
    # Create arrays that will contain unique elements, removed elements
    arr.sort()
    unique_arr = []
    removed_elements = []
    
    # Check if current element is identical to previous element
    # If unique, append to unique_arr, otherwise append to removed_elements
    for i in range(len(arr)):
        if i == 0 or arr[i] != arr[i-1]:
            unique_arr.append(arr[i])
        else:
            removed_elements.append(arr[i])
    return unique_arr, removed_elements

# Test the function
arr = [1, 2, 2, 3, 4, 4, 5]
unique_arr, removed_elements = remove_duplicates(arr)
print("Original array:", arr)
print("Unique array:", unique_arr)
print("Removed elements:", removed_elements)
