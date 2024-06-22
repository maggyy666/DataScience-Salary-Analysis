from tkinter import *
import customtkinter as ctk

root = ctk.CTk()
root.geometry('1400x600')
ctk.set_appearance_mode('system')
ctk.set_default_color_theme('blue')

root.configure(bg='#1E1E1E')

#sidebar
side_frame = ctk.CTkFrame(root, width=200, height=200, corner_radius=0, fg_color='#2C2C2C')
side_frame.grid(row=0,column=0,sticky='ns')

#grid @layout
root.grid_columnconfigure(1,weight=1)
root.grid_rowconfigure(0,weight=1)

#mainframe
main_frame = ctk.CTkFrame(root,corner_radius=0,fg_color='#1E1E1E')
main_frame.grid(row=0,column=1,sticky='nsew')

#grid @mainframe
main_frame.grid_rowconfigure(0,weight=1) #top spacer
main_frame.grid_rowconfigure(1,weight=10) #bottom spacer
main_frame.grid_rowconfigure(2,weight=1) #middle row

main_frame.grid_columnconfigure(0,weight=1) #left spacer
main_frame.grid_columnconfigure(1,weight=0) #middle
main_frame.grid_columnconfigure(2,weight=1) #right spacer

#tiles
tile1 = ctk.CTkFrame(main_frame,fg_color='#2C2C2C')
tile2 = ctk.CTkFrame(main_frame,fg_color='#2C2C2C')

#Tiles w/ padding
tile1.grid(row=1, column=0, padx=(20,10), pady=(20,10), sticky='nsew')
tile2.grid(row=1, column=2, padx=(10,20), pady=(20,10), sticky='nsew')

#top spacers / buttons
top_spacer = ctk.CTkFrame(side_frame,fg_color='#2C2C2C')
top_spacer.grid(row=0,column=0,sticky='ew')

buttons = ['Home','About']
for text in buttons:
    button = ctk.CTkButton(
        side_frame,
        text=text,
        width=180,
        height=40,
        fg_color='#2C2C2C'
    )
    button.grid(pady=5)
bottom_spacer = ctk.CTkFrame(side_frame, fg_color='#2C2C2C')
bottom_spacer.grid(row=len(buttons)+1,column=0,sticky='ew')
root.mainloop()