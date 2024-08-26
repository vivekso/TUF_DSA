def Find_GCD_of_two_numbers(n,m):
    while m:
        n, m = m, n % m
    return n

print(Find_GCD_of_two_numbers(192,271))