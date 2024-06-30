# DS Salary Analysis Project

## Overview
The DS Salary Analysis Project is an application designed for visualizing and analyzing data science salary information. The application is built using the Tkinter library for the user interface and Matplotlib for data visualization. It leverages custom styling and plot generation to provide an intuitive and interactive experience for users to explore salary data across various dimensions.

## Features
- **User Interface:** Utilizes the Tkinter library to create a user-friendly interface with a modern appearance using customtkinter.
- **Data Visualization:** Generates dynamic plots (bar charts, pie charts, box plots) using Matplotlib to visualize salary data.
- **Category Analysis:** Allows users to analyze data by job title categories, experience levels, and locations.

## Requirements
- **Development Environment:** Python 3.x
- **Libraries:** Tkinter, customtkinter, Matplotlib, pandas

## Installation
1. Clone the repository to your local machine.
   ```bash
   git clone https://github.com/maggyy666/DataScience-Salary-Analysis.git
2. Navigate to the project directory.
    ```bash
   cd DataScience-Salary-Analysis
3. Install the required libraries.
    ```bash
   pip install -r requirements.txt
## Usage
1. Launch the application by running the main.py file.
    ```bash
   python main.py
2. Use the navigation bar to switch between different data sets and plot types.
3. Select categories from the sidebar to filter the data and update the plots dynamically.
## Project Structure
- **main.py:** The main script that initializes the Tkinter window and handles user interactions.
- **utils.py:** Contains utility functions for data loading, styling plots, and mapping values.
- **plot_generator.py:** Includes functions to generate and update various types of plots based on the selected data and categories.

## License
This project is licensed under the MIT License, granting users the freedom to use, modify, and distribute the software as per the terms of the license.
