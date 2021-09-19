# Evenodd is a tech startup. Each employee at the startup is given an employee id which is a unique positive integer. On one warm Sunday evening, five employees of 
# the company come together for a meeting and sit at a circular table:
# E1,E5,E2,E4,E3
# The employees follow a strange convention. They will continue the meeting only if the following condition is satisfied. The sum of the employee-ids 
# of every pair of adjacent employees at the table must be an even number. They are so lazy that they won't move around to satisfy the above condition. If the 
# current seating plan doesn't satisfy the condition, the meeting will be canceled. You are given the employee-id of all five employees. Your task is to decide if the 
# meeting happened or not. The input will be five lined, each line containing an integer. The įth line will have the employee-id of Ei. The output will be a single 
# line containing one of these two strings: YES or NO.

list=[]
x=0
for i in range(5):
  print('Enter value for employee no.',i)
  ele=int(input())
  list.append(ele) 
for i in range(len(list)-1):
  if (list[i]+list[i+1])%2 !=0:
    x=x+1
if x==0:
  print('YES, they can have a chat')
else:
  print('NO, they cant have a chat')  
