import matplotlib.pyplot as plt
import pandas as pd
from utils import style_plot, plot_on_tile, load_data, experience_level_mapping, country_names_mapping, company_size_mapping, format_label, job_categories, employment_type_mapping

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
    'ES': 'Spain',
    'CA': 'Canada',
    'GB': 'United Kingdom',
    'IT': 'Italy',
    'FR': 'France',
    'DE': 'Germany',
    'NL': 'Netherlands',
    'AU': 'Australia',
    'BR': 'Brazil',
    'US': 'United States',
    'CN': 'China',
    'JP': 'Japan',
    'KR': 'South Korea',
    'RU': 'Russia',
    'MX': 'Mexico',
    'AR': 'Argentina',
    'ZA': 'South Africa',
    'NG': 'Nigeria'
}
def map_country_names(country_code):
    return country_names_mapping.get(country_code, 'Other')
def update_plot1_with_job_titles(tile, category=None):
    data = load_data()
    if category and category in job_categories:
        data = data[data['job_title'].isin(job_categories[category])]
    salary_per_title = data.groupby('job_title')['salary_in_usd'].mean().sort_values(ascending=False)
    selected_jobs = pd.concat([salary_per_title.head(3), salary_per_title.tail(3), salary_per_title[3:-3].sample(4)]).reset_index()
    selected_jobs = selected_jobs.sort_values(by='salary_in_usd').reset_index(drop=True)
    fig, ax = plt.subplots(figsize=(8, 6))

    ax.barh(selected_jobs['job_title'], selected_jobs['salary_in_usd'], height=0.8, color='#5bc0de')
    style_plot(fig, ax, f'Average Salary per Job in {category if category else "Data Science"}', 'Average Salary in USD')
    plot_on_tile(fig, tile)
def format_job_title(title):
    return "\n".join(title.split())

def update_plot1_with_experience_salary(tile):
    data = load_data()
    experience_salary = data.groupby('experience_level')['salary_in_usd'].mean().sort_values()
    experience_salary.index = experience_salary.index.map(experience_level_mapping)
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.barh(experience_salary.index, experience_salary.values, color='#5bc0de')
    style_plot(fig, ax, 'Average Salary by Experience Level', 'Average Salary in USD')
    plot_on_tile(fig, tile)

def update_plot1_with_job_locations(tile):
    data = load_data()
    country_mapping = {
        'IN': 'India',
        'ES': 'Spain',
        'CA': 'Canada',
        'GB': 'United Kingdom',
        'IT': 'Italy',
        'FR': 'France',
        'DE': 'Germany',
        'NL': 'Netherlands',
        'AU': 'Australia',
        'BR': 'Brazil',
    }
    data_outside_us = data[data['company_location'] != 'US']
    job_location = data_outside_us['company_location'].value_counts().head(10)
    job_location.index = job_location.index.map(lambda x: country_mapping.get(x, 'Other'))
    fig, ax = plt.subplots(figsize=(8, 6))
    bars = ax.barh(job_location.index, job_location.values, color='#888888')
    for bar in bars:
        width = bar.get_width()
        ax.text(width + 10, bar.get_y() + bar.get_height() / 2, f'{int(width)}', ha='left', va='center', color='white', fontweight='bold')  # Add +10 to width for better spacing
    style_plot(fig, ax, 'Top 10 Job Locations (Outside US)', 'Number of Jobs')
    plot_on_tile(fig, tile)



def update_plot2_with_common_positions(tile):
    data = load_data()
    job_count = data['job_title'].value_counts().head(5)
    fig, ax = plt.subplots()
    ax.pie(job_count, labels=job_count.index, autopct=lambda pct: format_label(pct, job_count.values), textprops={'color': 'white'}, startangle=140, colors=plt.cm.Paired(range(len(job_count))))
    ax.set_title('Top 5 Most Common Positions in the DS Industry', color='white', fontsize=12)
    fig.patch.set_facecolor('#2C2C2C')
    ax.set_facecolor('#1E1E1E')
    plt.gca().set_aspect('equal')
    plot_on_tile(fig, tile)


