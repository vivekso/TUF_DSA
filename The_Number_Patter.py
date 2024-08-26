''' def The_Number_Patter(n):
  for i in range(2 * n - 1):
    for j in range(2 * n - 1):
      top = i
      bottom = (2 * n - 2) - i
      right = (2 * n - 2) - j
      left = j
      print(n - min(top, bottom, left, right), end=" ")
    print()

while True:
	a = int(input("please enter a integer greater then 1 :"))
	if(a > 1):
		break
	else:
	    print("Invalid input. Please enter an integera and greater then 1.")
The_Number_Patter(a)
'''
def number_pattern(n):
    size = 2 * n - 1
    for i in range(size):
        for j in range(size):
            distance = min(i, j, size - i - 1, size - j - 1)
            print(n - distance, end=" ")
        print()

while True:
    a = int(input("Please enter an integer greater than 1: "))
    if a > 1:
        break
    else:
        print("Invalid input. Please enter an integer greater than 1.")

number_pattern(a)
