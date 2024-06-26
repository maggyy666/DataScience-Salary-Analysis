from tkinter import *
import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import matplotlib.pyplot as plt


root = ctk.CTk()
root.geometry('1800x800')
ctk.set_appearance_mode('system')
ctk.set_default_color_theme('blue')

root.configure(bg='#1E1E1E')

# Navbar
navbar = ctk.CTkFrame(root, height=40, fg_color='#333333')
navbar.grid(row=0, column=0, columnspan=2, sticky='ew')

# Placeholder for buttons
navbar.grid_columnconfigure(0, weight=1)
navbar_label = ctk.CTkLabel(navbar, text="My Dashboard", fg_color='#333333', font=('Helvetica', 16, 'bold'))
# Navbar grid configuration
navbar.grid_columnconfigure(1, weight=0)
navbar.grid_columnconfigure(2, weight=0)
navbar.grid_columnconfigure(3, weight=0)
navbar.grid_columnconfigure(4, weight=1)  # This creates a spacer between left and right aligned buttons
navbar.grid_columnconfigure(5, weight=0)
navbar.grid_columnconfigure(6, weight=0)
navbar.grid_columnconfigure(7, weight=0)
navbar_label = ctk.CTkLabel(navbar, text="Data Science Salary Analysis App", fg_color='#333333', font=('Helvetica', 16, 'bold'))
navbar_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')

# Adding buttons to the navbar
def switch_to_home():
    update_plot1_with_job_titles()
    update_plot2_with_common_positions()

def switch_to_experience_salary():
    update_plot1_with_experience_salary()
    update_plot2_with_common_positions()

def switch_to_job_location():
    update_plot1_with_job_locations()
    update_plot2_with_common_positions()

home_button = ctk.CTkButton(navbar, text='Home', command=switch_to_home)
def switch_to_job_titles():
    update_plot1_with_job_titles()

#Func for PIE CHART BUTTONS
def switch_to_country_distribution():
    update_plot2_with_country_distribution()

def switch_to_experience_distribution():
    update_plot2_with_experience_distribution()

def switch_to_company_size_distribution():
    update_plot2_with_company_size_distribution()



#PIE CHART BUTTONS - shifted to the right
country_distribution_button = ctk.CTkButton(navbar, text='Country Distribution', command=switch_to_country_distribution)
country_distribution_button.grid(row=0, column=4, padx=(0, 10), pady=5, sticky='e')

experience_distribution_button = ctk.CTkButton(navbar, text='Experience Distribution', command=switch_to_experience_distribution)
experience_distribution_button.grid(row=0, column=5, padx=(0, 10), pady=5, sticky='e')

company_size_distribution_button = ctk.CTkButton(navbar, text='Company Size Distribution', command=switch_to_company_size_distribution)
company_size_distribution_button.grid(row=0, column=6, padx=(0, 10), pady=5, sticky='e')



#BAR CHART BUTTONS
home_button = ctk.CTkButton(navbar, text='Average Salary', command=switch_to_job_titles)
home_button.grid(row=0, column=1, padx=10, pady=5)

experience_salary_button = ctk.CTkButton(navbar, text='Salary by Experience', command=switch_to_experience_salary)
experience_salary_button.grid(row=0, column=2, padx=10, pady=5)

job_location_button = ctk.CTkButton(navbar, text='Jobs by Location', command=switch_to_job_location)
job_location_button.grid(row=0, column=3, padx=10, pady=5)

# Sidebar
side_frame = ctk.CTkFrame(root, width=200, height=200, corner_radius=0, fg_color='#2C2C2C')
side_frame.grid(row=1, column=0, sticky='ns')

# Grid @layout
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(1, weight=1)

# Mainframe
main_frame = ctk.CTkFrame(root, corner_radius=0, fg_color='#1E1E1E')
main_frame.grid(row=1, column=1, sticky='nsew')

# Grid @mainframe
main_frame.grid_columnconfigure(0, weight=1)  # Left spacer
main_frame.grid_columnconfigure(1, weight=0)  # Tile 1
main_frame.grid_columnconfigure(2, weight=1)  # Spacer between
main_frame.grid_columnconfigure(3, weight=10)  # Tile 2
main_frame.grid_columnconfigure(4, weight=1)  # Right Spacer

main_frame.grid_rowconfigure(0, weight=1)  # Top spacer
main_frame.grid_rowconfigure(1, weight=10)  # Tiles row
main_frame.grid_rowconfigure(2, weight=1)  # Bottom spacer

# Tiles
tile1 = ctk.CTkFrame(main_frame, fg_color='#2C2C2C')
tile1.grid(row=1, column=1, padx=(10, 5), pady=(10, 5), sticky='nsew')

tile2 = ctk.CTkFrame(main_frame, fg_color='#2C2C2C')
tile2.grid(row=1, column=3, padx=(5, 10), pady=(10, 5), sticky='nsew')

