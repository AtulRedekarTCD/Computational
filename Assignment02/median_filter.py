import numpy as np

def median_filter(data, window):

#     print(type(data))
    # Check for odd window size
    if(window % 2 == 1):
        length = len(data)
        # print("data: ", data)
        window_array = [0] * len(data)
        padding = (window - 1) // 2  # converting
#         print("padding: ", padding)



        # extracting window size arrays
#         window_array = data[index: window + index]
        window_array = np.sort(data)       # Sorting in window size arrays in ascending order

        # printing window size arrays
        # print("window_array ", window_array)

        # storing median values
        median = window_array[int((window - 1) / 2)]

        # print("median",  median)

        return median
    else:
        # Throwing error for even window
        print("Window size has to be odd number")