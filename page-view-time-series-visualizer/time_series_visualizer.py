import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import calendar
import numpy as np
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", index_col="date", parse_dates=["date"])
df.rename(columns={"value" : "views"}, inplace=True)

# Clean data
df = df[(df['views'] >= df['views'].quantile(0.025)) & (df['views'] <= df['views'].quantile(0.975))] # 1304 -> 1176

def draw_line_plot():
    # Draw line plot
    df_line = df.copy()
    fig, ax = plt.subplots(figsize=(14, 5))
    ax.plot(df_line, color='red')
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    fig.tight_layout()

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month
    df_bar['month'] = df_bar.index.month
    df_bar = df_bar.groupby(['year', 'month'])['views'].mean().unstack()
    df_bar.columns = [calendar.month_name[i] for i in df_bar.columns]

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(7,6))
    df_bar.plot(kind="bar", ax=ax)
    ax.set_title("Average Page Views per Month")
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")
    ax.ticklabel_format(style="plain", axis='y')
    ax.legend(title='Months')
    fig.tight_layout()

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(14, 5))
    sns.boxplot(x='year', y='views', hue='year', data=df_box, ax=ax1, flierprops={'markersize' : 1.5})
    sns.boxplot(x='month', y='views', hue='month', data=df_box, ax=ax2, flierprops={'markersize' : 1.5}, order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    ax1.set_title("Year-wise Box Plot (Trend)")
    ax2.set_title("Month-wise Box Plot (Seasonality)")
    ax1.set_xlabel("Year")
    ax2.set_xlabel("Month")
    ax1.set_ylabel("Page Views")
    ax2.set_ylabel("Page Views")
    ax1.set_yticks(np.arange(0, 200001, 20000))
    ax2.set_yticks(np.arange(0, 200001, 20000))
    ax1.legend_.remove()
    fig.tight_layout()

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
