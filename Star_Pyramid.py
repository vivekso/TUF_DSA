while True:
  try:
    a = int(input("Enter a valid integer: "))
    if(a > 1):
        break  # Exit the loop if input is valid
  except ValueError:
    print("Invalid input. Please enter an integera and greater then 1.")

def starPyramid(a):
  totalNumerOfRow = a + a-1
  for i in range(a):
    for j in range(a-i-1):
      print(' ', end='')
    for k in range(2*i+1):
      print('*', end='')
    for l in range(a-i-1):
      print(' ', end='')
    print('')
starPyramid(a)