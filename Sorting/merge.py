def merge_sort(arr):
	if len(arr) == 1:
		return arr
	
	a = arr[0:len(arr)/2]
	b = arr[(len(arr)/2) + 1: len(arr)]
	
	
arr = [5,4,3,2,1]
merge_sort(arr)
print(arr)