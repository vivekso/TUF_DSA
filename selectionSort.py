
def descending(L):
	lenOfArr = len(L)
	if lenOfArr < 1:
		return L

	for i in range(lenOfArr):
		j = i
		while (j > 0 and L[j] > L[j-1]):
			L[j], L[j-1] = L[j-1],L[j]
			j -= 1
	return L



def ascending(l):
	n = len(l)
	if n < 1:
		return l
	for i in range(n):
		j = i
		while (j > 0 and l[j] < l[j-1]):
			l[j],l[j-1] = l[j-1],l[j]
			j -= 1
	return l