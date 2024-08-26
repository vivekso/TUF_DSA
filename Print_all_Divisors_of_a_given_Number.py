import math
def Print_all_Divisors_of_a_given_Number(n):
	divisor_list = []
	itirate_over = int(math.sqrt(n))

	for i in range(1,itirate_over +1):
		if((n % i) == 0):
			divisor_list.append(i)
			if(i != n // i):
				divisor_list.append(n//i)
	return divisor_list

print(Print_all_Divisors_of_a_given_Number(4362875872533423))