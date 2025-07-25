# Insertion sort

def insertion_sort(nums):
	inp_len = len(nums)
	for i in range(1, inp_len):
		key = nums[i]
		j = i
		while j > 0 and nums[j] < nums[j - 1]:
			nums[j], nums[j-1] = nums[j - 1], nums[j]
			j -= 1
	return nums

if __name__ == "__main__":
    unsorted_list = [4, 8, 2, 5]
    res = insertion_sort(unsorted_list)
    print(" ".join(map(str, res)))
    unsorted_list = [5, 4, 3, 2]
    res = insertion_sort(unsorted_list)
    print(" ".join(map(str, res)))
    unsorted_list = [9, 2, 4, 8, 1]
    res = insertion_sort(unsorted_list)
    print(" ".join(map(str, res)))
