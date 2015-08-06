# FFT Demonstration Code

Scanned PDF notes and some example code using Fast Fourier Transforms in python

# Sine Wave Ampliude Spectrum

One possible normalization convention for a FFT spectrum is to normalize such that each bin contains the peak amplitude of the sine wave corresponding to that frequency. This is good for signals at a single frequency, but it's a confusing convention for broadband signals or broadband noise. To see a demonstration of this convention, run its demonstration code:

```python
%run sine_wave_demo.py
```

This will yield the following plots, showing the single-frequency signal with a DC offset, and the spectrum which correctly reconstructs the DC offset and the signal's amplitude and phase.

![Sine Wave Signal](plot_images/sinewave_signal_signal.png?raw=true)
![Sine Wave Spectrum](plot_images/sinewave_signal_spectrum.png?raw=true)
