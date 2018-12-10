def merge_sort(array):
	if len(array) <= 1:  # base case
		return array

	# divide array in half and merge sort recursively
	half = len(array) // 2
	left = merge_sort(array[:half])
	right = merge_sort(array[half:])

	return merge(left, right)
def merge(left, right):
	arr = []
	l = 0
	r = 0
	while l < len(left) and r < len(right):
		if left[l] < right[r]:
			arr.append(left[l])
			l += 1
		else:
			arr.append(right[r])
			r += 1
	arr = arr + left[l:len(left)]
	arr = arr + right[r:len(right)]
	
	return arr
	
	
arr = [5,4,3,2,1]
arr = merge_sort(arr)
print(arr)