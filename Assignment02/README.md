# Add here a title for the project
Audio Retoration Using Median and Cubic Spline Interpolation Methods

## High-level Description of the project
This Assignment is remove tnhe clicks from Audio signal using median filter and cubic spline interpolation techniques.
- median filtering
It is a non linear filter based on the principle of removing outliners using simple median technique. Although it 
does not remove all the spikes but removes considerable noise from audio signal. 
- cubic splines
It is another technique of interpolation based on principles of polynomials with control points called as "Knots".
It computes the line from third order piecewise cubic function which interpolates data points between knots and 
provide more smoothness for the signal.
---

## Installation and Execution

Provide details on the Python version and libraries (e.g. numpy version) you are using. One easy way to do it is to do that automatically:
```sh                                 
pip3 install pipreqs

pipreqs $project/path/requirements.txt
```
For more details check [here](https://github.com/bndr/pipreqs)


Afer installing all required packages you can run the demo file simply by typing:
```sh
python demo_audio_restoration.py
```
---

## Methodology and Results
Step 1:
Read the original Audio and degraded File using wavefile functions
Also store only one channel data into a array. We don't require the 2 channels data.
plot the original and degraded data using matplotlib

Step 2:
Now, we can figure out the clicks on the graph. created a data array called "Detect".
Detect has '1' for every click and '0' for rest audio data.
Plot the clicks graph as well.

step 3:
median filter implementation:
The algorithm is very simple just passing the array of degraded data based on considering the click as median.
For example click is at index = 7. inpjut to the median filter is [ 7 - Padding_data : 7 + Padding_data ]
where as length of Padding_data depends on the provided filter length. 
For,
Filter length 3 padding data required is 1 
for filter length 5 Padding data required is 2 and so on..

The filter will sort this input in ascending order.
It will return the median from the array.
Now, replace the click value with the median value computed

Step 4:
Get the best value for filter length. Considered value from 3 to 19 and computed the MSE for each of the 
filter length.
plot the graph of MSE against the filter length. 
get_filter_len() will return the best filter length for the audio data.

Step 5:
Now, using the filter length restore the data from median filter function.
Plot the output data file.

Step 6:
write the output data into the 'output.wav' file


**Results**

1. For the median filter, different lengths were explored to test the effectiveness of the restoration. In particular, XXXX were tested and XXX was observed to deliver the lowest MSE, as shown in the figure below.

<img src="MedianFilter_MSEvsLength.png" width="350">

The restored waveform <output_medianFilter.wav> with the optimal filter length is given below:



2. Using the cubic splines, we observe ....

The restored waveform <output_cubicSplines.wav> with the optimal filter length is given below:


3. Comparing the two different interpolation methods, we notice that method X achieves a lower MSE. The runtime of XX method is .....

After listening to the two restored files, we notice ...


---
## Credits

This code was developed for purely academic purposes by XXXX (add github profile name) as part of the module ..... 

Resources:
- XXXX
- XXX





