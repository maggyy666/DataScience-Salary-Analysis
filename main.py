from tkinter import *
import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from plot_generator import generate_plot
from plot_generator import generate_pie_chart

root = ctk.CTk()
root.geometry('1800x800')
ctk.set_appearance_mode('system')
ctk.set_default_color_theme('blue')

root.configure(bg='#1E1E1E')

#Navbar
navbar = ctk.CTkFrame(root,height=20,fg_color='#333333')
navbar.grid(row=0,column=0,columnspan=2,sticky='ew')
# Navbar
navbar = ctk.CTkFrame(root, height=40, fg_color='#333333')
navbar.grid(row=0, column=0, columnspan=2, sticky='ew')

# Placeholder for buttons
navbar.grid_columnconfigure(0, weight=1)
navbar_label = ctk.CTkLabel(navbar, text="My Dashboard", fg_color='#333333', font=('Helvetica', 16, 'bold'))
navbar_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')

# Adding buttons to the navbar
def switch_to_home():
    update_plot1_with_job_titles()
    update_plot2_with_common_positions()

def switch_to_experience_salary():
    update_plot1_with_experience_salary()
    update_plot2_with_common_positions()

#Placeholder for buttons
navbar.grid_columnconfigure(0,weight=1)
navbar_label = ctk.CTkLabel(navbar,text="My Dashboard",fg_color='#333333')
navbar_label.grid(row=0,column=0,padx=1,pady=1,sticky='w')


#sidebar
side_frame = ctk.CTkFrame(root, width=200, height=200, corner_radius=0, fg_color='#2C2C2C')
side_frame.grid(row=1, column=0, sticky='ns')

#grid @layout
root.grid_columnconfigure(1,weight=1)
root.grid_rowconfigure(1,weight=1)

#mainframe
main_frame = ctk.CTkFrame(root, corner_radius=0, fg_color='#1E1E1E')
main_frame.grid(row=1, column=1, sticky='nsew')

#grid @mainframe
main_frame.grid_columnconfigure(0, weight=1)  #left spacer
main_frame.grid_columnconfigure(1, weight=0)  #Tile 1
main_frame.grid_columnconfigure(2, weight=1)  #Spacer between
main_frame.grid_columnconfigure(3, weight=10)  #Tile 2
main_frame.grid_columnconfigure(4, weight=1)  #Right Spacer

main_frame.grid_rowconfigure(1, weight=1)  #Top spacer
main_frame.grid_rowconfigure(2, weight=10)  #Tiles row
main_frame.grid_rowconfigure(3, weight=1)  # Bottom spacer

#tiles
tile1 = ctk.CTkFrame(main_frame, fg_color='#2C2C2C')
tile1.grid(row=1, column=1, padx=(10,5), pady=(10,5), sticky='nsew')

tile2 = ctk.CTkFrame(main_frame, fg_color='#2C2C2C')
tile2.grid(row=1, column=3, padx=(5,10), pady=(10,5), sticky='nsew')

#plot in tiles
def add_plot(tile):
    fig = generate_plot()
    canvas = FigureCanvasTkAgg(fig, tile)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=BOTH, expand=True, padx=20, pady=20)
add_plot(tile1)

def add_pie_chart(tile):
    fig = generate_pie_chart()
    canvas = FigureCanvasTkAgg(fig, tile)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=BOTH, expand=True)
add_pie_chart(tile2)



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
#run
root.mainloop()