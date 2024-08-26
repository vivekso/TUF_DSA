while True:
  try:
    a = int(input("Enter a valid integer: "))
    if(a > 1):
        break  # Exit the loop if input is valid
  except ValueError:
    print("Invalid input. Please enter an integera and greater then 1.")

def rectangularStarPattern(row, pattern):
  for i in range(row, -1, -1):
    print(i*pattern)

rectangularStarPattern(a,'*')