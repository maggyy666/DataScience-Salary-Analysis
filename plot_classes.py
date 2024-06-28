import matplotlib.pyplot as plt
import pandas as pd
from utils import style_plot, plot_on_tile, load_data, experience_level_mapping, country_names_mapping, \
    company_size_mapping, format_label

job_categories = {
    'Data Scientists': ['Data Scientist', 'Applied Scientist', 'Applied Data Scientist', 'Business Data Analyst',
                        'Staff Data Scientist', 'Lead Data Scientist', 'Product Data Scientist',
                        'Principal Data Scientist', 'Data Scientist Lead'],
    'Data Engineers': ['Data Engineer', 'Data Modeler', 'Analytics Engineer', 'ETL Engineer', 'Data DevOps Engineer',
                       'BI Data Engineer', 'Data Infrastructure Engineer', 'Software Data Engineer',
                       'Cloud Database Engineer', 'Azure Data Engineer', 'Marketing Data Engineer',
                       'Cloud Data Engineer', 'Lead Data Engineer', 'Principal Data Engineer'],
    'ML Engineers': ['ML Engineer', 'Machine Learning Engineer', 'Applied Machine Learning Engineer',
                     'Machine Learning Scientist', 'Deep Learning Engineer', 'Machine Learning Software Engineer',
                     'Machine Learning Research Engineer', 'NLP Engineer', 'Machine Learning Developer',
                     'Principal Machine Learning Engineer', 'Lead Machine Learning Engineer'],
    'AI Specialists': ['AI Developer', 'AI Scientist', 'AI Programmer', 'Autonomous Vehicle Technician',
                       'Applied Machine Learning Scientist', 'Principal Machine Learning Engineer',
                       'Machine Learning Manager'],
    'DS Management': ['Head of Data', 'Data Science Manager', 'Data Manager', 'Director of Data Science',
                      'Head of Data Science', 'Data Science Lead', 'Data Analytics Manager', 'Head of Machine Learning',
                      'Data Science Tech Lead'],
    'Research Roles': ['Research Engineer', 'Research Scientist', 'Deep Learning Researcher',
                       'Machine Learning Researcher', '3D Computer Vision Researcher'],
    'Business Intelligence': ['BI Data Engineer', 'BI Developer', 'BI Analyst', 'BI Data Analyst', 'Power BI Developer',
                              'Business Intelligence Engineer'],
    'Specialized Analysts': ['Data Analyst', 'Data Quality Analyst', 'Compliance Data Analyst',
                             'Financial Data Analyst', 'Marketing Data Analyst', 'Insight Analyst',
                             'Product Data Analyst'],
    'Architects': ['Data Architect', 'Principal Data Architect', 'Big Data Architect', 'Cloud Data Architect'],
    'Miscellaneous': ['Data Strategist', 'Data Specialist', 'Lead Data Analyst', 'MLOps Engineer',
                      'Data Operations Engineer', 'Data Science Consultant', 'Data Analytics Specialist',
                      'Machine Learning Infrastructure Engineer', 'Data Analytics Lead', 'Data Lead',
                      'Data Science Engineer', 'Manager Data Management', 'Data Analytics Engineer',
                      'Data Analytics Consultant', 'Data Management Specialist', 'Data Operations Analyst',
                      'Principal Data Analyst', 'Finance Data Analyst']
}


