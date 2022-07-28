#strings
first_name = 'Jathursan'
last_name = 'Navamenan'
Xray = 'HELLO BOY'

print (first_name + last_name)
print ('Hello  '+ first_name+' '+ last_name)
print (len(first_name))
print (Xray.replace('HELLO BOY','HELLO GUYS'))
print(first_name.isupper())
print (last_name.index("e"))
print(Xray[8])


# String formatting

output = 'Hello, ' + first_name + ' ' + last_name
print(output)
output1 = 'Hello, {} {} '.format(first_name, last_name)
print(output1)
output2 = 'Hello, {0} {1} '.format(first_name, last_name)
print(output2)
output3 = 'Hello, {1} {0} '.format(first_name, last_name)
print(output3)
output4 = f'Hello,{first_name} {last_name}'
print(output4)

# get input string

First_name = input('Enter the First name:  ')
Last_name = input('Enter the Last name:  ')

print ('This is you entered')
print (First_name + Last_name)

# Capitalize the string

print ('After capitalizieing:')
print('HAI '+ First_name.capitalize()+' '+Last_name.capitalize())
print("hai i'm "+First_name.upper()+' '+Last_name.lower())