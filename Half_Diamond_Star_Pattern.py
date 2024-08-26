while True:
  try:
    a = int(input("Enter a valid integer: "))
    if(a > 1):
        break  # Exit the loop if input is valid
  except ValueError:
    print("Invalid input. Please enter an integera and greater then 1.")

def HalfDiamondStarPattern(n):
  for i in range(1,2*n):
    if(i <= n):
      for j in range(i):
        print("*",end="")
    if(i > n):
      for j in range(i,2*n):
        print("*",end="")

    print()

HalfDiamondStarPattern(a)