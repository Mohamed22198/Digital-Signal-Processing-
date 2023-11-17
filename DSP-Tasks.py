import tkinter as tk
from tkinter import filedialog, ttk
import numpy as np
import matplotlib.pyplot as plt

#***************************** TASK 1 ******************************
def browse_file_1():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        # Extract the file name from the path
        selected_file = file_path.split("/")[-1]
        # selected_file = file_path.split("\\")[-1]
        selected_file_label["text"] = selected_file
        data = read_signal_data_1(file_path)
        if data is not None:
            plot_signal_1(data)
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
def plot_signal_1(data):
    if len(data) == 0:
        print("No data to plot.")
        return

    index = [sample[0] for sample in data]
    amplitude = [sample[1] for sample in data]

    plt.figure(figsize=(10, 5))

    # Continuous representation
    plt.subplot(1, 2, 1)
    plt.plot(index, amplitude, label="Continuous Signal", marker='o')
    plt.xlabel("Sample Index")
    plt.ylabel("Amplitude")
    plt.title("Continuous Signal Representation")
    plt.legend()

    # Discrete representation
    plt.subplot(1, 2, 2)
    plt.stem(index, amplitude, linefmt='-b', markerfmt='ob', basefmt=' ', label="Discrete Signal")
    plt.xlabel("Sample Index")
    plt.ylabel("Amplitude")
    plt.title("Discrete Signal Representation")
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()
def generate_signal_1():

    plt.figure(figsize=(12,5))

    signal_type = signal_type_combobox.get()
    A = float(A_entry.get())
    analog_frequency = float(analog_frequency_entry.get())
    sampling_frequency = float(sampling_frequency_entry.get())
    phase_shift = float(phase_shift_entry.get())

    t = np.arange(0, 1, 1 / sampling_frequency)  # Time vector

    if signal_type == "sin":
        signal = A * np.sin(2 * np.pi * analog_frequency * t + phase_shift)
        signal_label = "Sinusoidal Signal"
    elif signal_type == "cos":
        signal = A * np.cos(2 * np.pi * analog_frequency * t + phase_shift)
        signal_label = "Cosinusoidal Signal"
    else:
        print("Invalid signal type.")
        return

    # Continuous representation
    plt.subplot(1, 2, 1)
    plt.plot(t, signal, label="")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.title("Continuous Signal Representation")
    plt.legend()

    # Discrete representation
    plt.subplot(1, 2, 2)
    plt.stem(t, signal, linefmt='-b', markerfmt='ob', basefmt=' ', label="")
    plt.xlabel("Sample Index")
    plt.ylabel("Amplitude")
    plt.title("Discrete Signal Representation")
    plt.grid(True)

    plt.legend()


    plt.show()
def Task1():
    # main window
    root = tk.Tk()
    root.geometry("800x500")
    root.title("DSP Task 1")

    header_label = ttk.Label(root, text="DSP Task 1", font=("Arial", 20))
    header_label.pack(pady=20)

    upload_button = ttk.Button(root, text="Upload Text File", command=browse_file_1)
    upload_button.pack()

    # display the selected file name
    selected_file_label = ttk.Label(root)
    selected_file_label.pack(pady=10)

    # combo box to select signal type
    signal_type_combobox = ttk.Combobox(root, values=("sin", "cos"))
    signal_type_combobox.pack(pady=10)

    # entry fields for input
    A_label = ttk.Label(root, text="A:")
    A_label.pack()
    A_entry = ttk.Entry(root)
    A_entry.insert(0, "")
    A_entry.pack()

    analog_frequency_label = ttk.Label(root, text="Analog Frequency:")
    analog_frequency_label.pack()
    analog_frequency_entry = ttk.Entry(root)
    analog_frequency_entry.insert(0, "")
    analog_frequency_entry.pack()

    sampling_frequency_label = ttk.Label(root, text="Sampling Frequency:")
    sampling_frequency_label.pack()
    sampling_frequency_entry = ttk.Entry(root)
    sampling_frequency_entry.insert(0, "")
    sampling_frequency_entry.pack()

    phase_shift_label = ttk.Label(root, text="Phase Shift:")
    phase_shift_label.pack()
    phase_shift_entry = ttk.Entry(root)
    phase_shift_entry.insert(0, "")
    phase_shift_entry.pack()

    # Create a button to generate the signal
    generate_button = ttk.Button(root, text="Generate Signal", command=generate_signal_1)
    generate_button.pack(pady=20)

    root.mainloop()
