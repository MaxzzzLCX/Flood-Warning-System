import numpy as np
import matplotlib

# Task 2F
def polyfit(dates,levels,p):
    x = matplotlib.dates.date2num(dates)
    p_coeff = np.polyfit(x-x[0],levels,p)

    poly = np.poly1d(p_coeff)

    d0 = x[0]

    return poly, d0




# Task 2F
# def polyfit(dates,levels,p):
#     x = matplotlib.dates.date2num(dates)
#     x = list(reversed(x))#idk why the order is reversed
#     y = levels
#     p_coeff = np.polyfit(x - x[0],y,p)

#     poly = np.poly1d(p_coeff)

#     d0 = x[0]

#     return poly, d0
