def Sum_of_first_N_Natural_Numbers(n):
  if(n < 0):
    return 0
  else:
    return n + Sum_of_first_N_Natural_Numbers(n-1)
print(Sum_of_first_N_Natural_Numbers(3))
