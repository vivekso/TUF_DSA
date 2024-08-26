def Symmetric_Butterfly_Pattern(n):

	for i in range(1,n+1):
		space = n - i
		for j in range(i):
			print("*",end="")
		for j in range(2 * space):
			print(" ",end="")
		for j in range(i):
			print("*",end="")
		print()
	for i in range(n-1, 0, -1):
		space = n - i
		for j in range(i):
			print("*",end="")
		for s in range(2*space):
			print(" ", end="")
		for j in range(i):
			print("*",end="")
		print()

while True:
	a = int(input("please enter a integer greater then 1 :"))
	if(a > 1):
		break
	else:
	    print("Invalid input. Please enter an integera and greater then 1.")
Symmetric_Butterfly_Pattern(a)