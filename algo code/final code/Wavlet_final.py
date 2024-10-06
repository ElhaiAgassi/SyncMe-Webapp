import json
import numpy as np
import pywt
import matplotlib.pyplot as plt

# Function to load JSON data_pool_6
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
    return np.array(positions)

# Function to extract palm velocities
def extract_palm_velocities(data):
    velocities = []
    for frame in data:
        palm_velocity = frame['PalmVelocity']
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

# Function to calculate wavelet coherence
def wavelet_coherence(a, b):
    scales = np.arange(1, 128)
    cwt_a, _ = pywt.cwt(a, scales, 'cmor')
    cwt_b, _ = pywt.cwt(b, scales, 'cmor')
    coherence = np.abs(np.mean(cwt_a * np.conj(cwt_b), axis=0))
    return coherence

# # Load the data_pool_6
# data1 = load_json('data_pool_3/sync_right_hand_data.json')
# data2 = load_json('data_pool_3/sync_left_hand_data.json')
#
# # data1 = load_json('data_pool_3/unsync_right_hand_data.json')
# # data2 = load_json('data_pool_3/unsync_left_hand_data.json')
#
# # Ensure both datasets are of the same length
# min_len = min(len(data1), len(data2))
# data1 = data1[:min_len]
# data2 = data2[:min_len]
#
# # Extract positions
# positions1 = extract_palm_positions(data1)
# positions2 = extract_palm_positions(data2)
#
# # Extract velocities
# velocities1 = extract_palm_velocities(data1)
# velocities2 = extract_palm_velocities(data2)
#
# # Step 1: Flip the data_pool_6 for the second hand along the x-axis to account for mirroring
# positions2_flipped = np.copy(positions2)
# positions2_flipped[:, 0] = -positions2_flipped[:, 0]
#
# velocities2_flipped = np.copy(velocities2)
# velocities2_flipped[:, 0] = -velocities2_flipped[:, 0]
#
# # Step 2: Perform wavelet coherence analysis for each axis separately
#
# # Wavelet coherence for positions (X, Y, Z separately)
# for axis in range(3):
#     coherence_positions = wavelet_coherence(positions1[:, axis], positions2_flipped[:, axis])
#     plt.plot(coherence_positions)
#     plt.title(f"Wavelet Coherence (Position Axis {axis})")
#     plt.show()
#
# # Wavelet coherence for velocities (X, Y, Z separately)
# for axis in range(3):
#     coherence_velocities = wavelet_coherence(velocities1[:, axis], velocities2_flipped[:, axis])
#     plt.plot(coherence_velocities)
#     plt.title(f"Wavelet Coherence (Velocity Axis {axis})")
#     plt.show()

