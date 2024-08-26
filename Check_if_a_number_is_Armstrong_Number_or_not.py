def Check_if_a_number_is_Armstrong_Number_or_not(n):
	cube_sum = 0
	m = n
	while n > 0:
		remainder = n % 10
		cube_sum = cube_sum + remainder ** 3
		n = n // 10
	return cube_sum == m
print(Check_if_a_number_is_Armstrong_Number_or_not(371))