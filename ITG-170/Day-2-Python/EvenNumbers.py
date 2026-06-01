start= int(input('Enter the start range: '))
end= int(input('Enter the end range: '))

for i in range(start,end+1):
    if i%2==0:
        print(i)