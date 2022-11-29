import numpy as np
import random
from scipy import signal as sc
from scipy.io import wavfile
import matplotlib.pyplot as plt
import median_filter as median
from scipy.io.wavfile import write

def get_filter_len(degraded_data_1d):

    '''
    get_filter_len give the best filter length for degraded audio data 
    by computing minimum MSE.

    Returns the filter length.

            Inputs:
                    degraded_data_1d   (array)  : degraded audio data

            Output:
                    filter_len         (int)    : filter length 
    '''

    # Computing MSE for the window size from 3 to 19
    windows = [3,5,7,9,11,13,15,17,19]

    MSE = np.zeros(len(windows))

    Threshold = 32000

    for w in range(len(windows)):
        
        window = windows[w]	
        padding = (window - 1) // 2

        for index in range(len(degraded_data_1d)):
            if( abs(degraded_data_1d[index]) >= Threshold ):            
                res_data[index] = median.median_filter(degraded_data_1d[index - padding : index + padding + 1], window)

        MSE[w] =  np.square(np.subtract(audio_data_1d,res_data)).mean()

        # print(MSE[w]," : ",window)
    
    
    # Returns a minimum index MSE
    min_index = np.where(MSE == MSE.min())

    # Convert it into integer value
    min_i = int(min_index[0])
    
    # Store the minimum filter length
    filter_len = windows[min_i] 

    plt.plot(windows,MSE,'-r*')
    plt.xlim(1,20,1)
    plt.ylim(0.4,1.8)
    plt.xlabel("Filter Length")
    plt.ylabel("MSE")
    plt.title("MSE vs Filter Size")
    plt.show()

    return filter_len

if __name__ == "__main__":

    # reading Data from Audio files
    samplerate, audio_data = wavfile.read("apple_audio.wav")
    samplerate, degraded_data = wavfile.read("degraded.wav")

    # Using single channel 
    audio_data_1d = audio_data[:, 1]
    degraded_data_1d = degraded_data[:, 1]

    # Creating a Array of detect for position of clicks
    detect = np.zeros(len(degraded_data_1d))

    Threshold = 32000
    for i in range(len(degraded_data_1d)):
        if( abs(degraded_data_1d[i]) >= Threshold ):
            detect[i] = 1

    # Plotting original, degraded and detected clicks
    figure, axs = plt.subplots(3, 1)
    axs[0].plot(audio_data_1d)
    axs[0].set_title('Original Audio Data')
    axs[1].plot(degraded_data_1d)
    axs[1].set_title('Degraded Audio Data')
    axs[2].plot(detect)
    axs[2].set_title('Clicks')

    for ax in axs.flat:
        ax.label_outer()

    plt.show()


    # Creating a copy of degraded data
    res_data = degraded_data_1d

    degraded_data_1d = degraded_data_1d.tolist()

    # Computing best filter length
    window = get_filter_len(degraded_data_1d)

    # print(" Best filter len : ",window)

    # data point required before and after click to find median of data
    padding = (window - 1) // 2

    for index in range(len(degraded_data_1d)):
        if( detect[index] == 1 ):
            res_data[index] = median.median_filter(degraded_data_1d[index - padding : index + padding + 1], window)


    # Plotting original, degraded and restored audio data
    figure, axs = plt.subplots(3, 1)
    axs[0].plot(audio_data_1d)
    axs[0].set_title('Original Audio Data')
    axs[1].plot(degraded_data_1d)
    axs[1].set_title('Degraded Audio Data')
    axs[2].plot(res_data)
    axs[2].set_title('Restored Audio Data')

    for ax in axs.flat:
        ax.label_outer()

    plt.show()

    # Writing the restored data to create a output audio file
    res_data1 = np.array(res_data)
    write("output.wav", samplerate, res_data1.astype(np.int16))