#*******************************************************************
#***************************** TASK 2 ******************************
def browse_file_2(button_number):
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        # Extract the file name from the path
        selected_file = file_path.split("/")[-1]
        selected_files[button_number]["text"] = selected_file  # Display the selected file name
        data = read_signal_data_2(file_path)
        if button_number == 1:
            data1.extend(data)
        else:
            data2.extend(data)
def read_signal_data_2(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.read().splitlines()

        if len(lines) < 3:
            print("Invalid file format.")
            return None

        signal_type = int(lines[0])
        is_periodic = int(lines[1])
        num_samples = int(lines[2])
        data = []

        for i in range(3, 3 + num_samples):
            parts = lines[i].split()
            if signal_type == 0:  # Time domain
                if len(parts) != 2:
                    print("Invalid line format in time domain signal.")
                    return None
                index, amplitude = float(parts[0]), float(parts[1])
            elif signal_type == 1:  # Frequency domain
                if len(parts) != 3:
                    print("Invalid line format in frequency domain signal.")
                    return None
                index, amplitude, phase_shift = float(parts[0]), float(parts[1]), float(parts[2])
            else:
                print("Invalid signal type.")
                return None

            data.append((index, amplitude))

        return data

    except Exception as e:
        print("Error reading the file:", e)
        return None
def add_signals(data1, data2):
    if len(data1) != len(data2):
        print("Error: The signals have different lengths.")
        return None

    summed_signal = [(sample1[0], sample1[1] + sample2[1]) for sample1, sample2 in zip(data1, data2)]
    return summed_signal
def sub_signals(data1, data2):
    if len(data1) != len(data2):
        print("Error: The signals have different lengths.")
        return None

    subtracted_signal = [(sample1[0], sample1[1] - sample2[1]) for sample1, sample2 in zip(data1, data2)]
    return subtracted_signal
def multiply_signal(data, constant):
    if constant == -1:
        # Invert the signal
        multiplied_signal = [(sample[0], -sample[1]) for sample in data]
    else:
        # Multiply the signal by the constant
        multiplied_signal = [(sample[0], sample[1] * constant) for sample in data]
    return multiplied_signal
def square_signal(data):
    squared_signal = [(sample[0], sample[1] ** 2) for sample in data]
    return squared_signal
def shift_signal(data, constant):
    shifted_signal = [(sample[0] + constant, sample[1]) for sample in data]
    return shifted_signal
def normalize_signal(data, normalize_type):
    if normalize_type == 0:  # Normalize to [0, 1]
        max_amplitude = max(sample[1] for sample in data)
        min_amplitude = min(sample[1] for sample in data)

        if max_amplitude == min_amplitude:
            return data  # Avoid division by zero

        normalized_signal = [(sample[0], (sample[1] - min_amplitude) / (max_amplitude - min_amplitude)) for sample in data]
    elif normalize_type == 1:  # Normalize to [-1, 1]
        max_amplitude = max(sample[1] for sample in data)
        min_amplitude = min(sample[1] for sample in data)

        if max_amplitude == min_amplitude:
            return data  # Avoid division by zero

        normalized_signal = [(sample[0], 2 * (sample[1] - min_amplitude) / (max_amplitude - min_amplitude) - 1) for sample in data]
    else:
        return data

    return normalized_signal
def accumulate_signal(data):
    accumulated_signal = []
    accumulated_amplitude = 0

    for sample in data:
        accumulated_amplitude += sample[1]
        accumulated_signal.append((sample[0], accumulated_amplitude))

    return accumulated_signal
def plot_signal_2(data):
    if len(data) == 0:
        print("No data to plot.")
        return

    index = [sample[0] for sample in data]
    amplitude = [sample[1] for sample in data]

    plt.figure(figsize=(10, 5))

    # Continuous representation
    plt.subplot(1, 2, 1)
    plt.plot(index, amplitude, label="Continuous Signal", marker='o')
    plt.xlabel("Sample Index")
    plt.ylabel("Amplitude")
    plt.title("Continuous Signal Representation")
    plt.legend()

    # Discrete representation
    plt.subplot(1, 2, 2)
    plt.stem(index, amplitude, linefmt='-b', markerfmt='ob', basefmt=' ', label="Discrete Signal")
    plt.xlabel("Sample Index")
    plt.ylabel("Amplitude")
    plt.title("Discrete Signal Representation")
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()
def Task2():
    # main window
    root = tk.Tk()
    root.geometry("800x500")
    root.title("DSP Task 2")

    header_label = ttk.Label(root, text="DSP Task 2", font=("Arial", 20))
    header_label.pack(pady=20)

    selected_files = {}  # Dictionary to store the selected file labels

    data1 = []  # List to store data for signal 1
    data2 = []  # List to store data for signal 2

    upload_button1 = ttk.Button(root, text="Upload Text File for Signal 1", command=lambda: browse_file_2(1))
    upload_button1.pack()

    selected_file_label1 = ttk.Label(root, text="Selected File 1: ")
    selected_file_label1.pack(pady=10)
    selected_files[1] = selected_file_label1  # Store the label in the dictionary

    upload_button2 = ttk.Button(root, text="Upload Text File for Signal 2", command=lambda: browse_file_2(2))
    upload_button2.pack()

    selected_file_label2 = ttk.Label(root, text="Selected File 2: ")
    selected_file_label2.pack(pady=10)
    selected_files[2] = selected_file_label2  # Store the label in the dictionary

    add_button = ttk.Button(root, text="Add Signals", command=lambda: plot_signal_2(add_signals(data1, data2)))
    add_button.pack()

    sub_button = ttk.Button(root, text="Subtract Signals", command=lambda: plot_signal_2(sub_signals(data1, data2)))
    sub_button.pack()

    const_label = ttk.Label(root, text="Enter A Constant value to use it in Shifting or Multiplying :")
    const_label.pack()

    constant_value = tk.DoubleVar(value=1.0)
    constant_entry = ttk.Entry(root, textvariable=constant_value, width=10)
    constant_entry.pack()

    mul_button = ttk.Button(root, text="Multiply Signal by Constant",command=lambda: plot_signal_2(multiply_signal(data1, constant_value.get())))
    mul_button.pack()

    shift_button = ttk.Button(root, text="Shift Signal", command=lambda: plot_signal_2(shift_signal(data1, constant_value.get())))
    shift_button.pack()

    squaring_button = ttk.Button(root, text="Squaring Signal",command=lambda: plot_signal_2(square_signal(data1)))
    squaring_button.pack()

    normalize_type_var = tk.IntVar(value=0)  # Default: Normalize to [0, 1]

    normalize_label = ttk.Label(root, text="Normalization Type:")
    normalize_label.pack()

    normalize_radiobutton0 = ttk.Radiobutton(root, text="0 to 1", variable=normalize_type_var, value=0)
    normalize_radiobutton1 = ttk.Radiobutton(root, text="-1 to 1", variable=normalize_type_var, value=1)

    normalize_radiobutton0.pack()
    normalize_radiobutton1.pack()

    normalize_button = ttk.Button(root, text="Normalize Signal", command=lambda: plot_signal_2(normalize_signal(data1, normalize_type_var.get())))
    normalize_button.pack()


    accumulate_button = ttk.Button(root, text="Accumulate Signal", command=lambda: plot_signal_2(accumulate_signal(data1)))
    accumulate_button.pack()


    root.mainloop()
#*******************************************************************
#***************************** TASK 3 ******************************
def browse_file_3():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        selected_file_label["text"] = file_path
def QuantizationTest1(file_name,Your_EncodedValues,Your_QuantizedValues):
    expectedEncodedValues=[]
    expectedQuantizedValues=[]
    with open(file_name, 'r') as f:
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        while line:
            # process line
            L=line.strip()
            if len(L.split(' '))==2:
                L=line.split(' ')
                V2=str(L[0])
                V3=float(L[1])
                expectedEncodedValues.append(V2)
                expectedQuantizedValues.append(V3)
                line = f.readline()
            else:
                break
    if( (len(Your_EncodedValues)!=len(expectedEncodedValues)) or (len(Your_QuantizedValues)!=len(expectedQuantizedValues))):
        print("QuantizationTest1 Test case failed, your signal have different length from the expected one")
        return
    for i in range(len(Your_EncodedValues)):
        if(Your_EncodedValues[i]!=expectedEncodedValues[i]):
            print("QuantizationTest1 Test case failed, your EncodedValues have different EncodedValues from the expected one")
            return
    for i in range(len(expectedQuantizedValues)):
        if abs(Your_QuantizedValues[i] - expectedQuantizedValues[i]) < 0.01:
            continue
        else:
            print("QuantizationTest1 Test case failed, your QuantizedValues have different values from the expected one")
            return
    print("QuantizationTest1 Test case passed successfully")
def read_signal_data_3(file_path):
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
def quantize_signal_3(data, levels=None, num_bits=None): 
    if levels is None and num_bits is None:
        print("Please provide either levels or num_bits.")
        return None, None, None

    if levels is None:
        levels = 2 ** num_bits

    max_amplitude = max(sample[1] for sample in data)
    min_amplitude = min(sample[1] for sample in data)

    amplitude_range = max_amplitude - min_amplitude
    quantization_step = amplitude_range / levels

    quantized_signal = [
        (sample[0], min_amplitude + quantization_step * round((sample[1] - min_amplitude) / quantization_step)) for
        sample in data]
    quantization_error = [(sample[0], sample[1] - quantized_sample[1]) for sample, quantized_sample in
                          zip(data, quantized_signal)]

    return quantized_signal, quantization_error, levels
def quantize_button_3():
    file_path = selected_file_label["text"]
    data = read_signal_data_3(file_path)
    if data is not None:
        quantization_type = quantization_type_var.get()

        if quantization_type == 'levels':
            levels = int(levels_entry.get())
            num_bits = None
        elif quantization_type == 'num_bits':
            num_bits = int(num_bits_entry.get())
            levels = None
        else:
            print("Invalid quantization type.")
            return

        quantized_signal, quantization_error, levels = quantize_signal_3(data, levels, num_bits)

        if quantized_signal is not None and quantization_error is not None:
            plt.figure(figsize=(12, 5))

            # Plot encoded signal
            plt.subplot(1, 3, 1)
            index = [sample[0] for sample in data]
            amplitude = [sample[1] for sample in data]
            plt.plot(index, amplitude, label="Encoded Signal", marker='o')
            plt.xlabel("Sample Index")
            plt.ylabel("Amplitude")
            plt.title("Encoded Signal")
            plt.legend()

            plt.subplot(1, 3, 2)
            # Plot quantized signal
            index = [sample[0] for sample in quantized_signal]
            amplitude = [sample[1] for sample in quantized_signal]
            plt.plot(index, amplitude, label="Quantized Signal", marker='o')
            plt.xlabel("Sample Index")
            plt.ylabel("Amplitude")
            plt.title("Quantized Signal")
            plt.legend()

            plt.subplot(1, 3, 3)
            # Plot quantization error
            index = [sample[0] for sample in quantization_error]
            amplitude = [sample[1] for sample in quantization_error]
            plt.plot(index, amplitude, label="Quantization Error", marker='o')
            plt.xlabel("Sample Index")
            plt.ylabel("Amplitude")
            plt.title("Quantization Error")
            plt.legend()

            plt.tight_layout()
            plt.show()
            # Return the encoded and quantized signals
            encoded_values = [sample[1] for sample in data]
            quantized_values = [sample[1] for sample in quantized_signal]

            # Display encoded and quantized values
            encoded_label["text"] = "Encoded Values: " + str(encoded_values)
            quantized_label["text"] = "Quantized Values: " + str(quantized_values)

            levels_label["text"] = "Levels: " + str(levels)
def Task3():
    # Create the main window
    root = tk.Tk()
    root.geometry("800x500")
    root.title("Signal Quantization")

    # Create and configure widgets
    header_label = ttk.Label(root, text="Signal Quantization", font=("Arial", 20))
    header_label.pack(pady=20)

    upload_button = ttk.Button(root, text="Browse Signal File", command=browse_file_3)
    upload_button.pack()

    selected_file_label = ttk.Label(root)
    selected_file_label.pack(pady=10)

    quantization_type_label = ttk.Label(root, text="Select Quantization Type:")
    quantization_type_label.pack()

    quantization_type_var = tk.StringVar()
    quantization_type_var.set("levels")
    quantization_radiobutton_levels = ttk.Radiobutton(root, text="Levels", variable=quantization_type_var, value="levels")
    quantization_radiobutton_num_bits = ttk.Radiobutton(root, text="Number of Bits", variable=quantization_type_var,
                                                        value="num_bits")
    quantization_radiobutton_levels.pack()
    quantization_radiobutton_num_bits.pack()

    levels_label = ttk.Label(root, text="Levels:")
    levels_label.pack()

    levels_entry = ttk.Entry(root)
    levels_entry.pack()

    num_bits_label = ttk.Label(root, text="Number of Bits:")
    num_bits_label.pack()

    num_bits_entry = ttk.Entry(root)
    num_bits_entry.pack()

    quantize_button = ttk.Button(root, text="Quantize Signal", command=quantize_button_3)
    quantize_button.pack()
    # Labels to display encoded and quantized values
    encoded_label = ttk.Label(root, text="Encoded Values:")
    encoded_label.pack()
    quantized_label = ttk.Label(root, text="Quantized Values:")
    quantized_label.pack()


    # Run the GUI main loop
    root.mainloop()
#*******************************************************************

#***************************** TASK 4 ******************************
#*******************************************************************

#***************************** TASK 5 ******************************
def Task5():
    def SignalSamplesAreEqual(file_name,samples):
        """
        this function takes two inputs the file that has the expected results and your results.
        file_name : this parameter corresponds to the file path that has the expected output
        samples: this parameter corresponds to your results
        return: this function returns Test case passed successfully if your results is similar to the expected output.
        """
        expected_indices=[]
        expected_samples=[]
        with open(file_name, 'r') as f:
            line = f.readline()
            line = f.readline()
            line = f.readline()
            line = f.readline()
            while line:
                # process line
                L=line.strip()
                if len(L.split(' '))==2:
                    L=line.split(' ')
                    V1=int(L[0])
                    V2=float(L[1])
                    expected_indices.append(V1)
                    expected_samples.append(V2)
                    line = f.readline()
                else:
                    break
                    
        if len(expected_samples)!=len(samples):
            print("Test case failed, your signal have different length from the expected one")
            return
        for i in range(len(expected_samples)):
            if abs(samples[i] - expected_samples[i]) < 0.01:
                continue
            else:
                print("Test case failed, your signal have different values from the expected one") 
                return
        print("Test case passed successfully")


    class DCTApp:
        def __init__(self, root):
            self.root = root
            self.root.title("DCT Calculator")

            self.create_widgets()

        def create_widgets(self):
            self.label = tk.Label(self.root, text="Upload a text file:")
            self.label.pack()

            self.upload_button = tk.Button(self.root, text="Upload File", command=self.upload_file)
            self.upload_button.pack()

            self.compute_button = tk.Button(self.root, text="Compute DCT", command=self.compute_dct)
            self.compute_button.pack()

            self.save_button = tk.Button(self.root, text="Save Coefficients", command=self.save_coefficients)
            self.save_button.pack()

            self.remove_button = tk.Button(self.root, text="Remove DCT", command=self.remove_dct)
            self.remove_button.pack()

            self.result_label = tk.Label(self.root, text="")
            self.result_label.pack()

            self.file_content = ""

        def upload_file(self):
            file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
            if file_path:
                with open(file_path, 'r') as file:
                    self.file_content = file.read()
                self.result_label.config(text="File uploaded successfully.")

        def compute_dct(self):
            if not self.file_content:
                self.result_label.config(text="Please upload a file first.")
                return

            input_data = self.file_content.split('\n')[3:]
            input_data = [line.split() for line in input_data if line.strip()]
            indices, values = zip(*[(int(index), float(value)) for index, value in input_data])
            # Define the signal samples
            # Signal samples



            signal_samples = np.array(values)

            N = len(signal_samples)
            dct_coefficients = np.zeros(N)

            for k in range(N):
                for n in range(N):
                    cos_term = np.cos((np.pi / (4 * N)) * (2 * n - 1) * (2 * k - 1))
                    dct_coefficients[k] += signal_samples[n] * cos_term
            dct_coefficients *= np.sqrt(2 / N)  # Normalize the entire vector


            # print("DCT Coefficients:", dct_coefficients)
            
            ###############################################################################
            #         # Load expected coefficients from the file
            #         expected_file_name = "D:\\Studying\\Level 4 sem 1\\Digital Signal Processing\\Labs\\Lab 5\\Task files\\DCT\\DCT_output.txt"
            #         with open(expected_file_name, 'r') as f:
            #             expected_data = [line.split() for line in f.read().split('\n') if line.strip()]

            #         expected_values = [float(value) for _, value in expected_data[3:]]  # Skip the first 3 lines

            #         expected_result = np.array(expected_values)

            #         print("Expected DCT Coefficients:", expected_result)
            # #################################################################################
                    # Test the result using the provided function
            expected_file_name = "D:\\Studying\\Level 4 sem 1\\Digital Signal Processing\\Labs\\Lab 5\\Task files\\DCT\\DCT_output.txt"

            SignalSamplesAreEqual(expected_file_name, dct_coefficients)

            self.display_result(dct_coefficients)


        def remove_dct(self):
            file_name = "D:\\Studying\\Level 4 sem 1\\Digital Signal Processing\\Labs\Lab 5\\Task files\Remove DC component\\DC_component_input.txt"
            with open(file_name, 'r') as f:
                data = [line.split() for line in f.read().split('\n') if line.strip()]

            values = [float(value) for _, value in data[3:]]  # Skip the first 3 lines
            Data = np.array(values)
            sum = 0
            for element in Data:
                sum += element
            average = sum / len(Data)
            result= []
            for element in Data:
                result.append(round((element-average),3))
            # print("Original: ",Data)
            # print("Result: ",result)# CORRECT BUT you need to take just first 3 decimal numbers to get ACCEPTED
            plt.subplot(1, 2, 1)
            plt.plot(Data, marker='o')
            plt.xlabel("Sample Index")
            plt.ylabel("Amplitude")
            plt.title("Original")

            plt.subplot(1, 2, 2)
            plt.plot(result,marker='o')
            plt.xlabel("Sample Index")
            plt.ylabel("Amplitude")
            plt.title("After Removing")

            plt.tight_layout()
            plt.show()
            # Test the result using the provided function
            SignalSamplesAreEqual("D:\Studying\Level 4 sem 1\Digital Signal Processing\Labs\Lab 5\Task files\Remove DC component\DC_component_output.txt", result)
            # plt.plot(result,marker = 'o')
            # plt.title("After removing DCT component")
            # plt.xlabel("x")
            # plt.ylabel("y")
            # plt.show()


        def display_result(self, result):
            plt.plot(result, marker='o')
            plt.title("DCT Result")
            plt.xlabel("Coefficient Index")
            plt.ylabel("Coefficient Value")
            plt.show()

        def save_coefficients(self):
            if not self.file_content:
                self.result_label.config(text="Please upload a file first.")
                return

            input_data = self.file_content.split('\n')[3:]
            input_data = [line.split() for line in input_data if line.strip()]

            values = zip(*[(int(index), float(value)) for index, value in input_data])
            signal = np.array(values)

            dct_result = dct(signal, norm='ortho')

            m = int(input("Enter the number of coefficients to save: "))
            selected_coefficients = dct_result[:m]

            filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
            if filename:
                with open(filename, 'w') as file:
                    for index, coefficient in enumerate(selected_coefficients):
                        file.write(f"Coefficient {index}: {coefficient}\n")

    if __name__ == "__main__":
        root = tk.Tk()
        app = DCTApp(root)
        root.mainloop()

#*******************************************************************

#***************************** Packege ******************************

# Create the main application window
root = tk.Tk()
root.title("Task Switcher")

# Create a variable to hold the currently selected task
current_task = tk.StringVar(value="Task 1")


# Create radio buttons for task selection
task_radio1 = tk.Radiobutton(root, text="Task 1", variable=current_task, value="Task 1", command=Task1)
task_radio2 = tk.Radiobutton(root, text="Task 2", variable=current_task, value="Task 2", command=Task2)
task_radio3 = tk.Radiobutton(root, text="Task 3", variable=current_task, value="Task 3", command=Task3)
task_radio4 = tk.Radiobutton(root, text="Task 4", variable=current_task, value="Task 4", command=Task3)
task_radio4 = tk.Radiobutton(root, text="Task 5", variable=current_task, value="Task 5", command=Task5)

# Create a label to display the selected task
task_label = tk.Label(root, text="Select a task:")

# Place the radio buttons and label in the window
task_radio1.pack()
task_radio2.pack()
task_radio3.pack()
task_radio4.pack()
task_label.pack()

# Start the main event loop
root.mainloop()