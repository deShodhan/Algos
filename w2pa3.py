#Accept an integer as input and print the time of the day. Use the following table for reference.

#T < 0 --INVALID
#0 <T < =5 --NIGHT
#6 < T < =11 --MORNING
#12 <T < =17 --AFTERNOON
#18 <T < =23 --EVENING
#Τ >24 --INVALID
#The input will be a single line containing an integer. The output should be one of these strings: NIGHT, MORNING, AFTERNOON, EVENING, INVALID.

value=int(input('Enter value:'))
if value<0:
    print('INVAILD')
elif 0<value<=5:
    print('NIGHT')
elif 6<=value<=11:
    print('MORNING')
elif 12<=value<=17:
    print('AFTERNOON')
elif 18<=value<=24:
    print('EVENING')
elif value>=24:
    print('INVAILD')
