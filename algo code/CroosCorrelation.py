'''
Cross-correlation is a measure of similarity between two signals as a function of the time-lag applied to one of them.
It essentially checks how well two signals match when one is shifted relative to the other.


Suppose you have two signals (or sequences of data points), a and b. These could be time series data representing hand movements in your case.
The cross-correlation function shifts one signal in time (or space) relative to the other signal and computes the similarity at each shift.


out put explanation:

Interpretation:
Maximum Correlation at Lag 0: This means the highest similarity occurs when the signals are aligned without any time shift.
This is a strong indicator that the movements are synchronized in time.

Value of Maximum Correlation (2.464): The magnitude of the correlation value itself is context-dependent,
but a relatively high value suggests strong synchronization.
Since your data is typically normalized, a value greater than 2 suggests good synchronization,
as values near or below 1 would indicate weaker correlation.

If the maximum correlation values are close to 1 and the lags are 0 or very small, the hands are likely synchronized.

Question: why did we need here to use abs on the data !!!!! ??????
'''

# import json
# import numpy as np
# from scipy.signal import correlate
#
#
# # Function to load JSON data
# def load_json(file_path):
#     with open(file_path, 'r') as file:
#         data = [json.loads(line) for line in file]
#     return data
#
#
# # Function to extract palm positions
# def extract_palm_positions(data):
#     positions = []
#     for frame in data:
#         palm_position = frame['PalmPosition']
#         positions.append([palm_position['x'], palm_position['y'], palm_position['z']])
#     return np.array(positions)
#
#
# # Function to extract palm velocities
# def extract_palm_velocities(data):
#     velocities = []
#     for frame in data:
#         palm_velocity = frame['PalmVelocity']
#         velocities.append([palm_velocity['x'], palm_velocity['y'], palm_velocity['z']])
#     return np.array(velocities)
#
#
# # Function to extract tip positions
# def extract_tip_positions(data):
#     positions = []
#     for frame in data:
#         frame_positions = []
#         for finger in frame['fingers']:
#             tip_position = finger['TipPosition']
#             frame_positions.append([tip_position['x'], tip_position['y'], tip_position['z']])
#         positions.append(np.mean(frame_positions, axis=0))
#     return np.array(positions)
#
#
# # Function to calculate cross-correlation
# def cross_correlation(a, b):
#     correlation = correlate(a[:, 0], b[:, 0])  # Using x-coordinate for simplicity
#     return correlation
#
#
# # Main function to perform cross-correlation
# def main():
#     # Load the data
#     data1 = load_json('data_pool_2/data4.json')
#     data2 = load_json('data_pool_2/mirrored_data4.json')
#     # data2 = load_json('data_pool_2/suffle.json')
#
#     # Extract features (choose one)
#     feature_extraction_function = extract_palm_positions  # Change this to the desired feature extraction function
#     positions1 = feature_extraction_function(data1)
#     positions2 = feature_extraction_function(data2)
#
#     # Compute cross-correlation
#     correlation = cross_correlation(positions1, positions2)
#     print("Cross-Correlation:", correlation)
#
#
# if __name__ == "__main__":
#     main()






