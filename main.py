from tkinter import *
import customtkinter as ctk
from plot_generator import (
    update_plot1_with_job_titles, update_plot1_with_experience_salary,
    update_plot1_with_job_locations, update_plot2_with_common_positions,
    update_plot2_with_country_distribution, update_plot2_with_experience_distribution,
    update_plot2_with_company_size_distribution, update_plot_with_category
)

current_section = 'home'
current_plot_type = 'bar'
current_data_set = 'Average Salary'
tile1 = None
tile2 = None

root = ctk.CTk()
root.geometry('1800x800')
ctk.set_appearance_mode('system')
ctk.set_default_color_theme('green')

root.configure(bg='#1E1E1E')

# Navbar
navbar = ctk.CTkFrame(root, height=40, fg_color='#333333')
navbar.grid(row=0, column=0, columnspan=2, sticky='ew')

# Navbar grid configuration
navbar.grid_columnconfigure(0, weight=1)
navbar.grid_columnconfigure(1, weight=0)
navbar.grid_columnconfigure(2, weight=0)
navbar.grid_columnconfigure(3, weight=0)
navbar.grid_columnconfigure(4, weight=1)
navbar.grid_columnconfigure(5, weight=0)
navbar.grid_columnconfigure(6, weight=1)
navbar.grid_columnconfigure(7, weight=0)
navbar.grid_columnconfigure(8, weight=0)
navbar.grid_columnconfigure(9, weight=0)
navbar.grid_columnconfigure(10, weight=1)

navbar_label = ctk.CTkLabel(navbar, text="DS Salary Analysis App", fg_color='#333333', font=('Helvetica', 16, 'bold'))
navbar_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')

def update_plot():
    if current_section == 'home':
        update_plot1_with_job_titles(tile1)
        update_plot2_with_common_positions(tile2)
    else:
        update_plot_with_category(tile1, current_plot_type, current_section, current_data_set)

# Function for creating job buttons
def create_job_buttons():
    global job_button_frame
    job_button_frame = ctk.CTkFrame(navbar, fg_color='#333333')
    job_button_frame.grid(row=1, column=0, columnspan=11, sticky='ew')

    # Configure columns for centering buttons
    job_button_frame.grid_columnconfigure(0, weight=1)
    job_button_frame.grid_columnconfigure(1, weight=0)
    job_button_frame.grid_columnconfigure(2, weight=0)
    job_button_frame.grid_columnconfigure(3, weight=0)
    job_button_frame.grid_columnconfigure(4, weight=0)
    job_button_frame.grid_columnconfigure(5, weight=0)
    job_button_frame.grid_columnconfigure(6, weight=1)

    avg_salary_button = ctk.CTkButton(job_button_frame, text='Average Salary', command=lambda: switch_job_data_set('Average Salary'))
    avg_salary_button.grid(row=0, column=1, padx=10, pady=5)

    salary_experience_button = ctk.CTkButton(job_button_frame, text='Salary by Experience', command=lambda: switch_job_data_set('Salary by Experience'))
    salary_experience_button.grid(row=0, column=2, padx=10, pady=5)

    job_location_button = ctk.CTkButton(job_button_frame, text='Jobs by Location', command=lambda: switch_job_data_set('Jobs by Location'))
    job_location_button.grid(row=0, column=3, padx=10, pady=5)

    experience_distribution_button = ctk.CTkButton(job_button_frame, text='Experience Distribution', command=switch_to_experience_distribution)
    experience_distribution_button.grid(row=0, column=6, padx=10, pady=5)

    company_size_distribution_button = ctk.CTkButton(job_button_frame, text='Company Size Distribution', command=switch_to_company_size_distribution)
    company_size_distribution_button.grid(row=0, column=7, padx=10, pady=5)

def show_job_buttons():
    home_button.grid_remove()
    experience_salary_button.grid_remove()
    job_location_button.grid_remove()
    create_job_buttons()

def switch_job_data_set(data_set):
    global current_data_set
    current_data_set = data_set
    update_plot()

# Functions for switching sections
def switch_to_home():
    global current_section, current_data_set
    current_section = 'home'
    current_data_set = 'Average Salary'
    update_plot1_with_job_titles(tile1)
    update_plot2_with_common_positions(tile2)
    current_section_label.configure(text='Home')

def switch_to_home_avg_salary():
    global current_data_set
    current_data_set = 'Average Salary'
    update_plot1_with_job_titles(tile1)

