import tkinter as mytk
from tkinter import ttk


# Creating a function to save the input from the user.
def save_input():
    with open("input_file.txt","w") as file:
        file.write(f"Text Entry : {entry_text.get()}\n")
        file.write(f"Combo Box : {combo_var.get()}\n")
        file.write(f"Check Button : {check_var.get()}\n")
        file.write(f"Radio Button : {radio_var.get()}\n")

    print("Inputs Saved to 'input_file.txt' . ")
    


root=mytk.Tk()
root.title("Tkinter widgets Examples")        
root.geometry("500x500")
# root.state("zoomed")

#Create and place the Entry Text Box
entry_label=mytk.Label(root,text="Enter some text ")
entry_label.pack(pady=5)
entry_text=mytk.Entry(root)
entry_text.pack(pady=5)

# Create and place the Combo Box
combo_label=mytk.Label(root,text="Choose an Option")
combo_label.pack(pady=5)
combo_var=mytk.StringVar()
combo_box=ttk.Combobox(root,textvariable=combo_var)
combo_box['values']=('Python','WordPress',"E-Commerce",'AI Prompt Engineering')
combo_box.current(0)
combo_box.pack(pady=5)

# Create and place the radio button
radio_label=mytk.Label(root,text="Choose an Option.")
radio_label.pack(pady=5)
radio_var=mytk.StringVar()
radio_button1=mytk.Radiobutton(root,text="Python",variable=radio_var,value="Option A= Python")
radio_button1.pack(pady=5)
radio_button2=mytk.Radiobutton(root,text="WordPress",variable=radio_var,value="Option B= WordPress")
radio_button2.pack(pady=5)


#Create and plae the check Button
check_var=mytk.BooleanVar()
check_button=mytk.Checkbutton(root,text="Varify, you are Human.",variable=check_var)
check_button.pack(pady=5)

# Create and Place the Save Button
save_button=mytk.Button(root,text="Save Inputs",command=save_input)
save_button.pack(pady=5)






root.mainloop()