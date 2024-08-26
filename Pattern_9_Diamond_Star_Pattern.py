import Inverted_Star_Pyramid
import Star_Pyramid

while True:
  try:
    a = int(input("Enter a valid integer: "))
    if(a > 1):
        break  # Exit the loop if input is valid
  except ValueError:
    print("Invalid input. Please enter an integera and greater then 1.")

def diamondStarPattern(n):
	Star_Pyramid.Star_Pyramid(n)
	Inverted_Star_Pyramid.invertedStarPyramid(n)
diamondStarPattern(a)