# Selection Sort
def selection_sort(nums):
	inp_len = len(nums)
	for i in range(inp_len):
		min_idx = i
		for j in range(i, inp_len):
			if nums[min_idx] > nums[j]:
				nums[min_idx], nums[j] = nums[j], nums[min_idx]

	return nums


if __name__ == "__main__":
    unsorted_list = [4, 8, 2, 5]
    res = selection_sort(unsorted_list)
    print(" ".join(map(str, res)))
    unsorted_list = [5, 4, 3, 2]
    res = selection_sort(unsorted_list)
    print(" ".join(map(str, res)))
    unsorted_list = [9, 2, 4, 8, 1]
    res = selection_sort(unsorted_list)
    print(" ".join(map(str, res)))
