import numpy as np

def median_filter(data, window):

    '''
    median_filter sorts the input Audio data array and 
    Returns the median from Audio data array.

            Inputs:
                    data   (int)  : Audio data array contains the clicks
                    window (int)  : filter length

            Output:
                    median (int)  : median of array
    '''

    # Check for odd window size
    if(window % 2 == 1):
        length = len(data)
        window_array = [0] * len(data)
        padding = (window - 1) // 2

        # Sorting in window size arrays in ascending order
        window_array = np.sort(data)       

        # printing window size arrays
        # print("window_array ", window_array)

        # storing median values
        median = window_array[padding]

        # print("median",  median)

        return median
    else:
        # Throwing error for even window
        print("Window size has to be odd number")