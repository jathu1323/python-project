x=50
y=0
z=2

print ()

try:
    print (x/y)
except:
    print('Not allowed to devide')
    try:
        a=x/z
        print(a)

        try:
            print (a/y)
        except:

            print('another')

            if (a<= 25.0):
                print('loop sucess')
                if (a<10.0):
                    print('nbjngb')
                else:
                    print('kkj')  
        else:
            print('bye')
    except:
        print('jathu')

    else:
        print('######')
else:
    print('something else here ')
finally:
    print ('this is our clean code')

print ()

