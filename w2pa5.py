# Accept a string as input. Select a substring made up of three consecutive characters in the input string such that there are an equal number of characters to 
# the left and right of this substring. If the input string is of even length, make the string of odd length as below: • If the last character is a period ( . ), 
# then remove it • If the last character is not a period, then add a period ( . ) to the end of the string Print this substring as output. You can assume that all 
# input strings will be in lower case and will have a length of at least four.

n=str(input())
if len(n)%2 is 0:
  print('even')
  if n[len(n)-1] == '.':
    n=n.replace(n[len(n)-1],'')
    print(n)
    c=int(len(n)/2)
    print(n[c-1:c+2])
  else: 
    n=n+'.'
    print(n)
    c=int(len(n)/2)
    print(n[c-1:c+2])
else:
  print('odd')
  c=int(len(n)/2)
  print(n[c-1:c+2])
