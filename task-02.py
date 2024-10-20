import heapq

def merge_k_lists(lists):
    # create empty list
    merged_list = []
    # create min heap
    min_heap = []

    #  add 1st elemets to heap
    for i, sorted_list in enumerate(lists):
        if sorted_list:
            heapq.heappush(min_heap, (sorted_list[0], i, 0))
# take min elements from heap and add to list
    while min_heap:
        value, list_idx, element_idx = heapq.heappop(min_heap)
        merged_list.append(value)

# if there is still elements add next elem to heap
        if element_idx + 1 < len(lists[list_idx]):
            next_value = lists[list_idx][element_idx + 1]
            heapq.heappush(min_heap, (next_value, list_idx, element_idx + 1))
    return merged_list
# example of use
lists = [[1, 2, 5], [1, 7, 3], [2, 6]]
merged_list = merge_k_lists(lists)
print("Sorted list is:", merged_list)