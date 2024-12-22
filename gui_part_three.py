import tkinter as mytk
from tkinter import ttk, messagebox

# Function to show a dialog box
def show_info_dialog():
    messagebox.showinfo("Dialog Box", 'This is a dialog box')

# Function to show a message box
def show_info_message():
    messagebox.showinfo("Message Box", 'This is a message box')

# Function to save the list box selection
def save_list_box_selection():
    selected_items = list_box.curselection()
    selected_text = [list_box.get(i) for i in selected_items]  # Get text for selected indices
    print(f"Selected Indices: {selected_items}")
    print(f"Selected Items: {selected_text}")  # Fix: Print the actual text of the selected items

root = mytk.Tk()
root.title("Tkinter Widgets Example.")
root.geometry("400x400")

# Paned Window
panded_window = ttk.PanedWindow(root, orient=mytk.HORIZONTAL)
panded_window.pack(fill=mytk.BOTH, expand=True)

# Frame for the left side of the Paned Window
left_frame = ttk.Frame(panded_window, width=100, height=300, relief=mytk.SUNKEN)
panded_window.add(left_frame, weight=1)

# Frame for the right side of the Paned Window
right_frame = ttk.Frame(panded_window, width=100, height=300, relief=mytk.SUNKEN)
panded_window.add(right_frame, weight=4)

# Scrollbar and text widget
text_widget = mytk.Text(left_frame, wrap="word", height=10)
scroll_bar1 = ttk.Scrollbar(left_frame, orient='vertical', command=text_widget.yview)
text_widget.configure(yscrollcommand=scroll_bar1.set)
text_widget.grid(row=0, column=1, sticky='ns')

left_frame.grid_columnconfigure(0, weight=1)

# List box with scrollbar
list_box = mytk.Listbox(left_frame)
scroll_bar2 = ttk.Scrollbar(left_frame, orient='vertical', command=list_box.yview)
list_box.configure(yscrollcommand=scroll_bar2.set)
list_box.grid(row=1, column=0, sticky='ew', pady=10)
scroll_bar2.grid(row=1, column=1, sticky='ns')  # Add scrollbar for the list box

# Populate list box with items
for item in ["Python", 'WordPress', 'SEO', 'Shopify']:
    list_box.insert(mytk.END, item)

# Spin box
spin_box = mytk.Spinbox(left_frame, from_=0, to=10)
spin_box.grid(row=2, column=0, sticky='ew', pady=10)

# Menu Button
menu_button = mytk.Menubutton(right_frame, text="Menu Button", relief=mytk.RAISED)
menu = mytk.Menu(menu_button, tearoff=0)
menu_button.config(menu=menu)
menu.add_command(label='Python')
menu.add_command(label="WordPress")
menu.add_command(label="Shopify")
menu.add_command(label="SEO")
menu_button.pack(pady=20)

# Button to show Dialog Box
dialog_button = mytk.Button(right_frame, text="Show Dialog", command=show_info_dialog)
dialog_button.pack(pady=20)

# Button to show Message Box
message_button = mytk.Button(right_frame, text="Show Message", command=show_info_message)
message_button.pack(pady=20)

# Button to save Listbox selection
save_button = mytk.Button(right_frame, text="Save ListBox selection", command=save_list_box_selection)
save_button.pack(pady=20)

root.mainloop()
