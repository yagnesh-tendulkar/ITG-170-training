# reading the file
# file = open("/home/miracle/Desktop/file_handling/example.txt",'w')
# content = file.read()
# print(content)
# file.close()

# ==========================================
# writing the file

# with open("/home/miracle/Desktop/file_handling/example.txt",'w') as file:
#     file.write('Hello, this is python progrmming')
# file1 = open("/home/miracle/Desktop/file_handling/example.txt",'r')
# content = file1.read()
# print(content)
# file1.close()

# ===========================================
# appending the file
# with open("/home/miracle/Desktop/file_handling/example.txt",'a') as file:
#     file.write(' Python is dynamically typed')
# file1 = open("/home/miracle/Desktop/file_handling/example.txt",'r')
# content = file1.read()
# print(content)
# file1.close()
# =============================================
# with open("/home/miracle/Desktop/file_handling/example.txt",'w') as file1:
#     file1.write("Python is dynamically typed and general purpose programming language")

# file = open("/home/miracle/Desktop/file_handling/example.txt",'r')
# content = file.read()
# print(content)
# file.close()
# ==============================================
# reading different types
# csv
# import csv
# with open("file path of csv",'r') as csvfile:
#     reader = csv.reader(csvfile)
#     for r in reader:
#         print(r)
# import csv
# with open("file path",'r') as file1:
#     reader = csv.reader(file1)
#     for r in reader:
#         print(r)
# ===========================
# import json
# with open("file path",'r') as json_file:
#     data = json.load(json_file)
#     print(data)
# ======================
# from docx import Document
# doc = Document('file path')
# for para in doc.paragraphs:
#     print(para.text)
# pip install python-docx
# ====================
# reading pdf files 
# import PyPDF2
# with open("file path",'rb') as pdffile:
#     reader = PyPDF2.PdfReader(pdffile)
#     for i in reader.pages:
#         print(i.extract_files())
# ====================



    