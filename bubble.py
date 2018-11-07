def bubble_sort(arr):
  changed = True
  while changed:
    changed = False
    for i in range(len(arr) - 1):
      if arr[i] > arr[i + 1]:
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
        changed = True

arr = [2,4,5,3,1,6,7,9,4]

bubble_sort(arr)
print(arr) 
