# FFT Demonstration Code

Scanned PDF notes and some example code using Fast Fourier Transforms in python

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

![Sine Wave Signal](plot_images/bandwidth_signal_timestream.png?raw=true)
![Sine Wave Spectrum](plot_images/bandwidth_signal_spectrum.png?raw=true)
