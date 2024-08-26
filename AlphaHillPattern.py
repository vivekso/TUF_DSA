import string

uppercase_latter = string.ascii_uppercase
# print(uppercase_latter)

while True:
  try:
    a = int(input("Enter a valid integer: "))
    if(a > 1):
        break  # Exit the loop if input is valid
  except ValueError:
    print("Invalid input. Please enter an integera and greater then 1.")

if(a == 1):
	print(uppercase_latter[a-1])
else:
	print("A")
	for i in range(1, a+1):
		for j in range(i):
			print(uppercase_latter[j], end="")
		for k in range(i,-1,-1):
			print(uppercase_latter[k], end="")
		print("")
