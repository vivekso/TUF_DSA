import string
def Reverse_Letter_Triangle_Pattern(n):
	letter_list = list(string.ascii_uppercase)
	for i in range(n, 0, -1):
		for j in range(i):
			print(letter_list[j],end='')
		print()


while True:
	a = int(input("please enter a integer greater then 1 :"))
	if(a > 1):
		break
	else:
	    print("Invalid input. Please enter an integera and greater then 1.")
Reverse_Letter_Triangle_Pattern(a)