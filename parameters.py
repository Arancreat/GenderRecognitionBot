import librosa.display
import numpy as np
from scipy.stats import gmean

# signal - амплитуда
# sample_rate - частота дискретизации
# max_time - длительность сигнала
voice = 'alexey_voice.wav'
signal, sample_rate = librosa.load(voice)
max_time = signal.size / sample_rate

# time_steps - время
time_steps = np.linspace(0, max_time, signal.size)

# freq_steps - амплитуда
# f - частота
f = np.abs(np.fft.fft(signal))
freq = np.fft.rfftfreq(len(signal), d=1 / sample_rate) / 10000

# mean - средняя частота
spec = np.abs(np.fft.rfft(signal))
amp = spec / spec.sum()
mean = (freq * amp).sum()

# sd
sd = np.sqrt(np.sum(amp * ((freq - mean) ** 2)))

# median
amp_cumsum = np.cumsum(amp)
median = freq[len(amp_cumsum[amp_cumsum <= 0.5]) + 1]

# mode
mode = freq[amp.argmax()]

# Q25, Q75, IQR
Q25 = freq[len(amp_cumsum[amp_cumsum <= 0.25]) + 1]
Q75 = freq[len(amp_cumsum[amp_cumsum <= 0.75]) + 1]
IQR = Q75 - Q25

# skew, kurt, sfm
z = amp - amp.mean()
w = amp.std()
skew = ((z ** 3).sum() / (len(spec) - 1)) / w ** 3
kurt = ((z ** 4).sum() / (len(spec) - 1)) / w ** 4
spec_flatness = gmean(spec ** 2) / np.mean(spec ** 2)

print(f'meanfreq = {mean}\nsd = {sd}\nmedian = {median}\n'
      f'Q25 = {Q25}\nQ75 = {Q75}\nIQR = {IQR}\n'
      f'skew = {skew}\nkurt = {kurt}\nsfm = {spec_flatness}\n'
      f'mode = {mode}')
