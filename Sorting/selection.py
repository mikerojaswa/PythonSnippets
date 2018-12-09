arr = [3,5,1,6,9,4]
arr2 = [1,2,3,4,5,6]
arr3 = [6,5,4,3,2,1]
arr4 = [2,2,2,2,2,2,2,2]

def selection_sort(arr):
	min_idx = 0
	for i in range(len(arr)):
		min_idx = i
		for j in range(i + 1, len(arr)):
			if arr[min_idx] > arr[j]:
				min_idx = j
		arr[i], arr[min_idx] = arr[min_idx], arr[i]
	

				


selection_sort(arr)
selection_sort(arr2)
selection_sort(arr3)
selection_sort(arr4)
print(arr)
print(arr2)
print(arr3)
print(arr4)