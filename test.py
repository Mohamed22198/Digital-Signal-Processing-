import tkinter as tk
from tkinter import filedialog, ttk
import numpy as np
import matplotlib.pyplot as plt


def browse_file_1():
    global data
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        # Extract the file name from the path
        selected_file = file_path.split("/")[-1]
        # selected_file = file_path.split("\\")[-1]
        selected_file_label["text"] = selected_file
        data = read_signal_data_1(file_path)
        # plot_signal_1(data)

def read_signal_data_1(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.read().splitlines()

        if len(lines) < 3:
            print("Invalid file format.")
            return None

        num_samples = int(lines[2])
        data = []

        for i in range(3, 3 + num_samples):
            parts = lines[i].split()
            if len(parts) != 2:
                print("Invalid line format.")
                return None
            index, amplitude = float(parts[0]), float(parts[1])
            data.append((index, amplitude))

        return data

    except Exception as e:
        print("Error reading the file:", e)
        return None

def calculate_fourier_transform(data, sampling_frequency):
    N = len(data)
    time = [point[0] for point in data]
    signal = [point[1] for point in data]
    freq = np.fft.fftfreq(N, 1.0 / sampling_frequency)
    fft_result = np.fft.fft(signal)

    amplitude = np.abs(fft_result) / N
    phase = np.angle(fft_result)

    return freq, amplitude, phase

def plot_frequency_amplitude_and_phase(freq, amplitude, phase):
    plt.figure(figsize=(10, 5))

    # Continuous representation
    plt.subplot(1, 2, 1)
    plt.plot(freq, amplitude)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Amplitude")
    plt.title("Frequency vs Amplitude")

    # Discrete representation
    plt.subplot(1, 2, 2)
    plt.plot(freq, phase)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Phase (radians)")
    plt.title("Frequency vs Phase")
    plt.grid()

    plt.tight_layout()
    plt.show()

def DFT_button_3():
    sampling = sampling_frequency_entry.get()
    freq, amplitude, phase = calculate_fourier_transform(data,sampling)
    plot_frequency_amplitude_and_phase(freq, amplitude, phase)
# main window
root = tk.Tk()
root.geometry("800x500")
root.title("DSP Task")

header_label = ttk.Label(root, text="DSP Task", font=("Arial", 20))
header_label.pack(pady=20)

upload_button = ttk.Button(root, text="Upload Text File", command=browse_file_1)
upload_button.pack()

# display the selected file name
selected_file_label = ttk.Label(root)
selected_file_label.pack(pady=10)

sampling_frequency_label = ttk.Label(root, text="Sampling Frequency:")
sampling_frequency_label.pack()
sampling_frequency_entry = ttk.Entry(root)
sampling_frequency_entry.insert(0, "")
sampling_frequency_entry.pack()

# Create a button to generate the signal
generate_button = ttk.Button(root, text="Generate Signal", command=DFT_button_3)
generate_button.pack(pady=20)

root.mainloop()