def Fibonacci_Series(n):
	if n <= 1:
		return n
	else:
		return Fibonacci_Series(n-1)+ Fibonacci_Series(n-2)
print(Fibonacci_Series(9))