def Number_Crown_Pattern(a):
	space = 2*(a - 1)
	for i in range(1, a + 1):
		for j in range(1,i+1):
			print(j,end='')
		for k in range(space):
			print(' ', end='')
		for l in range(i,0,-1):
			print(l, end='')
		print()
		space -= 2
while True:
	a = int(input("please enter a integer greater then 1 :"))
	if(a > 1):
		break
	else:
	    print("Invalid input. Please enter an integera and greater then 1.")
Number_Crown_Pattern(a)