import numpy as nm
from amplitude_and_power_spectrum import amplitude_and_power_spectrum

# generate a sine wave at 3 Hz
# sampled 100 times per second
# for 60 seconds
# with a phase angle of 20 degrees
# an amplitude of 1 volt
# and a DC offset of 2 volts
time = nm.arange(0.0,60.0,0.01) # seconds
f_signal = 3.0 # Hz
phase_angle = 20.0 # degrees
# note that exp(-ix) = cos(x) - i*sin(x)
voltage = nm.cos(2.0*nm.pi*f_signal*time)*nm.cos(phase_angle*(nm.pi/180.0)) - nm.sin(2.0*nm.pi*f_signal*time)*nm.sin(phase_angle*(nm.pi/180.0)) + 2.0

# take the amplitude spectrum
freq,amplitudes,phase = amplitude_and_power_spectrum(voltage, 0.01, return_amplitudes=True)

# plot everything
import pylab
pylab.figure(1)
pylab.clf()
pylab.subplot(211)
pylab.plot(time,voltage)
pylab.xlabel('Time [s]')
pylab.ylabel('Voltage [V]')
pylab.title('Voltage Signal: 3 Hz Sine Wave for 60 Seconds')
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
pylab.plot(freq,amplitudes,linestyle='None',marker='*',markersize=20)
pylab.xlabel('Frequency [Hz]')
pylab.ylabel('Amplitude [V]')
pylab.title('Amplitude/Phase Spectrum')
pylab.subplot(212)
# note that where the amplitude is zero, the phase angle will just be numerical roundoff error
# so, let's hack that a bit and define those bins to have a phase of "not a number"
tiny_amplitude_locations = nm.where(amplitudes < 1.0e-10)[0]
phase[tiny_amplitude_locations] = nm.nan
pylab.plot(freq,phase*(180.0/nm.pi),linestyle='None',marker='*',markersize=20)
pylab.xlabel('Frequency [Hz]')
pylab.ylabel('Phase Angle [deg]')
pylab.xlim([0,50.0])
pylab.ylim([-1.0,21.0])
pylab.title('   ')
pylab.tight_layout()

pylab.ion()
pylab.show()
