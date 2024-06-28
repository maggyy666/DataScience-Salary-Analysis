import matplotlib.pyplot as plt
from utils import style_plot, plot_on_tile, load_data, experience_level_mapping, country_names_mapping, company_size_mapping
from plot_generator import *
class JobCategoryPlot:
    def __init__(self, job_titles):
        self.job_titles = job_titles

    def filter_data(self, data):
        return data[data['job_title'].isin(self.job_titles)]

    def update_plot(self, tile, plot_type, data_set):
        data = self.filter_data(load_data())
        fig, ax = plt.subplots(figsize=(18, 6))

        if data_set == 'Average Salary':
            self.plot_average_salary(ax, data, plot_type)
        elif data_set == 'Salary by Experience':
            self.plot_salary_by_experience(ax, data, plot_type)
        elif data_set == 'Jobs by Location':
            self.plot_jobs_by_location(ax, data, plot_type)
        elif data_set == 'Country Distribution':
            self.plot_country_distribution(ax, data, plot_type)
        elif data_set == 'Experience Distribution':
            self.plot_experience_distribution(ax, data, plot_type)
        elif data_set == 'Company Size Distribution':
            self.plot_company_size_distribution(ax, data, plot_type)

        plot_on_tile(fig, tile)

    def plot_average_salary(self, ax, data, plot_type):
        salary_per_country = data.groupby('company_location')['salary_in_usd'].mean().sort_values()
        if plot_type == 'bar':
            ax.barh(salary_per_country.index, salary_per_country.values, color='#5bc0de')
            style_plot(ax.figure, ax, 'Average Salary by Country', 'Average Salary in USD')
        elif plot_type == 'pie':
            salary_per_country = salary_per_country.head(10)
            ax.pie(salary_per_country, labels=salary_per_country.index, autopct='%1.1f%%', colors=plt.cm.Paired(range(len(salary_per_country))), textprops={'color': 'white'})
            ax.set_title('Top 10 Average Salary by Country', color='white', fontsize=12)
            ax.figure.patch.set_facecolor('#2C2C2C')
            ax.set_facecolor('#1E1E1E')
        elif plot_type == 'box':
            specialties = ['Data Scientist', 'Applied Scientist', 'Applied Data Scientist', 'Business Data Analyst',
                           'Staff Data Scientist', 'Lead Data Scientist', 'Product Data Scientist',
                           'Principal Data Scientist', 'Data Scientist Lead']
            data_filtered = data[data['job_title'].isin(specialties)]
            data_filtered.boxplot(column='salary_in_usd', by='job_title', ax=ax)
            ax.set_title('Average Salary for Data Scientist Specialties', color='white', fontsize=12)
            ax.set_xlabel('Specialty', color='white')
            ax.set_ylabel('Salary in USD', color='white')
            ax.figure.suptitle('')
            ax.figure.patch.set_facecolor('#2C2C2C')
            ax.set_facecolor('#1E1E1E')
            ax.tick_params(axis='x', colors='white')
            ax.tick_params(axis='y', colors='white')

    def plot_salary_by_experience(self, ax, data, plot_type):
        experience_salary = data.groupby('experience_level')['salary_in_usd'].mean().sort_values()
        experience_salary.index = experience_salary.index.map(experience_level_mapping)
        if plot_type == 'bar':
            ax.barh(experience_salary.index, experience_salary.values, color='#5bc0de')
            style_plot(ax.figure, ax, 'Average Salary by Experience Level', 'Average Salary in USD')
        elif plot_type == 'pie':
            ax.pie(experience_salary, labels=experience_salary.index, autopct='%1.1f%%', colors=plt.cm.Paired(range(len(experience_salary))), textprops={'color': 'white'})
            ax.set_title('Salary by Experience Level', color='white', fontsize=12)
            ax.figure.patch.set_facecolor('#2C2C2C')
            ax.set_facecolor('#1E1E1E')
        elif plot_type == 'box':
            data.boxplot(column='salary_in_usd', by='experience_level', ax=ax)
            ax.set_title('Salary Distribution by Experience Level')
            ax.set_xlabel('Experience Level')
            ax.set_ylabel('Salary in USD')
            ax.figure.suptitle('')

    def plot_jobs_by_location(self, ax, data, plot_type):
        job_location = data['company_location'].value_counts().head(10)
        job_location.index = job_location.index.map(lambda x: country_names_mapping.get(x, 'Other'))
        if plot_type == 'bar':
            ax.barh(job_location.index, job_location.values, color='#5bc0de')
            style_plot(ax.figure, ax, 'Top Job Locations', 'Number of Jobs')
        elif plot_type == 'pie':
            ax.pie(job_location, labels=job_location.index, autopct='%1.1f%%', colors=plt.cm.Paired(range(len(job_location))), textprops={'color': 'white'})
            ax.set_title('Top Job Locations', color='white', fontsize=12)
            ax.figure.patch.set_facecolor('#2C2C2C')
            ax.set_facecolor('#1E1E1E')
        elif plot_type == 'box':
            data.boxplot(column='salary_in_usd', by='company_location', ax=ax)
            ax.set_title('Salary Distribution by Location')
            ax.set_xlabel('Location')
            ax.set_ylabel('Salary in USD')
            ax.figure.suptitle('')

    def plot_country_distribution(self, ax, data, plot_type):
        country_distribution = data['company_location'].value_counts().head(10)
        if plot_type == 'bar':
            ax.barh(country_distribution.index, country_distribution.values, color='#5bc0de')
            style_plot(ax.figure, ax, 'Country Distribution', 'Count')
        elif plot_type == 'pie':
            ax.pie(country_distribution, labels=country_distribution.index, autopct='%1.1f%%', colors=plt.cm.Paired(range(len(country_distribution))), textprops={'color': 'white'})
            ax.set_title('Top 10 Country Distribution', color='white', fontsize=12)
            ax.figure.patch.set_facecolor('#2C2C2C')
            ax.set_facecolor('#1E1E1E')
        elif plot_type == 'box':
            data.boxplot(column='salary_in_usd', by='company_location', ax=ax)
            ax.set_title('Salary Distribution by Country')
            ax.set_xlabel('Country')
            ax.set_ylabel('Salary in USD')
            ax.figure.suptitle('')

    def plot_experience_distribution(self, ax, data, plot_type):
        experience_distribution = data['experience_level'].value_counts()
        experience_distribution.index = experience_distribution.index.map(experience_level_mapping)
        if plot_type == 'bar':
            ax.barh(experience_distribution.index, experience_distribution.values, color='#5bc0de')
            style_plot(ax.figure, ax, 'Experience Distribution', 'Count')
        elif plot_type == 'pie':
            ax.pie(experience_distribution, labels=experience_distribution.index, autopct='%1.1f%%', colors=plt.cm.Paired(range(len(experience_distribution))), textprops={'color': 'white'})
            ax.set_title('Experience Distribution', color='white', fontsize=12)
            ax.figure.patch.set_facecolor('#2C2C2C')
            ax.set_facecolor('#1E1E1E')
        elif plot_type == 'box':
            data.boxplot(column='salary_in_usd', by='experience_level', ax=ax)
            ax.set_title('Salary Distribution by Experience Level')
            ax.set_xlabel('Experience Level')
            ax.set_ylabel('Salary in USD')
            ax.figure.suptitle('')

    def plot_company_size_distribution(self, ax, data, plot_type):
        company_size_distribution = data['company_size'].value_counts()
        company_size_distribution.index = company_size_distribution.index.map(company_size_mapping)
        if plot_type == 'bar':
            ax.barh(company_size_distribution.index, company_size_distribution.values, color='#5bc0de')
            style_plot(ax.figure, ax, 'Company Size Distribution', 'Count')
        elif plot_type == 'pie':
            ax.pie(company_size_distribution, labels=company_size_distribution.index, autopct='%1.1f%%', colors=plt.cm.Paired(range(len(company_size_distribution))), textprops={'color': 'white'})
            ax.set_title('Company Size Distribution', color='white', fontsize=12)
            ax.figure.patch.set_facecolor('#2C2C2C')
            ax.set_facecolor('#1E1E1E')
        elif plot_type == 'box':
            data.boxplot(column='salary_in_usd', by='company_size', ax=ax)
            ax.set_title('Salary Distribution by Company Size')
            ax.set_xlabel('Company Size')
            ax.set_ylabel('Salary in USD')
            ax.figure.suptitle('')

