# Task 1
# Define binary search including low and high

def binary_search(target, items):
    low = 0  # Where the list should start
    high = len(items) - 1  # Where the list should end (-1 = end)

    # Perform a while loop which will continue as long as low is less than
    # or equal to high and until target is found or list is exhausted
    while low <= high:
        mid = (low + high) // 2  # Calculate the mid index point (low + high and divide by 2)
        guess = items[mid]  # Assign mid point variable as guess

        if guess == target:  # By accessing mid point, Python is able to compare this to target value
            return mid  # Return mid if target is middle index
        elif guess < target:  # Narrows the search down to lower range
            low = mid + 1
        else:
            high = mid - 1  # Narrows search to higher range

    # The search continues until low is greater than high so high would be
    # the last index point meaning the whole list has been exhausted
    return None  # Return None if the target is not found in the list

sorted_items = ['The truth had to be told', 'Once upon a time', 'Good Morning']
target_item = 'Once upon a time'

index = binary_search(target_item, sorted_items)  # Perform binary search

if index is not None:
    print(f"Item '{target_item}' found at index {index}.")
else:
    print(f"Item '{target_item}' not found in the list.")
