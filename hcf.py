m, n, = int(input("enter the value of m  ")), int(input("enter the value of n  "))


def find_hcf(m,n):
	min_number = min(m,n)

	hcf = 1
	for i in range(1,min_number -1):
		if m % i == 0 and n % i == 0:
			hcf = i
	return hcf

print(find_hcf(m,n))
