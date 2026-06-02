import random
import time

class MergeSOrt(object):
	"""
	It is Algrothimn which solve sorting in O(n log(n))
	"""
	def __init__(self, arr):
		self.arr = arr

	def merge(self, left, right):
		
		result = []

		left_element, right_element = 0, 0

		while left_element < len(left) and right_element < len(right):
			if left[left_element] <= right[right_element]:
				result.append(left[left_element])
				left_element += 1
			else:
				result.append(right[right_element])
				right_element += 1

		if left :
			result.extend(left[left_element:])
		if right:
			result.extend(right[right_element:])
		return result

	def mergesort(self):
		if len(self.arr) <= 1:
			return self.arr

		# Divide array in two part
		middle = len(self.arr) // 2

		left = MergeSOrt(self.arr[:middle])
		right = MergeSOrt(self.arr[middle:])

		# divide array recursively
		
		left = left.mergesort()
		right = right.mergesort()

		return self.merge(left, right)
a = time.time()
arr = [random.randint(1,1000000) for _ in range(1000000)]

obj = MergeSOrt(arr)

# Measure execution time accurately
start = time.perf_counter()
sorted_arr = obj.mergesort()
end = time.perf_counter()

print(f"First 10 sorted elements: {sorted_arr[:10]}")
print(f"Execution time: {end - start:.6f} seconds")