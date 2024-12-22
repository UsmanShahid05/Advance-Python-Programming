file=open("example.txt",'w')
file.write("Hello world of coding. \n")
file.write("Usman Shahid is here.\n")
file.write(str(1234))
file.close()
file=open('example.txt','r')
content=file.read()
print(content)
file.close()
file=open('example.txt','a')
file.write('\nThis is appended text line\n')
file.close()
file=open('example.txt','r')
content=file.read()
print(content)
for line in content:
    print(line.strip())
    print("You got this line")

file=open('example.txt','r')
lines=file.readlines()
print(lines)
print("Hello")
print(line.strip())
file.close()

new_file=open("file.docx",'w')
new_file.write("Hello this is first line in this docs file\n")
new_file.close()
file=open('file.docx','r')
file=file.readlines()
print(file)
file[0]='This line has been modified'
print(file)

file.close()

file=open('example.txt','r')
while True:
   line=file.readlines()
   if not line:
       print("Text ended")
       break
   print("While loop read line : ",line)

print("Hello World!")
file.close()
import os
#os.rename('example.txt','texted_file.txt')
try:
    file=open("example.txt",'r')
    content=file.readlines()
    print(content)
except FileNotFoundError:
    print("Sorry File Not Found!")

file=open("texted_file",'w')
print("File closed : ",file.closed)
print("File Mode : ",file.mode)
print("File Name : ",file.name)
print("File Softspace : " , hasattr(file,'softspace'))
file.close()
print("File Closed : ",file.closed)






