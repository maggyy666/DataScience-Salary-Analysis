import tkinter as tk

root = tk.Tk()
label1 = tk.Label(root,text="Label1")
label2 = tk.Label(root, text="Label2")
label1.pack()
label2.pack()
root = ctk.CTk()
root.geometry('1400x600')
root.title("Application")
ctk.set_appearance_mode("system")
ctk.set_default_color_theme('blue')

root.mainloop()
root.mainloop()