def Find_the_highest_lowest_frequency_element(arr):
	frequency = {}
	for i in arr:
		frequency[i] = frequency.get(i, 0) + 1
	highest_frequency = max(frequency.values())
	lowest_frequency = min(frequency.values())

	highest_frequency_elements = [num for num, freq in frequency.items() if freq == highest_frequency]
	lowest_frequency_elements = [num for num, freq in frequency.items() if freq == lowest_frequency]


	return highest_frequency_elements, lowest_frequency_elements

arr = [10,15,5,10,10,5,5,15,15]
print(Find_the_highest_lowest_frequency_element(arr))