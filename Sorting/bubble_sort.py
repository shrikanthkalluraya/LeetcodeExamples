#bubble sort

def bubble_sort(nums):
	inp_len = len(nums)

	for i in reversed(range(inp_len)):
		swapped = False
		for j in range(i):
			if nums[j]>nums[j+1]:
				nums[j], nums[j+1] = nums[j+1], nums[j]
				swapped = True
		if not swapped:
			return nums
	return nums
if __name__ == "__main__":
    unsorted_list = [4, 8, 2, 5]
    res = bubble_sort(unsorted_list)
    print(" ".join(map(str, res)))
    unsorted_list = [5, 4, 3, 2]
    res = bubble_sort(unsorted_list)
    print(" ".join(map(str, res)))
    unsorted_list = [9, 2, 4, 8, 1]
    res = bubble_sort(unsorted_list)
    print(" ".join(map(str, res)))
