import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot


    # Create first line of best fit
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    plt.scatter(x, y)
    slope, intercept, _, _, _ = linregress(x, y)
    x_prediction = pd.Series(range(1880, 2051))
    y_prediction = slope * x_prediction + intercept
    plt.plot(x_prediction, y_prediction)

    # Create second line of best fit
    x_later_years = df.loc[df['Year'] >= 2000, 'Year']
    y_later_years = df.loc[df['Year'] >= 2000, 'CSIRO Adjusted Sea Level']

    slope_later_years, intercept_later_years, _, _, _ = linregress(x_later_years, y_later_years)

    x_later_years_prediction = pd.Series(range(2000, 2051))
    y_later_years_prediction = slope_later_years * x_later_years_prediction + intercept_later_years

    plt.plot(x_later_years_prediction, y_later_years_prediction)

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()