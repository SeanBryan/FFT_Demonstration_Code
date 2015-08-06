import numpy as nm
from amplitude_and_power_spectrum import amplitude_and_power_spectrum

# generate power from 2.95 to 3.0 Hz
# sampled 100 times per second
# for 5 seconds
# with a total signal rms of 1 volt
time = nm.arange(0.0,5.0,0.01) # seconds
# let's do this by actually having ten sine waves of equal amplitude superposed
# the amplitude of each will need to be 0.1*sqrt(2) to get the total amplitude to be sqrt(2)
# the rms of that will be a factor of sqrt(2) smaller, i.e. 1.0
f_signals = nm.arange(2.950,3.005,0.005) # i.e. 2.95 to 3.0
voltage = nm.zeros_like(time)
for f in f_signals:
	voltage = voltage + 0.1*nm.sqrt(2.0)*nm.cos(2.0*nm.pi*f*time)

# now add white noise whose rms across all frequencies is 0.25
voltage = voltage + 0.25*nm.random.randn(len(voltage))

# take the power spectrum
freq,v_sqrt_hz = amplitude_and_power_spectrum(voltage, 0.01, return_amplitudes=False)

# do the rms integral from 2.6 to 3.6 Hz to measure the rms signal power
df = nm.mean(nm.diff(freq))
# note that freq[13] = 2.6 Hz and freq[18] = 3.6 Hz
rms_signal = nm.sqrt(nm.sum(v_sqrt_hz[13:19]**2.0)*df)

# do the rms integral at all frequencies that are NOT in the range 2.6 to 3.6 Hz to measure the rms noise power
rms_noise = nm.sqrt(nm.sum(v_sqrt_hz[0:13]**2.0)*df + nm.sum(v_sqrt_hz[19:]**2.0)*df)

# plot everything
import pylab
pylab.figure(1)
pylab.clf()
pylab.subplot(211)
pylab.plot(time,voltage)
pylab.xlabel('Time [s]')
pylab.ylabel('Voltage [V]')
pylab.title('Voltage Signal: 2.95-3.00 Hz Power for 5 Seconds with an RMS of 1.0 V\nVoltage Noise: 0.25 V RMS White Noise')
pylab.subplot(212)
pylab.plot(time,voltage,linestyle='None',marker='*')
pylab.xlabel('Time [s]')
pylab.ylabel('Voltage [V]')
pylab.xlim([0,1.0])
pylab.title('Zoom-in')
pylab.tight_layout()

pylab.figure(2)
pylab.clf()
pylab.subplot(211)
pylab.plot(freq,v_sqrt_hz)
pylab.xlabel('Frequency [Hz]')
pylab.ylabel('Power Spectral Density\n[V/sqrt(Hz)]')
pylab.title('Measured Signal RMS = ' + str(rms_signal)[0:5] + ' Measured Noise RMS = ' + str(rms_noise)[0:5])
pylab.subplot(212)
pylab.semilogy(freq,v_sqrt_hz)
pylab.xlabel('Frequency [Hz]')
pylab.ylabel('Power Spectral Density\n[V/sqrt(Hz)]')
pylab.title('Log-scale')
pylab.tight_layout()

pylab.ion()
pylab.show()
