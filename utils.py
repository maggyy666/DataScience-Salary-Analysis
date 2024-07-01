import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import BOTH

experience_level_mapping = {
    'EX': 'Executive-level/Director',
    'SE': 'Senior-level/Expert',
    'MI': 'Mid-level/Intermediate',
    'EN': 'Entry-level/Junior'
}

job_categories = {
    'Data Scientists': ['Data Scientist', 'Applied Scientist', 'Applied Data Scientist', 'Business Data Analyst', 'Staff Data Scientist', 'Lead Data Scientist', 'Product Data Scientist', 'Principal Data Scientist', 'Data Scientist Lead'],
    'Data Engineers': ['Data Engineer', 'Data Modeler', 'Analytics Engineer', 'ETL Engineer', 'Data DevOps Engineer', 'BI Data Engineer', 'Data Infrastructure Engineer', 'Software Data Engineer', 'Cloud Database Engineer', 'Azure Data Engineer', 'Marketing Data Engineer', 'Cloud Data Engineer', 'Lead Data Engineer', 'Principal Data Engineer'],
    'ML Engineers': ['ML Engineer', 'Machine Learning Engineer', 'Applied Machine Learning Engineer', 'Machine Learning Scientist', 'Deep Learning Engineer', 'Machine Learning Software Engineer', 'Machine Learning Research Engineer', 'NLP Engineer', 'Machine Learning Developer', 'Principal Machine Learning Engineer', 'Lead Machine Learning Engineer'],
    'AI Specialists': ['AI Developer', 'AI Scientist', 'AI Programmer', 'Autonomous Vehicle Technician', 'Applied Machine Learning Scientist', 'Principal Machine Learning Engineer', 'Machine Learning Manager'],
    'DS Management': ['Head of Data', 'Data Science Manager', 'Data Manager', 'Director of Data Science', 'Head of Data Science', 'Data Science Lead', 'Data Analytics Manager', 'Head of Machine Learning', 'Data Science Tech Lead'],
    'Research Roles': ['Research Engineer', 'Research Scientist', 'Deep Learning Researcher', 'Machine Learning Researcher', '3D Computer Vision Researcher'],
    'Business Intelligence': ['BI Data Engineer', 'BI Developer', 'BI Analyst', 'BI Data Analyst', 'Power BI Developer', 'Business Intelligence Engineer'],
    'Specialized Analysts': ['Data Analyst', 'Data Quality Analyst', 'Compliance Data Analyst', 'Financial Data Analyst', 'Marketing Data Analyst', 'Insight Analyst', 'Product Data Analyst'],
    'Architects': ['Data Architect', 'Principal Data Architect', 'Big Data Architect', 'Cloud Data Architect'],
    'Miscellaneous': ['Data Strategist', 'Data Specialist', 'Lead Data Analyst', 'MLOps Engineer', 'Data Operations Engineer', 'Data Science Consultant', 'Data Analytics Specialist', 'Machine Learning Infrastructure Engineer', 'Data Analytics Lead', 'Data Lead', 'Data Science Engineer', 'Manager Data Management', 'Data Analytics Engineer', 'Data Analytics Consultant', 'Data Management Specialist', 'Data Operations Analyst', 'Principal Data Analyst', 'Finance Data Analyst']
}



country_names_mapping = {
    'IN': 'India',
    'US': 'United\nStates',
    'CA': 'Canada',
    'DE': 'Germany',
    'FR': 'France',
    'GB': 'United\nKingdom',
    'ES': 'Spain',
    'AU': 'Australia',
    'BR': 'Brazil',
    'NL': 'Netherlands',
    'IT': 'Italy',
    'CH': 'Switzerland',
    'AT': 'Austria',
    'SG': 'Singapore',
    'PL': 'Poland',
    'BE': 'Belgium',
    'IE': 'Ireland',
    'IL': 'Israel',
    'MX': 'Mexico',
    'SE': 'Sweden',
    'JP': 'Japan',
    'NZ': 'New\nZealand',
    'RU': 'Russia',
    'PR': 'Puerto\nRico',
    'BA': 'Bosnia\nand\nHerzegovina'
}

employment_type_mapping = {
    'CT': 'Contract',
    'FL': 'Freelance',
    'PT': 'Part-time',
    'FT': 'Full-time',
    'IN': 'Internship'
}
company_size_mapping = {
    'S': 'Small [<50]',
    'M': 'Medium [<249]',
    'L': 'Large [>250]'
}

def load_data():
    return pd.read_csv('ds_salaries.csv')

def style_plot(fig, ax, title, xlabel):
    ax.set_facecolor('#1E1E1E')
    fig.patch.set_facecolor('#2C2C2C')
    fig.subplots_adjust(left=0.2)
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
    canvas.get_tk_widget().pack(fill=BOTH, expand=True, padx=15, pady=20)

def format_label(pct, allvalues):
    absolute = int(pct / 100 * sum(allvalues))
    return "{:.1f}%\n({:d})".format(pct, absolute)
