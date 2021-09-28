'''
Simple Ciper code. Shift places of a given string
'''
alpha='abcdefghijklmnopqrstuvwxyz'
n=input()
k=1
for i in range(len(n)):
  print(alpha[((alpha.index(n[i]))+k)%26])
