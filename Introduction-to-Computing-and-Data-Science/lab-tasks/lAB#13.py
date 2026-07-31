"""
LAB # 13: Signal Manipulation & Processing in Python
"""

import matplotlib.pyplot as plt
import numpy as np

# %% Basic Sine Wave Generation

f = 2
t = np.linspace(0, 5, 1000)
v = np.sin(2 * np.pi * f * t)

plt.figure(figsize=(10, 5), dpi=100)
plt.plot(t, v)

plt.xlabel("Time (sec)")
plt.ylabel("Amplitude (Volts)")

# %% Multiple Frequency Sine Waves

t = np.linspace(0, 1, 200)
multiples = 4
plt.figure(figsize=(10, 5), dpi=100)

for k in range(1, multiples + 1):
    f = k
    v = v = np.sin(2 * np.pi * f * t)
    plt.plot(t, v, label=str(f) + ' Hz')

plt.legend()
plt.xlabel("Time (sec)")
plt.ylabel("Amplitude (Volts)")

# %% Fourier Series - Odd Harmonics with Amplitude Scaling

t = np.linspace(0, 1, 200)

multiples = 8

plt.figure(figsize=(10, 5), dpi=100)

for k in range(1, multiples + 1):
    f = 2 * k - 1
    magnitude = (4/np.pi) * (1/f)
    v = magnitude * np.sin(2 * np.pi * f * t)

    plt.plot(t, v, label=str(f) + ' Hz')

plt.legend()
plt.xlabel("Time (sec)")
plt.ylabel("Amplitude (Volts)")

# %% Square Wave Approximation (20 Harmonics)

square = 1
t = np.linspace(0, 1, 200)
multiples = 20

for k in range(1, multiples + 1):
    f = 2*k - 1
    magnitude = (4/np.pi) * (1/f)
    v = magnitude * np.sin(2 * np.pi * f * t)
    square += v

plt.figure(figsize=(10, 5), dpi=100)

plt.plot(t, square, label='Odd freq. sum 1 to ' + str(f) + ' Hz')

plt.legend()

plt.xlabel("Time (sec)")
plt.ylabel("Amplitude (Volts)")

# %% Square Wave Approximation (15 Harmonics)

square = 1
t = np.linspace(0, 1, 200)
multiples = 15

for k in range(1, multiples + 1):
    f = 2*k - 1
    magnitude = (4/np.pi) * (1/f)
    v = magnitude * np.sin(2 * np.pi * f * t)
    square += v

plt.figure(figsize=(10, 5), dpi=100)

plt.plot(t, square, label='Odd freq. sum 1 to ' + str(f) + ' Hz')

plt.legend()

plt.xlabel("Time (sec)")
plt.ylabel("Amplitude (Volts)")

# %% Frequency Spectrum - Stem Plot

square = 1
t = np.linspace(0, 1, 200)

freq, mag = [], []

odd_multiples = 15

for k in range(1, odd_multiples + 1):
    f = 2*k - 1
    magnitude = (4/np.pi) * (1/f)
    v = magnitude * np.sin(2 * np.pi * f * t)
    square += v

    freq.append(f)
    mag.append(magnitude)

plt.figure(figsize=(10, 5), dpi=100)
plt.stem(freq, mag)

plt.xticks(freq)

plt.xlabel("Time (sec)")
plt.ylabel("Amplitude (Volts)")

# %% DTMF Signal Generation and Visualization

t = np.linspace(0, 1, 44100)

fv1, fh1 = 770, 1209

v1, v2 = np.sin(2 * np.pi * fv1 * t), np.sin(2 * np.pi * fh1 * t)

signal = v1 + v2

plt.figure(figsize=(10, 5), dpi=100)
plt.plot(t[:500], signal[:500], label='v1 + v2')

plt.legend()
plt.xlabel("Time (sec)")
plt.ylabel("Amplitude (Volts)")

# from IPython.display import Audio
# Audio(signal, rate = 44100)

# %% DTMF Digit Recognition using Correlation

fv1, fh1, fh2 = 697, 1209, 1336

sin_fv1 = np.sin(2 * np.pi * fv1 * t)
sin_fh1, sin_fh2 = np.sin(2 * np.pi * fh1 * t), np.sin(2 * np.pi * fh2 * t)

dtmf_digit1, dtmf_digit2 = sin_fv1 + sin_fh1, sin_fv1 + sin_fh2

dtmf_digits_signals = [dtmf_digit1, dtmf_digit2]
value = []

for digital_signal in dtmf_digits_signals:
    out = np.sum(signal * digital_signal)
    value.append(out)

print(value)
print(f"Maxmimum value = {max(value)}")

print(f"Index of maximum value: {value.index(max(value))}")
print("The siganl has similarity to digit 2")

# %% [markdown]
# ## Cell 9: Complete DTMF Decoder with Frequency Tolerance

t = np.linspace(0, 1, 44100)

# DTMF frequency pairs for each digit
dial_num_dict = {
    '1': (697, 1209), '2': (697, 1336), '3': (697, 1477),
    '4': (770, 1209), '5': (770, 1336), '6': (770, 1477),
    '7': (852, 1209), '8': (852, 1336), '9': (852, 1477),
    '*': (941, 1209), '0': (941, 1336), '#': (941, 1477)
}


def dtmfSignalGenerator(f1, f2, t):
    return np.sin(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t)


# given frequencies that should correspond to digit 2
fv1, fh1 = 840, 1330
signal = dtmfSignalGenerator(fv1, fh1, t)

# function to calculate correlation with tolerance for both frequencies


def correlateSignal(input_signal, t, dial_num_dict, tol_f1=36, tol_f2=60):
    max_similar = 0
    detected_digit = None

    for digit, (f1, f2) in dial_num_dict.items():
        if ((fv1 - tol_f1 < f1 < fv1 + tol_f1) and
                (fh1 - tol_f2 < f2 < fh1 + tol_f2)):
            # generate DTMF signal for the current digit
            dtmf_signal = dtmfSignalGenerator(f1, f2, t)
            # compute the similarity using cross-correlation
            correlation = np.correlate(
                input_signal, dtmf_signal, mode='valid')[0]

            # track the maximum similarity and corresponding digit
            if correlation > max_similar:
                max_similar = correlation
                detected_digit = digit

    return detected_digit, max_similar


# detect the digit from the input signal
detected_digit, max_similar = correlateSignal(signal, t, dial_num_dict)

if detected_digit is None:
    print("No valid digit detected.")
else:
    print(f"Detected Digit: {
          detected_digit}\nMaximum Similarity: {max_similar}")

    f1, f2 = dial_num_dict[detected_digit]
    detected_signal = dtmfSignalGenerator(f1, f2, t)

    plt.figure(figsize=(10, 5), dpi=100)

    plt.plot(t[:500], signal[:500], label='Input Signal (Digit 2)', alpha=0.7)
    plt.plot(t[:500], detected_signal[:500], label=f'Actual Signal (Digit {
        detected_digit})', linestyle='--', alpha=0.7)

    plt.legend()
    plt.xlabel("Time (sec)")
    plt.ylabel("Amplitude (Volts)")
    plt.title(f"DTMF Signal for Detected Digit {detected_digit}")

    plt.grid(True)
    plt.show()
