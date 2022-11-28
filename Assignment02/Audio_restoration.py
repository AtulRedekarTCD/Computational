import numpy as np
import random
from scipy import signal as sc
from scipy.io import wavfile
import matplotlib.pyplot as plt
import median_filter as median
from scipy.io.wavfile import write

samplerate, audio_data = wavfile.read("apple_audio.wav")

samplerate, degraded_data = wavfile.read("degraded.wav")

audio_data_1d = audio_data[:, 1]

degraded_data_1d = degraded_data[:, 1]

detect = np.zeros(len(degraded_data_1d))

for i in range(len(degraded_data_1d)):
    if( abs(degraded_data_1d[i]) >= 32000):
        detect[i] = 1

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

# For Normalized Values
# Normalized_data = (degraded_data_1d / degraded_data_1d.max() )
# print(Normalized_data)

# plt.figure(figsize=(14, 8), dpi=80)
# plt.plot(Normalized_data)
# plt.show()


		
# plt.figure(figsize=(14, 8), dpi=80)
# plt.plot(detect)
# plt.show()

res_data = degraded_data_1d

degraded_data_1d = degraded_data_1d.tolist()

windows = [3,5,7,9,11,13,15,17,19]
MSE = np.zeros(len(windows))

for w in range(len(windows)):
    
    window = windows[w]	
    padding = (window - 1) // 2

    for index in range(len(degraded_data_1d)):
        if( abs(degraded_data_1d[index]) >= 32000):
            res_data[index] = median.median_filter(degraded_data_1d[index - padding : index + padding + 1], window)

    MSE[w] =  np.square(np.subtract(audio_data_1d,res_data)).mean()
    # print(MSE[w]," : ",window)

plt.plot(windows,MSE,'-r*')
plt.xlim(1,20,1)
plt.ylim(0.4,1.8)
plt.xlabel("Filter Length")
plt.ylabel("MSE")
plt.title("MSE vs Filter Size")
plt.show()

# Best Filter LE gth from the Data
window = 11

for index in range(len(degraded_data_1d)):
        if( abs(degraded_data_1d[index]) >= 32000):
            res_data[index] = median.median_filter(degraded_data_1d[index - padding : index + padding + 1], window)


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

res_data1 = np.array(res_data)
write("output.wav", samplerate, res_data1.astype(np.int16))