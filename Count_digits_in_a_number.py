def Count_digits_in_a_number(n):
  count = 0
  while n > 0:
    n //= 10
    count += 1
  return count
print(Count_digits_in_a_number(47358742))
# print(1//10)
