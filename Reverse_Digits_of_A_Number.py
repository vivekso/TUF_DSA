def Reverse_Digits_of_A_Number(n):
	reverse_num = 0
	while n > 0:
		num = n % 10
		n = n // 10
		reverse_num = reverse_num * 10 + num
	return reverse_num
print(Reverse_Digits_of_A_Number(86723600))