def switch_to_home_experience_salary():
    global current_data_set
    current_data_set = 'Salary by Experience'
    update_plot1_with_experience_salary(tile1)

def switch_to_home_job_location():
    global current_data_set
    current_data_set = 'Jobs by Location'
    update_plot1_with_job_locations(tile1)

def switch_to_home_country_distribution():
    global current_data_set
    current_data_set = 'Country Distribution'
    update_plot2_with_country_distribution(tile2)

def switch_to_home_experience_distribution():
    global current_data_set
    current_data_set = 'Experience Distribution'
    update_plot2_with_experience_distribution(tile2)

def switch_to_home_company_size_distribution():
    global current_data_set
    current_data_set = 'Company Size Distribution'
    update_plot2_with_company_size_distribution(tile2)



def switch_to_experience_salary():
    global current_data_set
    current_data_set = 'Salary by Experience'
    update_plot()

def switch_to_job_location():
    global current_data_set
    current_data_set = 'Jobs by Location'
    update_plot()

def switch_to_job_titles():
    global current_data_set
    current_data_set = 'Average Salary'
    update_plot()

def switch_to_country_distribution():
    global current_data_set
    current_data_set = 'Country Distribution'
    update_plot()

def switch_to_experience_distribution():
    global current_data_set
    current_data_set = 'Experience Distribution'
    update_plot()

def switch_to_company_size_distribution():
    global current_data_set
    current_data_set = 'Company Size Distribution'
    update_plot()

# PIE CHART BUTTONS - shifted to the right
country_distribution_button = ctk.CTkButton(navbar, text='Country Distribution', command=switch_to_country_distribution)
country_distribution_button.grid(row=0, column=7, padx=(0, 10), pady=5, sticky='e')

experience_distribution_button = ctk.CTkButton(navbar, text='Experience Distribution', command=switch_to_experience_distribution)
experience_distribution_button.grid(row=0, column=8, padx=(0, 10), pady=5, sticky='e')

company_size_distribution_button = ctk.CTkButton(navbar, text='Company Size Distribution', command=switch_to_company_size_distribution)
company_size_distribution_button.grid(row=0, column=9, padx=(0, 10), pady=5, sticky='e')

# TITLE LABEL
current_section_label = ctk.CTkLabel(navbar, text='Home', fg_color='#333333', font=('Helvetica', 20, 'bold'))
current_section_label.grid(row=0, column=5, padx=60, pady=10, sticky='w')

# BAR CHART BUTTONS
home_button = ctk.CTkButton(navbar, text='Average Salary', command=switch_to_home_avg_salary)
home_button.grid(row=0, column=1, padx=10, pady=5)

experience_salary_button = ctk.CTkButton(navbar, text='Salary by Experience', command=switch_to_home_experience_salary)
experience_salary_button.grid(row=0, column=2, padx=10, pady=5)

job_location_button = ctk.CTkButton(navbar, text='Jobs by Location', command=switch_to_home_job_location)
job_location_button.grid(row=0, column=3, padx=10, pady=5)
# Sidebar
side_frame = ctk.CTkFrame(root, width=200, height=200, corner_radius=0, fg_color='#2C2C2C')
side_frame.grid(row=1, column=0, sticky='ns')

# Grid layout
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(1, weight=1)

# Mainframe
main_frame = ctk.CTkFrame(root, corner_radius=0, fg_color='#1E1E1E')
main_frame.grid(row=1, column=1, sticky='nsew')

# Grid layout in mainframe
main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_columnconfigure(1, weight=0)
main_frame.grid_columnconfigure(2, weight=1)
main_frame.grid_columnconfigure(3, weight=10)
main_frame.grid_columnconfigure(4, weight=1)

main_frame.grid_rowconfigure(0, weight=1)
main_frame.grid_rowconfigure(1, weight=10)
main_frame.grid_rowconfigure(2, weight=1)

# Tiles
tile1 = ctk.CTkFrame(main_frame, fg_color='#2C2C2C')
tile1.grid(row=1, column=1, padx=(10, 5), pady=(10, 5), sticky='nsew')

tile2 = ctk.CTkFrame(main_frame, fg_color='#2C2C2C')
tile2.grid(row=1, column=3, padx=(5, 10), pady=(10, 5), sticky='nsew')

# Initially load the default plots
switch_to_home()

# Sidebar buttons
def clear_main_frame():
    for widget in main_frame.winfo_children():
        widget.destroy()

