def even():
    for i in range(2,11):
        if i%2==0:
            yield i
for i in even():
    print (i)