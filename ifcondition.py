# if & elif conditions

country =input('Country Name Srilanka or India : ')
if country.lower() == 'srilanka':
    price=(int(input('Enter Your Salary LKR: ')))*12
    print ('Annual income LKR:', price)

    if price >=250000:    
        if price <= 300000 :
            print('Annual income 300000 (Paying Tax) : ')
            x=price*(6/100)
            print (x)
        elif price <= 600000:
            print('Annual income 600000 (Paying Tax) : ')
            y=(price*(12/100))+(price*(6/100))
            print (y)
        elif price >60000:
            print('Annual income above 600000 (Paying Tax) : ')
            z=price*(18/100)
            print (z)
    else :
        print('Not Eligible For Tax Paying')

elif country.lower() == 'india':
    state=input("Enter your State \n[andhrapradesh, amaravati, goa, Other] : ")

    if state.lower() in ('andhra pradesh','amaravati','goa','other'):
        price=(int(input('Enter Your Salary INR : ')))*12
        print ('Annual income INR :', price)

        if price >=250000:    
            if price <= 500000 :
                print('Annual income 500000 (Paying Tax) : ')
                x=price*(5/100)
                print (x)
            elif price <= 750000:
                print('Annual income 750000 (Paying Tax) : ')
                a=(price*(10/100))+12500
                print (a)
            elif price <=1000000 :
                print('Annual income above 1000000 (Paying Tax) : ')
                b=(price*(15/100))+37500
                print (b)
            elif price<=1250000:
                print('Annual income above 1250000 (Paying Tax) : ')
                c=(price*(20/100))+75000
                print (c)
            elif price<1500000:
                print('Annual income above 150000 (Paying Tax) : ')
                d=(price*(25/100))+125000
                print (d)
            elif price >=1500000:
                print('Annual income above 150000 (Paying Tax) : ')
                e=(price*(30/100))+187500
                print (e)
        else:
            price('Not Eligible for paying tax')
    else :
        print('Your State not in a list')
    
else:
    print('Sorry...\n'' Your country is not here... \n'' Wait for The Next updates.... \n'' Thanks for Using Our Services')

