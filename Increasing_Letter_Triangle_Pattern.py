import string
def Increasing_Letter_Triangle_Pattern(n):
  letter_string = list(string.ascii_uppercase)
  pattern = ""
  for i in range(1, n + 1):
    for j in range(1, i + 1):
      pattern += letter_string[j - 1]
    pattern += "\n"
  return pattern


while True:
	a = int(input("please enter a integer greater then 1 :"))
	if(a > 1):
		break
	else:
	    print("Invalid input. Please enter an integera and greater then 1.")
print(Increasing_Letter_Triangle_Pattern(a))