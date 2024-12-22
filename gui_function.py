import tkinter as mytk

def on_button_click():
    print("Great! You Done It.")

def another_function():
    print("Another function Executed.")
root=mytk.Tk()
root.title("NEW GUI WINDOW")
root.geometry('400x300')
user_name=input("Enter your name : ")
label=mytk.Label(root,text=f'Hello {user_name}', font=10)
label.pack()
button=mytk.Button(root,text='Get in touch now',font=10,bg='black',fg='white',command=on_button_click)
button1=mytk.Button(root,text="Second Task",font=10, bg='blue',fg='white',command=another_function)
button1.pack()
button.pack()

root.mainloop()
