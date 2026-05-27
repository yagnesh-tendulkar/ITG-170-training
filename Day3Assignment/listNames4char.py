arr = list(map(str,input("Enter names : ").split()))



result= list(filter(lambda name: len(name)>4,arr))