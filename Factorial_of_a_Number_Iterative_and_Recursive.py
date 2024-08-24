def Factorial_of_a_Number_Iterative_and_Recursive(n):
  if (n <= 0):
    return 1
  else:
    return n * Factorial_of_a_Number_Iterative_and_Recursive(n-1)
print(Factorial_of_a_Number_Iterative_and_Recursive(10))
