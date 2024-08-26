from string import ascii_uppercase
def Alpha_Hill_Pattern(n):
	letter_string = list(ascii_uppercase)
	for i in range(n):
		for j in range(1,n-i):
			print(" ", end="")
		for j in range(i+1):
			print(letter_string[j], end="")
		for j in range(i, 0, -1):
			print(letter_string[j-1],end="")
		for j in range(1,n-i):
			print(" ", end="")
		print()


while True:
	a = int(input("please enter a integer greater then 1 :"))
	if(a > 1):
		break
	else:
	    print("Invalid input. Please enter an integera and greater then 1.")
Alpha_Hill_Pattern(a)