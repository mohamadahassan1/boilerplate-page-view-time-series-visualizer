import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv',  index_col='date')

# Clean data
# 1. Calculate the 2.5th and 97.5th percentiles (the cutoffs)
lower_bound = df['value'].quantile(0.025)
upper_bound = df['value'].quantile(0.975)

# 2. Filter the DataFrame to keep only the values *between* the two bounds
df = df[
    (df['value'] >= lower_bound) &
    (df['value'] <= upper_bound)
]



def draw_line_plot(df):
    # Create the figure and axes object
    fig, ax = plt.subplots(figsize=(10, 5))

    # Plot the data
    ax.plot(df.index, df['value'], color='red', linewidth=1)

    # Set the title and labels
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")

    
    # Return the figure object 
    return fig



    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar.index = pd.to_datetime(df_bar.index)

    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.strftime('%B')  # Full month name for better plotting
    df_bar['month_num'] = df_bar.index.month       # Month number for sorting

    # Draw bar plot
    def draw_bar_plot(df):
    # Ensure the index is a DatetimeIndex before proceeding
    df_bar = df.copy()
    if not isinstance(df_bar.index, pd.DatetimeIndex):
        df_bar.index = pd.to_datetime(df_bar.index)

    # 1. Prepare data for the plot: Extract year and month
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.strftime('%B')
    df_bar['month_num'] = df_bar.index.month

    # 2. Calculate the average daily page views for each month grouped by year
    df_grouped = df_bar.groupby(['year', 'month_num', 'month'])['value'].mean().reset_index()

    # 3. Pivot the data to get years as rows and months as columns
    df_pivot = df_grouped.pivot(index='year', columns='month', values='value')

    # 4. Ensure columns are in chronological month order (Jan, Feb, Mar, etc.)
    month_order = ['January', 'February', 'March', 'April', 'May', 'June',
                   'July', 'August', 'September', 'October', 'November', 'December']
    present_months = [month for month in month_order if month in df_pivot.columns]
    df_pivot = df_pivot[present_months]

    # 5. Create the plot
    fig, ax = plt.subplots(figsize=(10, 8))
    df_pivot.plot(kind='bar', ax=ax)

    # 6. Set labels and legend
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")
    ax.legend(title='Months')
    plt.xticks(rotation=0)

    # 7. Save image (for project submission)
    fig.savefig('bar_plot.png')


    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot(df):
    # 1. Prepare data for plotting
    df_box = df.copy()
    
    # Ensure index is datetime (critical if it wasn't done globally)
    if not isinstance(df_box.index, pd.DatetimeIndex):
        df_box.index = pd.to_datetime(df_box.index)

    # Extract Year and Month for plotting
    df_box['Year'] = df_box.index.year
    df_box['Month'] = df_box.index.strftime('%b') # Abbreviated month name (Jan, Feb, etc.)
    
    # Create a column for month order to ensure plots are chronological
    df_box['Month_num'] = df_box.index.month

    # 2. Set up the figure and axes for two adjacent plots
    # figsize is adjusted to accommodate two plots side-by-side
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))

    # --- First Plot: Year-wise Box Plot (Trend) ---
    # Use 'Year' on the x-axis and 'value' on the y-axis
    sns.boxplot(x='Year', y='value', data=df_box, ax=axes[0])
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")

    # --- Second Plot: Month-wise Box Plot (Seasonality) ---
    # Sort months chronologically using the numerical order before plotting
    month_order = df_box.sort_values('Month_num')['Month'].unique()
    
    # Use 'Month' on the x-axis and 'value' on the y-axis
    sns.boxplot(x='Month', y='value', data=df_box, order=month_order, ax=axes[1])
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")

    # 3. Adjust layout and save
    plt.tight_layout() # Ensures titles and labels don't overlap
    fig.savefig('box_plot.png')
    
   

    # Return the figure object (required for project testing)
    return fig

    draw_box_plot(df)
