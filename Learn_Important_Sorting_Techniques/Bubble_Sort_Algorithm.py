def Bubble_Sort_Algorithm(arr):
	n = len(arr)
	for i in range(n):
		swap_happend = False
		for j in range(0, n-i-1):
			if(arr[j] > arr[j+1]):
				arr[j], arr[j+1] = arr[j+1], arr[j]
				swap_happend = True
		if not swap_happend:
			break
	return arr

arr = [9, 13, 20, 24, 46, 52]
print(Bubble_Sort_Algorithm(arr))