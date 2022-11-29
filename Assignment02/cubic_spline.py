import numpy as np
import random
from scipy import signal as sc
from scipy.io import wavfile
import matplotlib.pyplot as plt
import median_filter as median
from scipy.io.wavfile import write
from scipy.interpolate import CubicSpline
import time
from tqdm import tqdm
from playsound import playsound

# reading Data from Audio files
samplerate, audio_data = wavfile.read("apple_audio.wav")
samplerate, degraded_data = wavfile.read("degraded.wav")

# Using single channel
audio_data_1d = audio_data[:, 1]
degraded_data_1d = degraded_data[:, 1]

# Creating a Array of detect for position of clicks
detect = np.zeros(len(degraded_data_1d))

# Creating a detection array from degraded_data with certain threshold
Threshold = 32000
for i in range(len(degraded_data_1d)):
    if (degraded_data_1d[i] >= Threshold):
        detect[i] = 1

for i in range(len(degraded_data_1d)):
    if (degraded_data_1d[i] <= (Threshold * -1)):
        detect[i] = 1

# Plotting original, degraded and detected clicks
figure, axs = plt.subplots(3, 1)
axs[0].plot(audio_data_1d)
axs[0].set_title('Original Audio Data')
axs[1].plot(degraded_data_1d)
axs[1].set_title('Degraded Audio Data')
axs[2].plot(detect)
axs[2].set_title('Clicks')

plt.show()
plt.pause(3)
plt.close

start = time.time()

click_index = np.where(detect == 1)

data_n = degraded_data_1d
aranged_data = np.arange(len(data_n))

# Array indexs of clicks
x_data = np.delete(aranged_data, click_index)

# Array of data where clicks are present
y_data = np.delete(data_n, click_index)

# interpolating from cubic spline 
for i in tqdm(range(0, 100)):
    restored = CubicSpline(x_data, y_data)
    # time.sleep(0.1)

for i in range(len(click_index)):
    data_n[click_index[i]] = restored(click_index)[i]

stop = time.time()

# Calculating execution time 
Exe_time_cubic_spline = format(stop - start)
print(" Execution time for cubic Spline : ", Exe_time_cubic_spline)

MSE = np.square(np.subtract(audio_data_1d, data_n)).mean()
print(" MSE Cubic Spline : ", MSE)

samplerate, degraded_data1 = wavfile.read("degraded.wav")
deg_data = degraded_data1[:, 1]

# Plotting original, degraded and restored audio data
figure, axs = plt.subplots(3, 1)
axs[0].plot(audio_data_1d)
axs[0].set_title('Original Audio Data')
axs[1].plot(deg_data)
axs[1].set_title('Degraded Audio Data')
axs[2].plot(data_n)
axs[2].set_title('Restored Audio Data Cubic Spline')

for ax in axs.flat:
    ax.label_outer()

plt.show()
plt.pause(3)
plt.close()

# Writing the restored data to create a output audio file
res_data = np.array(data_n)
write("output_cubic_spline.wav", samplerate, res_data.astype(np.int16))

playsound("deg_audio_msg.mp3")
time.sleep(1)
playsound("degraded.wav")

playsound("res_audio_msg.mp3")
time.sleep(1)
playsound("output_cubic_spline.wav")