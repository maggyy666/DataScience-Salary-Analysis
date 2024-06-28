import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import BOTH

experience_level_mapping = {
    'EX': 'Executive-level/Director',
    'SE': 'Senior-level/Expert',
    'MI': 'Mid-level/Intermediate',
    'EN': 'Entry-level/Junior'
}

country_names_mapping = {
    'IN': 'India',
    'US': 'United States',
    'CA': 'Canada',
    'DE': 'Germany',
    'FR': 'France',
    'GB': 'United Kingdom',
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
