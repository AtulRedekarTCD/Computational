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

start = time.time()

click_index = np.where(detect == 1)

data_n = degraded_data_1d
aranged_data = np.arange(len(data_n))


x_data = np.delete(aranged_data, click_index)
y_data = np.delete(data_n, click_index)


for i in tqdm(range(0, 100)):
    restored = CubicSpline(x_data, y_data)
    time.sleep(0.1)

for i in range(len(click_index)):
    data_n[click_index[i]] = restored(click_index)[i]

stop = time.time()

print(" Execution time for cubic Spline : ", format(stop - start))

MSE = np.square(np.subtract(audio_data_1d, data_n)).mean()
print(" MSE ", abs(MSE))

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

# Writing the restored data to create a output audio file
res_data1 = np.array(data_n)
write("output_cubic_spline.wav", samplerate, res_data1.astype(np.int16))
