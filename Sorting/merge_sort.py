# Merge sort

def merge_sort(nums):
	inp_len = len(nums)
	if inp_len <= 1:
		return nums
	mid = inp_len//2
	left_half = nums[:mid]
	right_half = nums[mid:]

	left_half = merge_sort(left_half)
	right_half = merge_sort(right_half)

	return merge(left_half, right_half)

def merge(left, right):
	merged_list = []
	i = 0
	j = 0

	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			merged_list.append(left[i])
			i += 1
		else:
			merged_list.append(right[j])
			j += 1

	while i < len(left):
		merged_list.append(left[i])
		i += 1
	while j< len(right):
		merged_list.append(right[j])
		j += 1
	return merged_list




if __name__ == "__main__":
    unsorted_list = [4, 8, 2, 5]
    res = merge_sort(unsorted_list)
    print(" ".join(map(str, res)))
    unsorted_list = [5, 4, 3, 2]
    res = merge_sort(unsorted_list)
    print(" ".join(map(str, res)))
    unsorted_list = [9, 2, 4, 8, 1]
    res = merge_sort(unsorted_list)
    print(" ".join(map(str, res)))
