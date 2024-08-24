def Print_N_to_1_using_Recursion(n):
  if(n > 0):
    print(n)
    Print_N_to_1_using_Recursion(n-1)
Print_N_to_1_using_Recursion(3)
