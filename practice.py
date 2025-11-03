def bubble_sort(arr):
  n = len(arr)
  for i in range(n):
    for j in range(0, n - i - 1):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
  return arr

def selection_sort(arr):
  n = len(arr)
  for i in range(n):
    min_index = i
    for j in range(i+1, n):
      if arr[min_index] > arr[j]:
        min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]

def insertion_sort(arr):
  n = len(arr)
  for i in range(1, n):
    key = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > key:
      arr[j + 1] = arr[j]
      j -= 1
    arr[j + 1] = key

def merge_sort(arr):
  n = len(arr)
  if n <= 1:
    return arr

  mid = n // 2
  left = merge_sort(arr[:mid])
  right = merge_sort(arr[mid:])

  result = []
  i = j = 0
  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(left[j])
      j += 1

  result += left[i:]
  result += right[j:]
  return result

def quick_sort(arr):
  n = len(arr)
  if n <= 1:
    return arr
  
  # pivot = arr[n // 2]
  # left = [x for x in arr if x < pivot]
  # middle = [x for x in arr if x == pivot]
  # right = [x for x in arr if x > pivot]
  # return quick_sort(left) + middle + quick_sort(right)
  pivot = arr[n // 2]
  left, middle, right = [], [], []
  for x in arr:
    if x < pivot:
      left.append(x)
    elif x > pivot:
      right.append(x)
    else:
      middle.append(x)
  return quick_sort(left) + middle + quick_sort(right)