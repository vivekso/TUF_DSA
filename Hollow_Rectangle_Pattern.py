def Hollow_Rectangle_Pattern(n):
	for i in range(n):
		if((i == 0) or (i == n-1)):
			for j in range(n):
				print("*",end="")
		else:
			for i in range(n):
				if((i == 0) or (i == n-1)):
					print("*",end="")
				else:
					print(" ",end="")
		print()

while True:
	a = int(input("please enter a integer greater then 1 :"))
	if(a > 1):
		break
	else:
	    print("Invalid input. Please enter an integera and greater then 1.")
Hollow_Rectangle_Pattern(a)