
"""
    Binary search.
    Only works on sorted arrays as we depend on the fact that there
    is a sorted structure that we can use to either move to the left subarray or right subarray.
    Think of how a sorted binary tree works:
    1) We check the current node
    2) If it is not current we check if the node is greater
    We move right (because our num is greater than node and so it must be in right subtree)
    Else move left (because our num is smaller and so it must be in left subtree)
    Rinse and repeat.
"""
import math
def binarySearch(arr, num):
    start = 0
    end = len(arr) - 1 # DONT FORGET THE -1!!!!
    # Need the == check or else we would not check the last case
    while start <= end:
        # In python we dont need floor because integer division.
        current = math.floor((start + end) / 2)
        
        if num == arr[current]: # Case 1: We found num
            return current
        elif num > arr[current]: # Case 2: Num we are searching for is greater so we check right. Update Start.
            start = current + 1
        else: # Case 3: Nums we are searching for is smaller so we check left. Update end.
            end = current - 1
    return -1 # If we dont find num return -1
