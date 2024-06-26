import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def generate_plot(dataset):
    if dataset == 'job_titles':
        data = pd.read_csv('ds_salaries.csv')
        salary_per_title = data.groupby('job_title')['salary_in_usd'].mean().sort_values(ascending=False)

        top_jobs = salary_per_title.head(3)
        bottom_jobs = salary_per_title.tail(3)
        middle_jobs = salary_per_title[3:-3].sample(4).sort_values(ascending=False)
        selected_jobs = pd.concat([top_jobs, middle_jobs, bottom_jobs])
        selected_jobs = selected_jobs.reset_index()

    bar_width = 0.6
    ax.barh(selected_jobs['job_title'],selected_jobs['salary_in_usd'],height=bar_width,color='#5bc0de')

    #design
    ax.set_facecolor('#1E1E1E')
    fig.patch.set_facecolor('#2C2C2C')

        ax.set_facecolor('#1E1E1E')
        fig.patch.set_facecolor('#2C2C2C')

        fig.subplots_adjust(left=0.30, right=0.95, top=0.85, bottom=0.15)
        ax.margins(x=0)

        ax.spines['bottom'].set_color('white')
        ax.spines['top'].set_color('white')
        ax.spines['right'].set_color('white')
        ax.spines['left'].set_color('white')
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')

        ax.set_xlabel('Average Salary in USD', fontsize=12, color='white', wrap=True)
        ax.set_title('Average Salary per Job in Data Science', fontsize=10, color='white')

    #Set x-axis limit to show max value
    max_salary = selected_jobs['salary_in_usd'].max()
    ax.set_xlim(0,max_salary*1.1)
        ax.grid(True, axis='x', color='gray', linestyle='--', linewidth=0.5)

        max_salary = selected_jobs['salary_in_usd'].max()
        ax.set_xlim(0, max_salary * 1.1)

        for label in ax.get_yticklabels():
            label.set_fontsize(8)
            label.set_color('white')
        for label in ax.get_xticklabels():
            label.set_fontsize(8)
            label.set_color('white')

        return fig

    elif dataset == 'experience_level':
        data = pd.read_csv('ds_salaries.csv')
        experience_salary = data.groupby('experience_level')['salary_in_usd'].mean().sort_values()
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.barh(experience_salary.index, experience_salary.values, color='#5bc0de')
        style_plot(fig, ax, 'Average Salary by Experience Level', 'Average Salary in USD')
        return fig

    elif dataset == 'job_locations':
        data = pd.read_csv('ds_salaries.csv')
        job_location = data['company_location'].value_counts().head(10)
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.barh(job_location.index, job_location.values, color='#5bc0de')
        style_plot(fig, ax, 'Top 10 Job Locations', 'Number of Job Titles')
        return fig

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

        return fig


def generate_pie_chart():
    data=pd.read_csv('ds_salaries.csv')

    #grouping
    job_count = data['job_title'].value_counts().head(5)
    job_titles = job_count.index
    job_counts = job_count.values
    fig,ax=plt.subplots()

    def format_label(pct,allvalues):
        absolute = int(pct/100*sum(allvalues))
        return "{:.1f}%\n({:d})".format(pct, absolute)

    wedges,texts,autotexts = ax.pie(
        job_count,
        labels=job_titles,
        autopct=lambda pct:format_label(pct,job_counts),
        textprops={'color':'white'},
        startangle=140,
        colors=plt.cm.Paired(range(len(job_count)))
    )


    #design
    ax.set_title('Top 5 Most Common positions in the DS Industry',color='white',fontsize=12)
    fig.patch.set_facecolor('#2C2C2C')
    ax.set_facecolor('#1E1E1E')
    plt.gca().set_aspect('equal')

    ax.set_position([0.1,0.1,0.8,0.8])
    return fig    ax.set_position([0.1, 0.1, 0.8, 0.8])
    return fig


def generate_box_plot():
    data = pd.read_csv('ds_salaries.csv')

    # Create a figure and axis with a dark background
    fig, ax = plt.subplots(figsize=(12, 8))
    fig.patch.set_facecolor('#2C2C2C')
    ax.set_facecolor('#1E1E1E')

    # Create the box plot
    sns.boxplot(x='company_location', y='salary_in_usd', data=data, palette='Set3', ax=ax)

    # Set title and labels with white color
    ax.set_title('Salary Distribution by Company Location', fontsize=16, color='white')
    ax.set_xlabel('Company Location', fontsize=12, color='white')
    ax.set_ylabel('Salary in USD', fontsize=12, color='white')

    # Adjust tick parameters to match the dark theme
    ax.tick_params(axis='x', colors='white', rotation=45)
    ax.tick_params(axis='y', colors='white')

    # Remove any extra spines and set their color to white
    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_color('white')

    # Adjust layout to ensure the plot fits well within the tile
    plt.tight_layout()

    return fig


def plot_on_tile(fig, tile):
    for widget in tile.winfo_children():
        widget.destroy()
    canvas = FigureCanvasTkAgg(fig, master=tile)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=BOTH, expand=True, padx=15, pady=20)

