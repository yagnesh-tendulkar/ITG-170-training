""" using write
file=open("data.txt","w")
file.write("Hello world")
file.close()"""
""" using writelines
file=open("data.txt","w")
lines=["Hi\n","Hello\n","Whatsup"]
file.writelines(lines)
file.close()"""
""" using append
file=open("data.txt","a")
file.write("Hello harinita")
file.close()"""
