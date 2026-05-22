# # 35.Program to check whether a given number is a happy number or not?
# def happy(n):
#     if n == 1:
#         return n
#     if n <=0:
#         return 0
#     t = n
#     l_d=[]
#     s=0
#     while( t>0):
#         d = t % 10
#         l_d.append(d)
#         t = t // 10
#     l_d.reverse()
#     for i in l_d:
#         s += pow(i,2)
#     if s == 1:
#         print("true")
        
#     else:
#         return happy(s)
# n = 71
# happy(n)