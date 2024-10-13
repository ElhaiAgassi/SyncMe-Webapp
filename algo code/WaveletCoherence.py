'''
Wavelet coherence is a method to study the relationship between two time series in the time-frequency domain.
It uses wavelet transforms to decompose the signals into different frequency components,
and then calculates the coherence between these components.
This allows you to see how the relationship between the signals changes over time and across different frequencies.

the only algorithem that is not good for now
'''
import json
import numpy as np
import pywt
import matplotlib.pyplot as plt

# Function to load JSON data
def load_json(file_path):
    with open(file_path, 'r') as file:
        data = [json.loads(line) for line in file]
    return data

# Function to extract palm positions
def extract_palm_positions(data):
    positions = []
    for frame in data:
        palm_position = frame['PalmPosition']
        positions.append([palm_position['x'], palm_position['y'], palm_position['z']])
        # positions.append([abs(palm_position['x']), abs(palm_position['y']), abs(palm_position['z'])])
    return np.array(positions)

# Function to extract palm velocities
def extract_palm_velocities(data):
    velocities = []
    for frame in data:
        palm_velocity = frame['PalmVelocity']
        # velocities.append([abs(palm_velocity['x']), abs(palm_velocity['y']), abs(palm_velocity['z'])])
        velocities.append([palm_velocity['x'], palm_velocity['y'], palm_velocity['z']])
    return np.array(velocities)

# Function to extract tip positions
def extract_TipPosition(data):
    positions = []
    for frame in data:
        frame_positions = []
        for finger in frame['fingers']:
            tip_position = finger['TipPosition']
            frame_positions.append([tip_position['x'], tip_position['y'], tip_position['z']])
        positions.append(np.mean(frame_positions, axis=0))
    return np.array(positions)

# Load the data
data1 = load_json('data_pool_2/data4.json')
data2 = load_json('data_pool_2/mirrored_data4.json')
# data2 = load_json('data_pool_2/suffle.json')

# Extract positions
positions1 = extract_palm_positions(data1)
positions2 = extract_palm_positions(data2)

# Extract velocities
velocities1 = extract_palm_velocities(data1)
velocities2 = extract_palm_velocities(data2)

# Function to calculate wavelet coherence
def wavelet_coherence(a, b):
    scales = np.arange(1, 128)
    cwt_a, _ = pywt.cwt(a[:, 0], scales, 'morl')
    cwt_b, _ = pywt.cwt(b[:, 0], scales, 'morl')
    coherence = np.abs(np.mean(cwt_a * np.conj(cwt_b), axis=0))
    return coherence

# Calculate wavelet coherence for positions
coherence_positions = wavelet_coherence(positions1, positions2)
# print(coherence_positions)
plt.plot(coherence_positions)
plt.title("Wavelet Coherence (Positions)")
plt.show()

# Calculate wavelet coherence for velocities
coherence_velocities = wavelet_coherence(velocities1, velocities2)
# print(coherence_velocities)
plt.plot(coherence_velocities)
plt.title("Wavelet Coherence (Velocities)")
plt.show()
