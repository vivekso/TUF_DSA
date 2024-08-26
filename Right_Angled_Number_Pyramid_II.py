while True:
  try:
    a = int(input("Enter a valid integer: "))
    if(a > 1):
        break  # Exit the loop if input is valid
  except ValueError:
    print("Invalid input. Please enter an integera and greater then 1.")

def rectangularStarPattern(row):
  for i in range(1, row + 1):
    for j in range(i):
      print(i, end="")
    print("")

rectangularStarPattern(a)