import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots()
    ax.scatter(x='Year', y='CSIRO Adjusted Sea Level', data=df, s=10)

    # Create first line of best fit
    res_1880 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_1880 = range(1880, 2051)
    m_1880 = res_1880.slope
    b_1880 = res_1880.intercept
    ax.plot(x_1880, m_1880 * x_1880 + b_1880, 'black')

    # Create second line of best fit
    res_2000 = linregress(range(2000, 2014), df['CSIRO Adjusted Sea Level'][-14:])
    m_2000 = res_2000.slope
    b_2000 = res_2000.intercept
    x_2000 = range(2000, 2051)
    ax.plot(x_2000, m_2000 * x_2000 + b_2000, 'r')

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()