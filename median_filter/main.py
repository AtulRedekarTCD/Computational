import numpy as np
from scipy import signal as sc
from scipy.io import wavfile

# Definition
# function Name :  median_filter(data, window)
# Inputs        :  list data   -> Input signal Array
#               :  int  window -> Size of Window
# Output        :  list median_array  -> Median Computed Array


def median_filter(data, window):

    # Check for odd window size
    if(window % 2 == 1):
        padded_data = data
        length = len(data)
        median_array = []
        padding = (window - 1) // 2  # converting
        print("padding: ", padding)

    #   Appending '0' padding at start and end of the signal data
        for i in range(padding * 2):
            if (i < padding):
                padded_data.insert(0, 0)
            else:
                padded_data.insert(len(padded_data), 0)

        print("padded_data : ", padded_data)

        for index in range(length):
            # extracting window size arrays
            window_array = padded_data[index: window + index]
            window_array.sort()       # Sorting in window size arrays in ascending order

            # printing window size arrays
            print("window_array", index, " : ", window_array)

            # storing median values
            median = window_array[int((window - 1) / 2)]

            median_array.append(median)  # creating median values array

        print("\nmedian_array : ", median_array)
        print("\n")

        return median_array
    else:
        # Throwing error for even window
        print("Window size hve to odd number")


if __name__ == "__main__":

    data = [1, 2, 3, 6, 10, 7, 2, 1]
    window = 3

    filter_out = sc.medfilt(data,kernel_size = window) # Using medfilt from scipy
    
    print(" medfilt : ", filter_out) 

# calling median_filter to computer Median
    median_filter(data, window)
