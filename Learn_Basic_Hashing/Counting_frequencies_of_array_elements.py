# 1st method 
# Using get function 
# In this case, frequency.get(i, 0) checks if i exists in the dictionary. If it does, it returns the value (which will be None in the first iteration). If it doesn't exist, it returns the default value 0. The + 1 increments the count regardless of whether the element existed or not.

def Counting_frequencies_of_array_elements(arr):
	frequency = {}
	for i in arr:
		frequency[i] = frequency.get(i, 0) + 1
	return frequency




# 2nd Method
'''Alternatively, you can initialize the frequency dictionary with a default value of 0 for all keys. This ensures that even if a key doesn't exist initially, it will have a value of 0 for the first access.'''

import collections

def Counting_frequencies_of_array_elements(arr):
	frequency = collections.defaultdict(int)
	for i in arr:
		frequency[i] += 1
	return frequency

array = [10,5,10,15,10,5]

print(Counting_frequencies_of_array_elements(array))