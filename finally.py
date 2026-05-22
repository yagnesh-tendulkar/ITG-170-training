def division(a,b):
    try:
        c=a/b
    
    except (ValueError, ZeroDivisionError) as e:
        print(e.args)
    else :
        print(c)
    finally:

    #  return 100
       print("this is finnay block")
    
print(division(100,4)        )