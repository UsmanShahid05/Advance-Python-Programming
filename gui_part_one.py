import tkinter as mytk
root=mytk.Tk()
root.title("My GUI Application")
root.geometry("400x300")
label=mytk.Label(root,text='Hello,World!')
label.pack()
button=mytk.Button(root,text="Click Button",bg="blue",fg='white',font=15,width=20,pady=20,command=lambda:print("You are not here"))
button1=mytk.Button(root,text="Click Me",bg='blue',fg='white', command=lambda:print("Button Clicked"),width=14,height=2,font=10)
button.pack()
button1.pack()

button2=mytk.Button(root,text="Click Now",bg='Black',fg='white',font=10,command=lambda:print("Thanks for clicking, but you are too slow"))
button2.pack()


root.mainloop()