def update_plot2_with_employment_type_distribution(tile):
    data = load_data()
    employment_type_count = data['employment_type'].value_counts()
    employment_type_count = employment_type_count[employment_type_count.index != 'FT']  # Exclude 'FT'

    employment_type_count.index = employment_type_count.index.map(employment_type_mapping)

    fig, ax = plt.subplots()
    patches, texts, autotexts = ax.pie(employment_type_count, labels=[f'{i+1}. {label}' for i, label in enumerate(employment_type_count.index)], autopct='%1.1f%%', colors=plt.cm.Paired(range(len(employment_type_count))), textprops={'color': 'white'}, startangle=140)
    ax.set_title('Distribution by Employment Type', color='white', fontsize=12)

    for text in texts + autotexts:
        text.set_color('white')

    fig.patch.set_facecolor('#2C2C2C')
    ax.set_facecolor('#1E1E1E')
    plt.gca().set_aspect('equal')

    plot_on_tile(fig, tile)
    plt.close(fig)




def update_plot2_with_experience_distribution(tile):
    data = load_data()
    experience_count = data['experience_level'].value_counts()
    experience_count.index = experience_count.index.map(experience_level_mapping)
    fig, ax = plt.subplots()
    ax.pie(experience_count, labels=experience_count.index, autopct=lambda pct: format_label(pct, experience_count.values), textprops={'color': 'white'}, startangle=140, colors=plt.cm.Paired(range(len(experience_count))))
    ax.set_title('Distribution by Experience Level', color='white', fontsize=12)
    fig.patch.set_facecolor('#2C2C2C')
    ax.set_facecolor('#1E1E1E')
    plt.gca().set_aspect('equal')
    plot_on_tile(fig, tile)

def update_plot2_with_company_size_distribution(tile):
    data = load_data()
    company_size_count = data['company_size'].value_counts()
    company_size_count.index = company_size_count.index.map(company_size_mapping)
    fig, ax = plt.subplots()
    ax.pie(company_size_count, labels=company_size_count.index, autopct=lambda pct: format_label(pct, company_size_count.values), textprops={'color': 'white'}, startangle=140, colors=plt.cm.Paired(range(len(company_size_count))))
    ax.set_title('Distribution by Company Size', color='white', fontsize=12)
    fig.patch.set_facecolor('#2C2C2C')
    ax.set_facecolor('#1E1E1E')
    plt.gca().set_aspect('equal')
    plot_on_tile(fig, tile)


def style_box_plot(ax):
    ax.set_facecolor('#1E1E1E')
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    for spine in ax.spines.values():
        spine.set_edgecolor('white')

    for label in (ax.get_xticklabels() + ax.get_yticklabels()):
        label.set_color('white')

    # Set titles with larger font size and bold weight
    ax.title.set_fontsize(14)
    ax.title.set_fontweight('bold')
    ax.xaxis.label.set_fontsize(12)
    ax.xaxis.label.set_fontweight('bold')
    ax.yaxis.label.set_fontsize(12)
    ax.yaxis.label.set_fontweight('bold')

