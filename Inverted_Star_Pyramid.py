while True:
  try:
    a = int(input("Enter a valid integer: "))
    if(a > 1):
        break  # Exit the loop if input is valid
  except ValueError:
    print("Invalid input. Please enter an integera and greater then 1.")

def invertedStarPyramid(a):
  for i in range(a, 0, -1):
    for j in range(a - i):
      print(" ", end="")
    for j in range(2 * i - 1):
      print("*", end="")
    for j in range(a - i):
      print(" ", end="")

    print()


invertedStarPyramid(a)