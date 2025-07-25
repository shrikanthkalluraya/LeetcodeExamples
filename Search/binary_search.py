# Binary Search

def binary_search(nums, target):
	left, right = 0, len(nums) - 1
	while left <= right:
		mid = (left + right) // 2

		if nums[mid] == target:
			return mid
		elif nums[mid] < target:
			left = mid + 1
		else:
			right = mid - 1

	return -1

if __name__ == "__main__":
    arr = [2, 4, 5, 7, 8, 9, 11, 34, 54, 56, 65, 74]
    target = 8
    res = binary_search(arr, target)
    print(res)