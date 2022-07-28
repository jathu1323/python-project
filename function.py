from datetime import datetime

#define

print('Task start :-) \n')
def print_time(task_name):
    print(task_name)
    print('JDK')
    print(datetime.now())
    print()

print_time('creator of function')

for x in range(0,11):
    print(x)
print_time('Task Completed ;-) Suessfull')


# logic over & over
name='JATHURSAN'
a=(name[0:1])
name2='NAVAMENAN'
b=(name2[0:1])

print('FIRST LATTERS ARE : '+a+' '+b)

def get(a):
    initial=a[0:1].upper()
    return initial

f_name = input('Enter the First name:  ')
f_name_i =get(f_name)
m_name = input('Enter the Middle name:  ')
m_name_i =get(m_name)
l_name = input('Enter the Last name:  ')
l_name_i =get(l_name)

print ('initials of your input :'+f_name_i+m_name_i+l_name_i)


# function parameters

def get1(b,force_uppercase=True):
    if force_uppercase:
        init=b[0:1].upper()
    else:
        init=b[0:1]
    return init

fi_name = input('Enter the First name:  ')
fi_name_i =get1(fi_name)

print('initial is : '+ fi_name_i)