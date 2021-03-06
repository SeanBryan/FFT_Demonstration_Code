# FFT Demonstration Code

This repository contains scanned PDF notes and some example code about using Fast Fourier Transforms (FFT) to analyze data in python. FFTs allow you to extract the amplitude and phase of purely periodic signals in data, measure the total power contained in a dataset across a broad bandwidth, or filter out noise from data to create a low-noise version of a dataset.

scanned_FFT_notes.pdf contains notes discussing the math basics of the FFT algorithm. The file amplitude_and_power_spectrum.py is a single python function that illustrates using SciPy's fft function and properly normalizing it for two common use cases discussed in the PDF notes and in the examples below.

By the way, the book "Numerical Recipes in C" has an excellent two chapters about the FFT algorithm. I highly reccomend reading them carefully at some point if you find yourself using the FFT algorithm often in your work. It's in the library, and an earlier edition is in the public domain which is really great. Here's a link to a pdf of that version:

http://www2.units.it/ipl/students_area/imm2/files/Numerical_Recipes.pdf

# Sine Wave Ampliude Spectrum

One possible normalization convention for a FFT spectrum is to normalize such that each bin contains the peak amplitude of the sine wave corresponding to that frequency. This is good for signals at a single frequency, but it's a confusing convention for broadband signals or broadband noise. To see a demonstration of this convention, run its demonstration code:

```python
%run sine_wave_demo.py
```

This will yield the following plots, showing the single-frequency signal with a DC offset, and the spectrum which correctly reconstructs the DC offset and the signal's amplitude and phase.

![Sine Wave Signal](plot_images/sinewave_signal_timestream.png?raw=true)
![Sine Wave Spectrum](plot_images/sinewave_signal_spectrum.png?raw=true)

# Power Spectral Density

Another possible normalization convention for a FFT spectrum is to normalize such that the spectrum has the units of power spectral density. This is good for broadband signals or broadband noise, because it allows the spectrum to be integrated across a particular audio band to yield a measurement of total rms power in that audio band. To see a demonstration of this convention, run its demonstration code:

```python
%run signal_and_noise_bandwidth_demo.py
```

This will yield the following plots, showing the signal with bandwidth from 2.95 Hz to 3.00 Hz and broadband white noise. It also shows that the power spectral density correctly reconstructs the RMS of the broadband signal, and the white noise power.

![Bandwidth Signal](plot_images/bandwidth_signal_timestream.png?raw=true)
![Bandwidth Spectrum](plot_images/bandwidth_signal_spectrum.png?raw=true)

# Filtering

Another important application of the FFT is filtering signals. This example implements the raised cosine filter (read more on its wikipedia article!) to filter out high frequency noise from data. The plan is to construct a transfer function which is an array of transmission-vs-audio-frequency, multiply that by the FFT of the data, and then inverse FFT to yield a filtered timestream. The top figure shows this transfer function, which is defined for both positive and negative frequencies according to the usual FFT convention. That works well, except as the low-noise example plot shows since the FFT enforces periodicity on the dataset there can be weird start and stop transients in the filtered timestream. One way to avoid this is to create copies of the data before and after (padding), then do this filtering, then only use the middle copy of the data leaving the transients in the other two copies. This yields the bottom graph, which also shows how this method works well even in the presence of a lot of noise.

```python
%run lowpass_cosine_with_fft.py
```

![Transfer Function](plot_images/filter_transfer_function.png?raw=true)
![Filter Transient](plot_images/filter_example_data_with_ringing.png?raw=true)
![No Transient and High Noise](plot_images/filter_example_data_noisy.png?raw=true)


