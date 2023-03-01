import matplotlib
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from .analysis import polyfit

# Task 2E
def plot_water_levels(station, dates, levels):
    typical_high = station.typical_range[1]
    typical_low = station.typical_range[0]
    plt.plot(dates,levels,label = 'water level')
    plt.axhline(typical_high,color = 'r',label = 'typical high')
    plt.axhline(typical_low,color = 'g',label = 'typical low')
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation = 45)
    plt.title(station.name)
    plt.legend()

    plt.tight_layout()

    plt.show()

# Task 2F
def plot_water_level_with_fit(station,dates,levels,p):
    typical_high = station.typical_range[1]
    typical_low = station.typical_range[0]

    poly, d0 = polyfit(dates,levels,p)
    x = matplotlib.dates.date2num(dates)

    plt.plot(matplotlib.dates.num2date(x),poly(x-d0), label = 'best poly fit')

    plt.plot(x,levels, label = 'water level')
    plt.axhline(typical_high,color = 'r',label = 'typical high')
    plt.axhline(typical_low,color = 'g',label = 'typical low')
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation = 45)
    plt.title(station.name)
    plt.legend()

    plt.tight_layout()

    plt.show()


