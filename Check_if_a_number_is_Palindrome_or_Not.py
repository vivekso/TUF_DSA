def Check_if_a_number_is_Palindrome_or_Not(n):
	reverse_num = 0
	originan_number = n
	while n > 0 :
		num = n % 10
		n = n // 10
		reverse_num = reverse_num * 10 + num
	if(originan_number == reverse_num):
		return 'Palindrome Number'
	else:
		return 'Not Palindrome'

print(Check_if_a_number_is_Palindrome_or_Not(786875))