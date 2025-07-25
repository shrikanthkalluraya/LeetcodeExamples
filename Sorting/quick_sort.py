# Quick sort

def quick_sort(nums):
	if len(nums) <= 1:
		return nums

	pivot = nums[len(nums)//2]
	left = [x for x in nums if x < pivot]
	middle = [x for x in nums if x == pivot]
	right = [x for x in nums if x > pivot]

	return quick_sort(left) + middle + quick_sort(right)

if __name__ == "__main__":
	unsorted_list = [4, 8, 2, 5]
	res = quick_sort(unsorted_list)
	print(" ".join(map(str, res)))
	unsorted_list = [5, 4, 3, 2]
	res = quick_sort(unsorted_list)
	print(" ".join(map(str, res)))
	unsorted_list = [9, 2, 4, 8, 1]
	res = quick_sort(unsorted_list)
	print(" ".join(map(str, res)))