class DataScientistsPlot(JobCategoryPlot):
    def __init__(self):
        super().__init__(job_categories['Data Scientists'])

class DataEngineersPlot(JobCategoryPlot):
    def __init__(self):
        super().__init__(job_categories['Data Engineers'])

class MLEngineersPlot(JobCategoryPlot):
    def __init__(self):
        super().__init__(job_categories['ML Engineers'])

class AISpecialistsPlot(JobCategoryPlot):
    def __init__(self):
        super().__init__(job_categories['AI Specialists'])

class DSManagementPlot(JobCategoryPlot):
    def __init__(self):
        super().__init__(job_categories['DS Management'])

class ResearchRolesPlot(JobCategoryPlot):
    def __init__(self):
        super().__init__(job_categories['Research Roles'])

class BusinessIntelligencePlot(JobCategoryPlot):
    def __init__(self):
        super().__init__(job_categories['Business Intelligence'])

class SpecializedAnalystsPlot(JobCategoryPlot):
    def __init__(self):
        super().__init__(job_categories['Specialized Analysts'])

class ArchitectsPlot(JobCategoryPlot):
    def __init__(self):
        super().__init__(job_categories['Architects'])

class MiscellaneousPlot(JobCategoryPlot):
    def __init__(self):
        super().__init__(job_categories['Miscellaneous'])

