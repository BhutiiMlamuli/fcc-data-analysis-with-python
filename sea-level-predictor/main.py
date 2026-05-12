import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    
    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], 
               color='blue', alpha=0.5, label='Data')
    
    # Create first line of best fit (using all data)
    slope, intercept, r_value, p_value, std_err = linregress(
        df['Year'], df['CSIRO Adjusted Sea Level']
    )
    
    # Create line extending to 2050
    years_extended = range(1880, 2051)
    sea_level_pred1 = [slope * year + intercept for year in years_extended]
    ax.plot(years_extended, sea_level_pred1, 'r', 
            label='Best Fit Line (1880-2013)')
    
    # Create second line of best fit (using data from 2000 onwards)
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(
        df_recent['Year'], df_recent['CSIRO Adjusted Sea Level']
    )
    
    # Create line extending to 2050 for recent data
    years_recent = range(2000, 2051)
    sea_level_pred2 = [slope_recent * year + intercept_recent for year in years_recent]
    ax.plot(years_recent, sea_level_pred2, 'green', 
            label='Best Fit Line (2000-2013)')
    
    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    
    # Add legend
    ax.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()