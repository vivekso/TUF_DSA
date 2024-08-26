def print_binary_triangle(n):
  for i in range(1, n + 1):
    start = 0 if i % 2 == 0 else 1
    for j in range(i):
      print(start, end="")
      start = 1 - start
    print()

while True:
  try:
    n = int(input("Enter a valid integer: "))
    if n > 1:
      break
  except ValueError:
    print("Invalid input. Please enter an integer greater than 1.")

print_binary_triangle(n)