def update_plot_with_category(tile, plot_type, category, data_set='Average Salary'):
    data = load_data()
    if category in job_categories:
        category_data = data[data['job_title'].isin(job_categories[category])].copy()
    else:
        category_data = data.copy()
    fig, ax = plt.subplots(figsize=(18, 7))

    if data_set == 'Average Salary':
        if plot_type == 'bar':
            salary_per_country = category_data.groupby('company_location')['salary_in_usd'].mean().sort_values()
            ax.barh(salary_per_country.index.map(map_country_names), salary_per_country.values, color='#5bc0de')
            style_plot(fig, ax, f'Average Salary for {category} by Country', 'Average Salary in USD')
        elif plot_type == 'pie':
            salary_per_country = category_data.groupby('company_location')['salary_in_usd'].mean().sort_values().head(10)
            ax.pie(salary_per_country, labels=salary_per_country.index.map(map_country_names), autopct='%1.1f%%', colors=plt.cm.Paired(range(len(salary_per_country))), textprops={'color': 'white'})
            ax.set_title(f'Top 10 Average Salary for {category} by Country', color='white', fontsize=14, fontweight='bold')
            fig.patch.set_facecolor('#2C2C2C')
            ax.set_facecolor('#1E1E1E')
        elif plot_type == 'box':
            data_filtered = category_data.copy()
            data_filtered['country'] = data_filtered['company_location'].map(map_country_names)
            data_filtered.boxplot(column='salary_in_usd', by='country', ax=ax)
            ax.set_title(f'Average Salary for {category} Specialties', color='white', fontsize=14, fontweight='bold')
            ax.set_xlabel('Specialty', color='white', fontsize=12, fontweight='bold')
            ax.set_ylabel('Salary in USD', color='white', fontsize=12, fontweight='bold')
            fig.suptitle('')
            fig.patch.set_facecolor('#2C2C2C')
            style_box_plot(ax)
    elif data_set == 'Salary by Experience':
        experience_salary = category_data.groupby('experience_level')['salary_in_usd'].mean().sort_values()
        experience_salary.index = experience_salary.index.map(experience_level_mapping)
        if plot_type == 'bar':
            ax.barh(experience_salary.index, experience_salary.values, color='#5bc0de')
            style_plot(fig, ax, f'Average Salary by Experience Level for {category}', 'Average Salary in USD')
        elif plot_type == 'pie':
            ax.pie(experience_salary, labels=experience_salary.index, autopct='%1.1f%%', colors=plt.cm.Paired(range(len(experience_salary))), textprops={'color': 'white'})
            ax.set_title(f'Salary by Experience Level for {category}', color='white', fontsize=14, fontweight='bold')
            fig.patch.set_facecolor('#2C2C2C')
            ax.set_facecolor('#1E1E1E')
        elif plot_type == 'box':
            category_data.loc[:, 'experience_level'] = category_data['experience_level'].map(experience_level_mapping)
            category_data.boxplot(column='salary_in_usd', by='experience_level', ax=ax)
            ax.set_title(f'Salary Distribution by Experience Level for {category}', color='white', fontsize=14, fontweight='bold')
            ax.set_xlabel('Experience Level', color='white', fontsize=12, fontweight='bold')
            ax.set_ylabel('Salary in USD', color='white', fontsize=12, fontweight='bold')
            fig.suptitle('')
            fig.patch.set_facecolor('#2C2C2C')
            style_box_plot(ax)
    elif data_set == 'Jobs by Location':
        country_distribution = category_data['company_location'].value_counts().head(10)
        country_distribution.index = country_distribution.index.map(map_country_names)
        if plot_type == 'bar':
            ax.barh(country_distribution.index, country_distribution.values, color='#5bc0de')
            style_plot(fig, ax, f'Top Job Locations for {category}', 'Number of Jobs')
        elif plot_type == 'pie':
            ax.pie(country_distribution, labels=country_distribution.index, autopct='%1.1f%%', colors=plt.cm.Paired(range(len(country_distribution))), textprops={'color': 'white'})
            ax.set_title(f'Top Job Locations for {category}', color='white', fontsize=14, fontweight='bold')
            fig.patch.set_facecolor('#2C2C2C')
            ax.set_facecolor('#1E1E1E')
        elif plot_type == 'box':
            data_filtered = category_data.copy()
            data_filtered['country'] = data_filtered['company_location'].map(map_country_names)
            data_filtered.boxplot(column='salary_in_usd', by='country', ax=ax)
            ax.set_title(f'Salary Distribution by Location for {category}', color='white', fontsize=14, fontweight='bold')
            ax.set_xlabel('Location', color='white', fontsize=12, fontweight='bold')
            ax.set_ylabel('Salary in USD', color='white', fontsize=12, fontweight='bold')
            fig.suptitle('')
            fig.patch.set_facecolor('#2C2C2C')
            style_box_plot(ax)
    elif data_set == 'Country Distribution':
        country_distribution = category_data['company_location'].value_counts().head(10)
        if plot_type == 'bar':
            ax.barh(country_distribution.index.map(map_country_names), country_distribution.values, color='#5bc0de')
            style_plot(fig, ax, f'Country Distribution for {category}', 'Count')
        elif plot_type == 'pie':
            ax.pie(country_distribution, labels=country_distribution.index.map(map_country_names), autopct='%1.1f%%', colors=plt.cm.Paired(range(len(country_distribution))), textprops={'color': 'white'})
            ax.set_title(f'Top 10 Country Distribution for {category}', color='white', fontsize=14, fontweight='bold')
            fig.patch.set_facecolor('#2C2C2C')
            ax.set_facecolor('#1E1E1E')
        elif plot_type == 'box':
            data_filtered = category_data.copy()
            data_filtered['country'] = data_filtered['company_location'].map(map_country_names)
            data_filtered.boxplot(column='salary_in_usd', by='country', ax=ax)
            ax.set_title(f'Salary Distribution by Country for {category}', color='white', fontsize=14, fontweight='bold')
            ax.set_xlabel('Country', color='white', fontsize=12, fontweight='bold')
            ax.set_ylabel('Salary in USD', color='white', fontsize=12, fontweight='bold')
            fig.suptitle('')
            fig.patch.set_facecolor('#2C2C2C')
            style_box_plot(ax)
    elif data_set == 'Experience Distribution':
        experience_distribution = category_data['experience_level'].value_counts()
        experience_distribution.index = experience_distribution.index.map(experience_level_mapping)
        if plot_type == 'bar':
            ax.barh(experience_distribution.index, experience_distribution.values, color='#5bc0de')
            style_plot(fig, ax, f'Experience Distribution for {category}', 'Count')
        elif plot_type == 'pie':
            ax.pie(experience_distribution, labels=experience_distribution.index, autopct='%1.1f%%', colors=plt.cm.Paired(range(len(experience_distribution))), textprops={'color': 'white'})
            ax.set_title(f'Experience Distribution for {category}', color='white', fontsize=14, fontweight='bold')
            fig.patch.set_facecolor('#2C2C2C')
            ax.set_facecolor('#1E1E1E')
        elif plot_type == 'box':
            category_data.loc[:, 'experience_level'] = category_data['experience_level'].map(experience_level_mapping)
            category_data.boxplot(column='salary_in_usd', by='experience_level', ax=ax)
            ax.set_title(f'Salary Distribution by Experience Level for {category}', color='white', fontsize=14, fontweight='bold')
            ax.set_xlabel('Experience Level', color='white', fontsize=12, fontweight='bold')
            ax.set_ylabel('Salary in USD', color='white', fontsize=12, fontweight='bold')
            fig.suptitle('')
            fig.patch.set_facecolor('#2C2C2C')
            style_box_plot(ax)
    elif data_set == 'Company Size Distribution':
        company_size_distribution = category_data['company_size'].value_counts()
        company_size_distribution.index = company_size_distribution.index.map(company_size_mapping)
        if plot_type == 'bar':
            ax.barh(company_size_distribution.index, company_size_distribution.values, color='#5bc0de')
            style_plot(fig, ax, f'Company Size Distribution for {category}', 'Count')
        elif plot_type == 'pie':
            ax.pie(company_size_distribution, labels=company_size_distribution.index, autopct='%1.1f%%',
                   colors=plt.cm.Paired(range(len(company_size_distribution))), textprops={'color': 'white'})
            ax.set_title(f'Company Size Distribution for {category}', color='white', fontsize=14, fontweight='bold')
            fig.patch.set_facecolor('#2C2C2C')
            ax.set_facecolor('#1E1E1E')
        elif plot_type == 'box':
            category_data.loc[:, 'company_size'] = category_data['company_size'].map(company_size_mapping)
            category_data.boxplot(column='salary_in_usd', by='company_size', ax=ax)
            ax.set_title(f'Salary Distribution by Company Size for {category}', color='white', fontsize=14,
                         fontweight='bold')
            ax.set_xlabel('Company Size', color='white', fontsize=12, fontweight='bold')
            ax.set_ylabel('Salary in USD', color='white', fontsize=12, fontweight='bold')
            fig.suptitle('')
            fig.patch.set_facecolor('#2C2C2C')
            style_box_plot(ax)
    elif data_set == 'Employment Type Distribution':
        employment_type_count = category_data['employment_type'].value_counts().head(10)
        if plot_type == 'bar':
            ax.barh(employment_type_count.index, employment_type_count.values, color='#5bc0de')
            style_plot(fig, ax, f'Employment Type Distribution for {category}', 'Count')
        elif plot_type == 'pie':
            ax.pie(employment_type_count, labels=employment_type_count.index, autopct='%1.1f%%',
                   colors=plt.cm.Paired(range(len(employment_type_count))), textprops={'color': 'white'})
            ax.set_title(f'Employment Type Distribution for {category}', color='white', fontsize=14, fontweight='bold')
            fig.patch.set_facecolor('#2C2C2C')
            ax.set_facecolor('#1E1E1E')
        elif plot_type == 'box':
            category_data.boxplot(column='salary_in_usd', by='employment_type', ax=ax)
            ax.set_title(f'Salary Distribution by Employment Type for {category}', color='white', fontsize=14,
                         fontweight='bold')
            ax.set_xlabel('Employment Type', color='white', fontsize=12, fontweight='bold')
            ax.set_ylabel('Salary in USD', color='white', fontsize=12, fontweight='bold')
            fig.suptitle('')
            fig.patch.set_facecolor('#2C2C2C')
            style_box_plot(ax)

    plot_on_tile(fig, tile)
    plt.close(fig)