# import json
# import numpy as np
# from scipy.signal import correlate
#
#
# # Function to load JSON data
# def load_json(file_path):
#     with open(file_path, 'r') as file:
#         data = [json.loads(line) for line in file]
#     return data
#
#
# # Function to extract palm positions
# def extract_palm_positions(data):
#     positions = []
#     for frame in data:
#         palm_position = frame['PalmPosition']
#         positions.append([abs(palm_position['x']), abs(palm_position['y']), abs(palm_position['z'])])
#     return np.array(positions)
#
#
# # Function to extract palm velocities
# def extract_palm_velocities(data):
#     velocities = []
#     for frame in data:
#         palm_velocity = frame['PalmVelocity']
#         velocities.append([palm_velocity['x'], palm_velocity['y'], palm_velocity['z']])
#     return np.array(velocities)
#
#
# # Function to extract tip positions
# def extract_tip_positions(data):
#     positions = []
#     for frame in data:
#         frame_positions = []
#         for finger in frame['fingers']:
#             tip_position = finger['TipPosition']
#             frame_positions.append([tip_position['x'], tip_position['y'], tip_position['z']])
#         positions.append(np.mean(frame_positions, axis=0))
#     return np.array(positions)
#
#
# # Function to calculate cross-correlation
# def cross_correlation(a, b):
#     correlation = correlate(a[:, 0], b[:, 0])  # Using x-coordinate for simplicity
#     lags = np.arange(-len(a) + 1, len(a))
#     return correlation, lags
#
#
# # Main function to perform cross-correlation
# def main():
#     # Load the data
#     data1 = load_json('data_pool_2/data4.json')
#     data2 = load_json('data_pool_2/suffle.json')
#
#     # Extract features (choose one)
#     feature_extraction_function = extract_palm_positions  # Change this to the desired feature extraction function
#     positions1 = feature_extraction_function(data1)
#     positions2 = feature_extraction_function(data2)
#
#     # Compute cross-correlation
#     correlation, lags = cross_correlation(positions1, positions2)
#     max_corr = np.max(correlation)
#     max_lag = lags[np.argmax(correlation)]
#
#     print("Cross-Correlation:", correlation)
#     print(f"Maximum Correlation: {max_corr} at Lag: {max_lag}")
#
#
# if __name__ == "__main__":
#     main()


import json
import numpy as np
from scipy.signal import correlate

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
        positions.append([abs(palm_position['x']), abs(palm_position['y']), abs(palm_position['z'])])
    return np.array(positions)

# Function to extract palm velocities
def extract_palm_velocities(data):
    velocities = []
    for frame in data:
        palm_velocity = frame['PalmVelocity']
        velocities.append([abs(palm_velocity['x']), abs(palm_velocity['y']), abs(palm_velocity['z'])])
    return np.array(velocities)

# Function to extract tip positions
def extract_tip_positions(data):
    positions = []
    for frame in data:
        frame_positions = []
        for finger in frame['fingers']:
            tip_position = finger['TipPosition']
            frame_positions.append([abs(tip_position['x']), abs(tip_position['y']), abs(tip_position['z'])])
        positions.append(np.mean(frame_positions, axis=0))
    return np.array(positions)

# Function to compute normalized cross-correlation
def cross_correlation_normalized(a, b):
    a = (a - np.mean(a)) / (np.std(a) * len(a))
    b = (b - np.mean(b)) / np.std(b)
    return correlate(a, b)

# Load the data
data1 = load_json('data_pool_2/data4.json')
# data2 = load_json('data_pool_2/mirrored_data4.json')
data2 = load_json('data_pool_2/suffle.json')

# Extract palm positions
positions1 = extract_palm_positions(data1)
positions2 = extract_palm_positions(data2)

# Compute the normalized cross-correlation
correlation_normalized = cross_correlation_normalized(positions1[:, 0], positions2[:, 0])
max_corr = np.max(correlation_normalized)
lag = np.argmax(correlation_normalized) - (len(positions1) - 1)
print("Maximum Correlation (Normalized):", max_corr)
print("Lag at Maximum Correlation (Normalized):", lag)

# Extract palm velocities
velocities1 = extract_palm_velocities(data1)
velocities2 = extract_palm_velocities(data2)

# Compute the normalized cross-correlation for velocities
correlation_velocity_normalized = cross_correlation_normalized(velocities1[:, 0], velocities2[:, 0])
max_corr_velocity = np.max(correlation_velocity_normalized)
lag_velocity = np.argmax(correlation_velocity_normalized) - (len(velocities1) - 1)
print("Maximum Velocity Correlation (Normalized):", max_corr_velocity)
print("Lag at Maximum Velocity Correlation (Normalized):", lag_velocity)

# Extract tip positions
tip_positions1 = extract_tip_positions(data1)
tip_positions2 = extract_tip_positions(data2)

# Compute the normalized cross-correlation for tip positions
correlation_tip_normalized = cross_correlation_normalized(tip_positions1[:, 0], tip_positions2[:, 0])
max_corr_tip = np.max(correlation_tip_normalized)
lag_tip = np.argmax(correlation_tip_normalized) - (len(tip_positions1) - 1)
print("Maximum Tip Position Correlation (Normalized):", max_corr_tip)
print("Lag at Maximum Tip Position Correlation (Normalized):", lag_tip)
