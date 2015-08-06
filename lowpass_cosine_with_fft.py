import numpy as nm
import scipy
import scipy.fftpack
import pylab

# Sean Bryan
# sean.a.bryan@asu.edu
# 9/5/2014

def lowpass_cosine( y, tau, f_3db, width, padd_data=True):
    # padd_data = True means we are going to symmetric copies of the data to the start and stop
    # to reduce/eliminate the discontinuities at the start and stop of a dataset due to filtering
    #
    # False means we're going to have transients at the start and stop of the data

    # kill the last data point if y has an odd length
    if nm.mod(len(y),2):
        y = y[0:-1]

    # add the weird padd
    # so, make a backwards copy of the data, then the data, then another backwards copy of the data
    if padd_data:
        y = nm.append( nm.append(nm.flipud(y),y) , nm.flipud(y) )

    # take the FFT
    ffty=scipy.fftpack.fft(y)
    ffty=scipy.fftpack.fftshift(ffty)

    # make the companion frequency array
    delta = 1.0/(len(y)*tau)
    nyquist = 1.0/(2.0*tau)
    freq = nm.arange(-nyquist,nyquist,delta)
    # turn this into a positive frequency array
    pos_freq = freq[(len(ffty)/2):]

    # make the transfer function for the first half of the data
    i_f_3db = min( nm.where(pos_freq >= f_3db)[0] )
    f_min = f_3db - (width/2.0)
    i_f_min = min( nm.where(pos_freq >= f_min)[0] )
    f_max = f_3db + (width/2);
    i_f_max = min( nm.where(pos_freq >= f_max)[0] )

    transfer_function = nm.zeros(len(y)/2)
    transfer_function[0:i_f_min] = 1
    transfer_function[i_f_min:i_f_max] = (1 + nm.sin(-nm.pi * ((freq[i_f_min:i_f_max] - freq[i_f_3db])/width)))/2.0
    transfer_function[i_f_max:(len(freq)/2)] = 0

    # symmetrize this to be [0 0 0 ... .8 .9 1 1 1 1 1 1 1 1 .9 .8 ... 0 0 0] to match the FFT
    transfer_function = nm.append(nm.flipud(transfer_function),transfer_function)

    # plot up the transfer function
    # since "freq" is only the positive frequencies, select out
    pylab.figure(1)
    pylab.clf()
    pylab.plot(freq,transfer_function)
    pylab.xlabel('Frequency [Hz]')
    pylab.ylabel('Filter Transfer Function')
    pylab.xlim([-10.0,10.0])
    pylab.ylim([-0.05,1.05])

    # apply the filter, undo the fft shift, and invert the fft
    filtered=nm.real(scipy.fftpack.ifft(scipy.fftpack.ifftshift(ffty*transfer_function)))

    # remove the padd, if we applied it
    if padd_data:
        filtered = filtered[(len(y)/3):(2*(len(y)/3))]

    # return the filtered data
    return filtered


# do an example of lowpass filtering
# first make some fake data
# a sine wave fluctuating once every pi seconds
# samples 1000 times per second
fakedata = nm.sin(nm.arange(0,11,0.001)) + nm.random.randn(len(nm.arange(0,11,0.001)))/4.0

# run the filter
# lowpass at 5 Hz, with a 1 Hz width of its roll-off
filtered = lowpass_cosine(fakedata,0.001,5.0,1.0,padd_data=True)

# plot the noisy data, with the filtered data on top
pylab.figure(2)
pylab.clf()
pylab.plot(nm.arange(0,11,0.001),fakedata,label='Noisy Data')
pylab.plot(nm.arange(0,11,0.001),filtered,label='Lowpass Filtered Data')
pylab.xlabel('Time [s]')
pylab.ylabel('Voltage')
pylab.legend()

pylab.ion()
pylab.show()

