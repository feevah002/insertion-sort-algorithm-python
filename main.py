def insertionSort(array):
  for j in range(1, len(array)):
    print("\n")
    print(j,"iteration")
    i = 0
    while array[j] > array[i]:
      i = i+1
    m = array[j]
    for k in range(0, j-i):
      array[j-k] = array[j-k-1]
    array[i] = m
    print(array)
arr = [19,4,61,3,9,6,0]
insertionSort(arr)

# -- or this(which ever one you choose to)

# un-comment(ctrl "/") it first tho

# def insertionSort(arr):
# 	for j in range(1, len(arr)):
# 		key = arr[j]
# 		i = j-1
# 		while i >= 0 and arr[i] > key:
# 			arr[i + 1] = arr[i]
# 			i -= 1
# 		arr[i + 1] = key
# arr = [12, 11, 13, 5, 6]
# insertionSort(arr)
# print (arr)