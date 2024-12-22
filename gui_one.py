import tkinter as tk
root=tk.Tk()

def on_button_click():
    print("Button Clicked")
def another_function():
    print("Another function executed")
def button_click_with_param(param='Click'):
    print(f"Button Clicked with Parameter : {param}")




root.title("Now The Real Test")
root.geometry("500x400")
kw={'bg':'blue',
    'fg':'white'}
label=tk.Label(root,text='Welcome',**kw,font=10)
label.pack(pady=10)

button=tk.Button(root,text='Click Now!',**kw,font=10,width=10,command=on_button_click)
button1=tk.Button(root,text="Now New One!",**kw,font=15,command=another_function)
button2=tk.Button(root,text='New Button here!',**kw, font=10, command=button_click_with_param)

                  

button.pack(pady=10)
button1.pack(pady=10)
button2.pack(pady=10)

root.mainloop()