class JobCategoryPlot:
    def __init__(self, tile, category):
        self.tile = tile
        self.category = category
        self.data = load_data()
        self.filtered_data = self.data[self.data['job_title'].isin(job_categories[self.category])]

    def plot_common_positions(self, plot_type):
        job_count = self.filtered_data['job_title'].value_counts().head(5)
        fig, ax = plt.subplots()

        if plot_type == 'bar':
            ax.barh(job_count.index, job_count.values, color='#5bc0de')
            style_plot(fig, ax, 'Top 5 Most Common Positions in the DS Industry', 'Count')
        elif plot_type == 'pie':
            ax.pie(job_count, labels=job_count.index, autopct=lambda pct: format_label(pct, job_count.values), textprops={'color': 'white'}, startangle=140, colors=plt.cm.Paired(range(len(job_count))))
            ax.set_title('Top 5 Most Common Positions in the DS Industry', color='white', fontsize=12)
            fig.patch.set_facecolor('#2C2C2C')
            ax.set_facecolor('#1E1E1E')
            plt.gca().set_aspect('equal')
        elif plot_type == 'box':
            self.filtered_data.boxplot(column='salary_in_usd', by='job_title', ax=ax)
            ax.set_title('Salary Distribution by Job Title')
            ax.set_xlabel('Job Title')
            ax.set_ylabel('Salary in USD')
            fig.suptitle('')

        plot_on_tile(fig, self.tile)


    def plot_salary_by_experience(self, plot_type):
        experience_salary = self.data.groupby('experience_level')['salary_in_usd'].mean().sort_values()
        experience_salary.index = experience_salary.index.map(experience_level_mapping)
        fig, ax = plt.subplots(figsize=(18, 6))
        if plot_type == 'bar':
            ax.barh(experience_salary.index, experience_salary.values, color='#5bc0de')
            style_plot(fig, ax, f'Salary by Experience Level for {self.category}', 'Average Salary in USD')
        elif plot_type == 'pie':
            ax.pie(experience_salary, labels=experience_salary.index, autopct='%1.1f%%',
                   colors=plt.cm.Paired(range(len(experience_salary))), textprops={'color': 'white'})
            ax.set_title(f'Salary by Experience Level for {self.category}', color='white', fontsize=12)
            fig.patch.set_facecolor('#2C2C2C')
            ax.set_facecolor('#1E1E1E')
        elif plot_type == 'box':
            self.data.boxplot(column='salary_in_usd', by='experience_level', ax=ax)
            ax.set_title(f'Salary Distribution by Experience Level for {self.category}', color='white', fontsize=12)
            ax.set_xlabel('Experience Level', color='white')
            ax.set_ylabel('Salary in USD', color='white')
            fig.suptitle('')
            fig.patch.set_facecolor('#2C2C2C')
            ax.set_facecolor('#1E1E1E')
            ax.tick_params(axis='x', colors='white')
            ax.tick_params(axis='y', colors='white')
        plot_on_tile(fig, self.tile)

    def plot_jobs_by_location(self, plot_type):
        job_location = self.data['company_location'].value_counts().head(10)
        fig, ax = plt.subplots(figsize=(18, 6))
        if plot_type == 'bar':
            ax.barh(job_location.index, job_location.values, color='#5bc0de')
            style_plot(fig, ax, f'Jobs by Location for {self.category}', 'Number of Jobs')
        elif plot_type == 'pie':
            ax.pie(job_location, labels=job_location.index, autopct='%1.1f%%',
                   colors=plt.cm.Paired(range(len(job_location))), textprops={'color': 'white'})
            ax.set_title(f'Jobs by Location for {self.category}', color='white', fontsize=12)
            fig.patch.set_facecolor('#2C2C2C')
            ax.set_facecolor('#1E1E1E')
        elif plot_type == 'box':
            self.data.boxplot(column='salary_in_usd', by='company_location', ax=ax)
            ax.set_title(f'Salary Distribution by Location for {self.category}', color='white', fontsize=12)
            ax.set_xlabel('Location', color='white')
            ax.set_ylabel('Salary in USD', color='white')
            fig.suptitle('')
            fig.patch.set_facecolor('#2C2C2C')
            ax.set_facecolor('#1E1E1E')
            ax.tick_params(axis='x', colors='white')
            ax.tick_params(axis='y', colors='white')
        plot_on_tile(fig, self.tile)

    def plot_country_distribution(self, plot_type):
        country_distribution = self.data['company_location'].value_counts().head(10)
        fig, ax = plt.subplots(figsize=(18, 6))
        if plot_type == 'bar':
            ax.barh(country_distribution.index, country_distribution.values, color='#5bc0de')
            style_plot(fig, ax, f'Country Distribution for {self.category}', 'Count')
        elif plot_type == 'pie':
            ax.pie(country_distribution, labels=country_distribution.index, autopct='%1.1f%%',
                   colors=plt.cm.Paired(range(len(country_distribution))), textprops={'color': 'white'})
            ax.set_title(f'Top 10 Country Distribution for {self.category}', color='white', fontsize=12)
            fig.patch.set_facecolor('#2C2C2C')
            ax.set_facecolor('#1E1E1E')
        elif plot_type == 'box':
            self.data.boxplot(column='salary_in_usd', by='company_location', ax=ax)
            ax.set_title(f'Salary Distribution by Country for {self.category}', color='white', fontsize=12)
            ax.set_xlabel('Country', color='white')
            ax.set_ylabel('Salary in USD', color='white')
            fig.suptitle('')
            fig.patch.set_facecolor('#2C2C2C')
            ax.set_facecolor('#1E1E1E')
            ax.tick_params(axis='x', colors='white')
            ax.tick_params(axis='y', colors='white')
        plot_on_tile(fig, self.tile)

        def plot_experience_distribution(self, plot_type):
            experience_distribution = self.data['experience_level'].value_counts()
            experience_distribution.index = experience_distribution.index.map(experience_level_mapping)
            fig, ax = plt.subplots(figsize=(18, 6))
            if plot_type == 'bar':
                ax.barh(experience_distribution.index, experience_distribution.values, color='#5bc0de')
                style_plot(fig, ax, f'Experience Distribution for {self.category}', 'Count')
            elif plot_type == 'pie':
                ax.pie(experience_distribution, labels=experience_distribution.index, autopct='%1.1f%%',
                       colors=plt.cm.Paired(range(len(experience_distribution))), textprops={'color': 'white'})
                ax.set_title(f'Experience Distribution for {self.category}', color='white', fontsize=12)
                fig.patch.set_facecolor('#2C2C2C')
                ax.set_facecolor('#1E1E1E')
            elif plot_type == 'box':
                self.data.boxplot(column='salary_in_usd', by='experience_level', ax=ax)
                ax.set_title(f'Salary Distribution by Experience Level for {self.category}', color='white', fontsize=12)
                ax.set_xlabel('Experience Level', color='white')
                ax.set_ylabel('Salary in USD', color='white')
                fig.suptitle('')
                fig.patch.set_facecolor('#2C2C2C')
                ax.set_facecolor('#1E1E1E')
                ax.tick_params(axis='x', colors='white')
                ax.tick_params(axis='y', colors='white')
            plot_on_tile(fig, self.tile)

        def plot_company_size_distribution(self, plot_type):
            company_size_distribution = self.data['company_size'].value_counts()
            company_size_distribution.index = company_size_distribution.index.map(company_size_mapping)
            fig, ax = plt.subplots(figsize=(18, 6))
            if plot_type == 'bar':
                ax.barh(company_size_distribution.index, company_size_distribution.values, color='#5bc0de')
                style_plot(fig, ax, f'Company Size Distribution for {self.category}', 'Count')
            elif plot_type == 'pie':
                ax.pie(company_size_distribution, labels=company_size_distribution.index, autopct='%1.1f%%',
                       colors=plt.cm.Paired(range(len(company_size_distribution))), textprops={'color': 'white'})
                ax.set_title(f'Company Size Distribution for {self.category}', color='white', fontsize=12)
                fig.patch.set_facecolor('#2C2C2C')
                ax.set_facecolor('#1E1E1E')
            elif plot_type == 'box':
                self.data.boxplot(column='salary_in_usd', by='company_size', ax=ax)
                ax.set_title(f'Salary Distribution by Company Size for {self.category}', color='white', fontsize=12)
                ax.set_xlabel('Company Size', color='white')
                ax.set_ylabel('Salary in USD', color='white')
                fig.suptitle('')
                fig.patch.set_facecolor('#2C2C2C')
                ax.set_facecolor('#1E1E1E')
                ax.tick_params(axis='x', colors='white')
                ax.tick_params(axis='y', colors='white')
            plot_on_tile(fig, self.tile)

        def plot_common_positions(self, plot_type):
            job_count = self.data['job_title'].value_counts().head(5)
            fig, ax = plt.subplots(figsize=(18, 6))
            if plot_type == 'bar':
                ax.barh(job_count.index, job_count.values, color='#5bc0de')
                style_plot(fig, ax, f'Top 5 Most Common Positions in {self.category}', 'Count')
            elif plot_type == 'pie':
                ax.pie(job_count, labels=job_count.index, autopct=lambda pct: format_label(pct, job_count.values),
                       textprops={'color': 'white'}, startangle=140, colors=plt.cm.Paired(range(len(job_count))))
                ax.set_title(f'Top 5 Most Common Positions in {self.category}', color='white', fontsize=12)
                fig.patch.set_facecolor('#2C2C2C')
                ax.set_facecolor('#1E1E1E')
                plt.gca().set_aspect('equal')
            plot_on_tile(fig, self.tile)

