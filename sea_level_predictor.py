import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np 

def draw_plot():
    # Read data from file
    df=pd.read_csv('epa-sea-level.csv')
    # Create scatter plot create a scatter plot using the Year column as 
    # the x-axis and the CSIRO Adjusted Sea Level column as the y-axis.
    plt.figure()
    plt.scatter(df['Year'],df['CSIRO Adjusted Sea Level'])   

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years= np.arange(1880, 2051, 1)
    plt.plot(years, years*slope+intercept,color='red', label='Predicted')  

    # Create second line of best fit using the data from year 2000 through the most recent year in the dataset
    df_short=df[df['Year']>=2000]  
    years= np.arange(2000, 2051, 1)
    slope, intercept, r_value, p_value, std_err = linregress(df_short['Year'], df_short['CSIRO Adjusted Sea Level'])
    plt.plot(years, years*slope+intercept, color='green', label='Predicted_from_2000')  

    # Add labels and title. The x label should be Year, the y label should be Sea Level (inches),
    #  and the title should be Rise in Sea Level.
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()