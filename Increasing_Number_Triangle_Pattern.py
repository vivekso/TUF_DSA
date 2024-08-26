def Increasing_Number_Triangle_Pattern(n):
	start = 1
	for i in range(1,n+1):
		for j in range(1,i+1):
			print(start,' ',end='')
			start += 1
		print()

while True:
	a = int(input("please enter a integer greater then 1 :"))
	if(a > 1):
		break
	else:
	    print("Invalid input. Please enter an integera and greater then 1.")
Increasing_Number_Triangle_Pattern(a)