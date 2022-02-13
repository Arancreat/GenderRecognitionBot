import librosa.display
import matplotlib.pyplot as plt
import numpy as np

# signal - амплитуда
# sample_rate - частота дискретизации
# max_time - длительность сигнала
voice = 'my_voice.wav'
signal, sample_rate = librosa.load(voice)
max_time = signal.size / sample_rate

# time_steps - время
time_steps = np.linspace(0, max_time, signal.size)
plt.figure()
plt.plot(time_steps, signal)
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")

# freq_steps - амплитуда
# f - частота
f = np.abs(np.fft.fft(signal))
freq_steps = np.fft.fftfreq(signal.size, d=1 / sample_rate)
plt.figure()
plt.plot(freq_steps, f)
plt.xlabel("Frequency [Hz]")
plt.ylabel("Amplitude")
plt.show()
