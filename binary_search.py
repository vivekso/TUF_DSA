import random as rand

def binary_search(arr,target):
	low = 0
	heigh = len(arr)
	mid = 0
	while (low <= heigh):
		mid = (low + heigh) //2
		if (arr[mid] < target):
			low = mid + 1
		elif (arr[mid] > target):
			heigh = mid - 1
		else :
			return mid
	return -1

def rand_list():
	rand_lst = []
	for i in range (100):
		n = rand.randint(1,10)
		rand_lst.append(n)
		rand_lst = sorted(rand_lst)
	return(rand_lst)

arr = [1,2,3,4,5,6,768,876,9787]
print(rand_list())
print(binary_search(rand_list(), 1))
