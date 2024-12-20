
i=5
while i>=0:
    print(i)
    i=i-1
print("While loop has been ended! ")

a=range(1,10,2)
i=1
for item in a:
    print(f" Value of dummy variable in iteration {i} is :",item)
    i=i+1



for i in range(1,4):
    for j in range(1,5):
        print(i," : ",j)
    print("inner loop has been ended")
print("Outloop has also been ended. ")



while True:
    age=input("Enter your age in years : ")
    if age.isdigit() and int(age) >0:
        age=int(age)
        print(f"Your age is {age} years. ")
        break
    else:
        print("Please enter a valid age")



user_text=input("Enter anything you want to check your input type :  ")
if user_text.isdigit():
    print("you entered digits values and your input datatype is : ",type(int(user_text)))
else:
    print("Your entered text datatype is : string")


while True:
    age=input("Enter your age in years : ")
    if age.isdigit() and int(age)>0:
        age=int(age)
        print(f"Your age is {age} years.")
        break
    else:
        print("Invalid Input! Please enter a valid age value.")

for i in range (1,11):
    if i%2==0:
        
        print(f"Sorry {i} is even number and can't be printed.")
        continue
    else:
        print(f"You got new value i.e {i}")
