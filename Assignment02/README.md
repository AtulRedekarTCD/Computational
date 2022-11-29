# Audio Retoration Using Median and Cubic Spline Interpolation Methods

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
python Audio_restoration.py
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

1. For the median filter, different Filter lengths were explored to find the quality of the restoration and their MSE Errros. Below figure is of MSE against the Filter length. 

<img src="Figure_2.png" width="700">

From the graph it is seen that optimal filter length is : 11 for lowest MSE '0.6'
The comparison over the original, degraded and restored data.

<img src="Figure_1.png" width="700">

The restored data is waveform <output_medianFilter.wav>
The execution Time for 


2. cubic splines is implemented in cubic_spline.py 
The MSE for cubic_spline is '0.4'.
The execution time for Cubic spline function is '15.40' sec.
Below Figure shows the original, degraded and restored Sound data by Cubic Spline.

<img src="Figure_3.png" width="700">


3. Comparing the median Filter and Cubic Spline interpolation methods, we can conclude the notice that CubicSpline achieves a lower MSE. The runtime of Median Filter method is 

After listening to the two method restored files, I notice that Cublic spline has some clicks and median filter is more clear and almost no clicks.



## Credits

This code was developed for purely for academic purposes by Atul Redekar github profile name - AtulRedekarTCD as part of the module computational Module.

## Resources
- For Implementation of CubicSpline https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.CubicSpline.html 
- 





