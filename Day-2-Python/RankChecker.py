mark= int(input('Enter obtained mark: '))
full=int(input('Enter total marks: '))
percentage=mark/full*100
if percentage>=90:
    print('You are passed with A grade')
elif percentage>=80:
    print('You are passed with B grade')
elif percentage>=70:
    print('You are passed with C grade')
elif percentage>=60:
    print('You are passed with D grade')
elif percentage>=30:
    print('You are passed with E grade')
else:
    print('You are Failed')