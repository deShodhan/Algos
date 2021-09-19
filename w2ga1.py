# Accept three positive integers as input and check if they form the sides of a right triangle. Print YES if they form one, and No if they do not. 
# The input will have three lines, with one integer on each line. The output should be a single line containing one of these two strings: YES or NO.

a=int(input('Enter value for side a:'))
b=int(input('Enter value for side b:'))
c=int(input('Enter value for side c:'))
if a**2==b**2+c**2 or b**2==a**2+c**2 or c**2==a**2+b**2:
  print('yes, you can form a right angle triangle')
else:
  print('No, you can noy form a right angle triangle') 