def show_category_analysis(category):
    clear_main_frame()
    current_section_label.configure(text=category)
    global current_section
    current_section = category

    main_frame.grid_columnconfigure(0, weight=1)
    main_frame.grid_columnconfigure(1, weight=1)
    main_frame.grid_columnconfigure(2, weight=1)
    main_frame.grid_columnconfigure(3, weight=1)
    main_frame.grid_columnconfigure(4, weight=1)
    main_frame.grid_columnconfigure(5, weight=1)
    main_frame.grid_columnconfigure(6, weight=1)

    main_frame.grid_rowconfigure(0, weight=1)
    main_frame.grid_rowconfigure(1, weight=1)
    main_frame.grid_rowconfigure(2, weight=1)
    main_frame.grid_rowconfigure(3, weight=1)

    # Frame for plot
    global tile1
    tile1 = ctk.CTkFrame(main_frame, fg_color='#2C2C2C')
    tile1.grid(row=1, column=2, columnspan=3, padx=(10, 5), pady=(10, 5), sticky='nsew')

    # Frame for buttons
    button_frame = ctk.CTkFrame(main_frame, fg_color='#2C2C2C')
    button_frame.grid(row=2, column=2, columnspan=3, padx=(10, 5), pady=(10, 5), sticky='nsew')

    # Buttons to switch between plot types
    bar_chart_button = ctk.CTkButton(button_frame, text='Bar Chart', command=lambda: switch_plot_type('bar'))
    bar_chart_button.pack(side=LEFT, padx=10)

    pie_chart_button = ctk.CTkButton(button_frame, text='Pie Chart', command=lambda: switch_plot_type('pie'))
    pie_chart_button.pack(side=LEFT, padx=10)

    box_plot_button = ctk.CTkButton(button_frame, text='Box Plot', command=lambda: switch_plot_type('box'))
    box_plot_button.pack(side=LEFT, padx=10)

    # Default plot
    update_plot_with_category(tile1, 'bar', category, current_data_set)
    show_job_buttons()

def switch_plot_type(plot_type):
    global current_plot_type
    current_plot_type = plot_type
    update_plot()

def switch_data_set(data_set):
    global current_data_set
    current_data_set = data_set
    update_plot()

def toggle_job_titles():
    if job_titles_frame.winfo_ismapped():
        job_titles_frame.grid_remove()
    else:
        job_titles_frame.grid()

job_titles_button = ctk.CTkButton(
    side_frame,
    text='Job Titles',
    width=180,
    height=40,
    fg_color='#2C2C2C',
    command=toggle_job_titles,
    font=('Helvetica', 18, 'bold')
)
job_titles_button.grid(row=2, column=0, pady=5)

job_titles_frame = ctk.CTkFrame(side_frame, fg_color='#2C2C2C')
job_titles_frame.grid(row=3, column=0, sticky='ew', padx=5, pady=5)
job_titles_frame.grid_remove()

job_titles = [
    ('Data Scientists', lambda: show_category_analysis('Data Scientists')),
    ('Data Engineers', lambda: show_category_analysis('Data Engineers')),
    ('ML Engineers', lambda: show_category_analysis('ML Engineers')),
    ('AI Specialists', lambda: show_category_analysis('AI Specialists')),
    ('DS Management', lambda: show_category_analysis('DS Management')),
    ('Research Roles', lambda: show_category_analysis('Research Roles')),
    ('Business Intelligence', lambda: show_category_analysis('Business Intelligence')),
    ('Specialized Analysts', lambda: show_category_analysis('Specialized Analysts')),
    ('Architects', lambda: show_category_analysis('Architects')),
    ('Miscellaneous', lambda: show_category_analysis('Miscellaneous'))
]


for title, func in job_titles:
    title_button = ctk.CTkButton(
        job_titles_frame,
        text=title,
        width=180,
        height=40,
        fg_color='#2C2C2C',
        command=func,
        font=('Helvetica', 13)
    )
    title_button.pack(pady=5)

# About button
about_button = ctk.CTkButton(
    side_frame,
    text='About',
    width=180,
    height=40,
    fg_color='#2C2C2C',
    font=('Helvetica', 18, 'bold')
)
about_button.grid(row=4, column=0, pady=5)

bottom_spacer = ctk.CTkFrame(side_frame, fg_color='#2C2C2C')
bottom_spacer.grid(row=5, column=0, sticky='ew')

# Run
root.mainloop()
