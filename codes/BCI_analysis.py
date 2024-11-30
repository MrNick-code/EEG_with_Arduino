import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt
import numpy as np

# Processing and files extraction 
def process_data(file_path):
    times = [] 
    channel_0_freqs = []   
    channel_1_freqs = []  

    with open(file_path, 'r', encoding='utf-8') as file:  # forces UTF-8 read
        time_index = 0
        for line in file:
            line = line.strip()
            if "Canal: 0" in line and "Frequência dominante:" in line:
                try:
                    freq = float(line.split("Frequência dominante:")[1].split("Hz")[0].strip())
                    channel_0_freqs.append(freq)
                except (IndexError, ValueError):
                    pass
            elif "Canal: 1" in line and "Frequência dominante:" in line:
                try:
                    freq = float(line.split("Frequência dominante:")[1].split("Hz")[0].strip())
                    channel_1_freqs.append(freq)
                    times.append(time_index) \
                    time_index += 1
                except (IndexError, ValueError):
                    pass

    return times, channel_0_freqs, channel_1_freqs

# Function for Butterworth filter
def apply_filter(data, cutoff=10, fs=50, order=4):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return filtfilt(b, a, data)

def plot_data(times, channel_0_freqs, channel_1_freqs, filtered_0, filtered_1):
    plt.figure(figsize=(12, 8))

    plt.subplot(2, 1, 1)
    plt.plot(times, channel_0_freqs, label="Canal 0 (Original)", color='blue', marker='o', linestyle='-')
    plt.plot(times, channel_1_freqs, label="Canal 1 (Original)", color='orange', marker='x', linestyle='-')
    plt.xlabel("Tempo (amostras consecutivas)")
    plt.ylabel("Frequência dominante (Hz)")
    plt.title("Frequências Dominantes (Original)")
    plt.legend()
    plt.grid(True)

    plt.subplot(2, 1, 2)
    plt.plot(times, filtered_0, label="Canal 0 (Filtrado)", color='blue', linestyle='--')
    plt.plot(times, filtered_1, label="Canal 1 (Filtrado)", color='orange', linestyle='--')
    plt.xlabel("Tempo (amostras consecutivas)")
    plt.ylabel("Frequência dominante (Hz)")
    plt.title("Frequências Dominantes (Filtradas)")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()

# File path (edit as needed)
file_path = "C:/Users/mathe/Downloads/BCIhist1.txt"

times, channel_0_freqs, channel_1_freqs = process_data(file_path)

filtered_channel_0 = apply_filter(np.array(channel_0_freqs))
filtered_channel_1 = apply_filter(np.array(channel_1_freqs))

plot_data(times, channel_0_freqs, channel_1_freqs, filtered_channel_0, filtered_channel_1)