# Load data
data = pd.read_csv('ds_salaries.csv')

# Plot functions
def update_plot1_with_job_titles():
    data = pd.read_csv('ds_salaries.csv')
    salary_per_title = data.groupby('job_title')['salary_in_usd'].mean().sort_values(ascending=False)
    selected_jobs = pd.concat([salary_per_title.head(3), salary_per_title.tail(3), salary_per_title[3:-3].sample(4)]).reset_index()
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.barh(selected_jobs['job_title'], selected_jobs['salary_in_usd'], height=0.8, color='#5bc0de')
    style_plot(fig, ax, 'Average Salary per Job in Data Science', 'Average Salary in USD')
    plot_on_tile(fig, tile1)


def update_plot1_with_experience_salary():
    experience_salary = data.groupby('experience_level')['salary_in_usd'].mean().sort_values()
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.barh(experience_salary.index, experience_salary.values, color='#5bc0de')
    style_plot(fig, ax, 'Average Salary by Experience Level', 'Average Salary in USD')
    plot_on_tile(fig, tile1)

def update_plot1_with_job_locations():
    job_location = data['company_location'].value_counts().head(10)
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.barh(job_location.index, job_location.values, color='#5bc0de')
    style_plot(fig, ax, 'Top 10 Job Locations', 'Number of Job Titles')
    plot_on_tile(fig, tile1)

def update_plot2_with_common_positions():
    job_count = data['job_title'].value_counts().head(5)
    fig, ax = plt.subplots()
    wedges, texts, autotexts = ax.pie(
        job_count,
        labels=job_count.index,
        autopct=lambda pct: format_label(pct, job_count.values),
        textprops={'color':'white'},
        startangle=140,
        colors=plt.cm.Paired(range(len(job_count)))
    )
    ax.set_title('Top 5 Most Common Positions in the DS Industry', color='white', fontsize=12)
    fig.patch.set_facecolor('#2C2C2C')
    ax.set_facecolor('#1E1E1E')
    plt.gca().set_aspect('equal')
    plot_on_tile(fig, tile2)

def style_plot(fig, ax, title, xlabel):
    ax.set_facecolor('#1E1E1E')
    fig.patch.set_facecolor('#2C2C2C')
    ax.spines['bottom'].set_color('white')
    ax.spines['top'].set_color('white')
    ax.spines['right'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    ax.set_xlabel(xlabel, fontsize=12, color='white', wrap=True)
    ax.set_title(title, fontsize=10, color='white')
    for label in ax.get_yticklabels():
        label.set_fontsize(8)
        label.set_color('white')
    for label in ax.get_xticklabels():
        label.set_fontsize(8)
        label.set_color('white')
    ax.grid(True, axis='x', color='gray', linestyle='--', linewidth=0.5)

def plot_on_tile(fig, tile):
    for widget in tile.winfo_children():
        widget.destroy()
    canvas = FigureCanvasTkAgg(fig, master=tile)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=BOTH, expand=True, padx=20, pady=20)

def format_label(pct, allvalues):
    absolute = int(pct/100*sum(allvalues))
    return "{:.1f}%\n({:d})".format(pct, absolute)

# Initially load the default plots
switch_to_home()
# Function to toggle the display of Job Titles options
def toggle_job_titles():
    if job_titles_frame.winfo_ismapped():
        job_titles_frame.grid_remove()
    else:
        job_titles_frame.grid()
# Top spacers / buttons
top_spacer = ctk.CTkFrame(side_frame, fg_color='#2C2C2C')
top_spacer.grid(row=0, column=0, sticky='ew')

home_button = ctk.CTkButton(
    side_frame,
    text='Home',
    width=180,
    height=40,
    fg_color='#2C2C2C',
    font=('Helvetica', 18, 'bold')
)
home_button.grid(row=1, column=0, pady=5)

# Job Titles button with toggle functionality
job_titles_button = ctk.CTkButton(
    side_frame,
    text='Job Titles v',
    width=180,
    height=40,
    fg_color='#2C2C2C',
    command=toggle_job_titles,
    font=('Helvetica',18,'bold')
)
job_titles_button.grid(row=2, column=0, pady=5)

# Frame for Job Titles options
job_titles_frame = ctk.CTkFrame(side_frame, fg_color='#2C2C2C')
job_titles_frame.grid(row=3, column=0, sticky='ew', padx=5, pady=5)
job_titles_frame.grid_remove()  # Initially hide the Job Titles options

# Add options under Job Titles
job_titles = [
    'Data Scientists',
    'Data Engineers',
    'ML & AI Specialists',
    'DS Management',
    'Research Roles',
    'Miscellaneous'
]

for title in job_titles:
    title_button = ctk.CTkButton(
        job_titles_frame,
        text=title,
        width=180,
        height=40,
        fg_color='#2C2C2C',
        command=lambda t=title: print(f"{t} button pressed")
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

