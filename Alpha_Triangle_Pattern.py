from string import ascii_uppercase
def Alpha_Triangle_Pattern(n):
	letter_list = list(ascii_uppercase)
	for i in range(1, n+1):
		for j in range(i,0,-1):
			print(letter_list[n-j],end='')
		print()



while True:
	a = int(input("please enter a integer greater then 1 :"))
	if(a > 1):
		break
	else:
	    print("Invalid input. Please enter an integera and greater then 1.")
Alpha_Triangle_Pattern(a)