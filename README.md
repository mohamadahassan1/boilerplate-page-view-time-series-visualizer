📈 FreeCodeCamp: Page View Time Series Visualizer

This project is the final requirement for the freeCodeCamp Data Analysis with Python Certification. It involves cleaning, manipulating, and visualizing time series data of page views on the freeCodeCamp.org forum using Pandas, Matplotlib, and Seaborn.

🎯 Project Goal

The primary objective was to analyze and visualize the patterns in the number of daily page views on the freeCodeCamp forum between May 2016 and December 2019 to identify yearly trends and monthly seasonality.

🛠️ Technologies Used

Technology	Purpose
Python	Core programming language
Pandas	Data importing, cleaning, and manipulation (time series indexing, grouping)
Matplotlib	Creating the Line and Bar charts
Seaborn	Creating the Box Plots (for distribution analysis)

⚙️ Key Steps and Data Cleaning

The project required specific data cleaning and preparation steps to ensure valid analysis:

    Data Import & Indexing: Imported fcc-forum-pageviews.csv and set the date column as the DataFrame index, ensuring it was converted to the datetime type for proper time series handling.

    Outlier Removal: Cleaned the data by filtering out days when page views were in the top 2.5% or the bottom 2.5% of the entire dataset.

📊 Visualizations Created

The project successfully generated three types of plots to analyze the data:

1. Line Plot (Daily Trend)

Shows the daily page view counts over the entire period to visualize the overall growth trend.
Visualization	Description
Title:	Daily freeCodeCamp Forum Page Views 5/2016-12/2019
X-Axis:	Date
Y-Axis:	Page Views
(path/to/line_plot.png)

2. Bar Chart (Yearly and Monthly Average)

Displays the average daily page views for each month, grouped by year. This visualization is key to seeing how average usage compares year-over-year.
Visualization	Description
X-Axis:	Years
Y-Axis:	Average Page Views
Legend:	Months

3. Box Plots (Trend and Seasonality Distribution)

Two adjacent box plots illustrate the distribution of page views, helping to identify variation and seasonality.

    Year-wise Box Plot (Trend): Shows how the spread of daily page views changed from year to year.

    Month-wise Box Plot (Seasonality): Shows the monthly distribution, revealing clear seasonal patterns in user engagement.

Plot 1	Plot 2
Title: Year-wise Box Plot (Trend)	Title: Month-wise Box Plot (Seasonality)
X-Axis: Year	X-Axis: Month (Jan, Feb, Mar, etc.)
Y-Axis: Page Views	Y-Axis: Page Views

🚀 How to Run the Code

    Clone the repository:
    Bash

git clone [YOUR-REPO-URL]

Install dependencies:
Bash

pip install pandas matplotlib seaborn

Run the main script (or the Jupyter Notebook where you developed the code):
Bash

    python time_series_visualizer.py

    Note: The required output images (line_plot.png, bar_plot.png, box_plot.png) will be saved to the working directory.

Feel free to star ⭐ this repository if you found the analysis interesting!

•This is the boilerplate for the Page View Time Series Visualizer project. Instructions for building your project can be found at https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/page-view-time-series-visualizer
