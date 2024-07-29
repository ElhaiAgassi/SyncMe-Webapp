# import json
# import numpy as np
# from scipy.signal import correlate
# from dtaidistance import dtw
# import pywt
#
# # Load JSON data
# with open('data4.json.json') as f1, open('mirrored_data4.json.json') as f2:
#     data1 = json.load(f1)
#     data2 = json.load(f2)
#
# # Extract relevant data (e.g., PalmPosition)
# def extract_positions(data):
#     return np.array([frame['PalmPosition'] for frame in data])
#
# positions1 = extract_positions(data1)
# positions2 = extract_positions(data2)
#
# # Calculate DTW distance
# dtw_distance = dtw.distance(positions1[:, 0], positions2[:, 0])
# print(f'DTW distance: {dtw_distance}')
#
# # Calculate Cross-Correlation
# corr = correlate(positions1[:, 0], positions2[:, 0])  # Example using x-coordinate
# lag = np.argmax(corr) - (len(positions1) - 1)
# print(f'Max correlation at lag: {lag}')
#
# # Compute Wavelet Coherence
# coeffs1, freqs1 = pywt.cwt(positions1[:, 0], np.arange(1, 31), 'cmor')
# coeffs2, freqs2 = pywt.cwt(positions2[:, 0], np.arange(1, 31), 'cmor')
# wavelet_coherence = np.abs(np.sum(coeffs1 * np.conj(coeffs2), axis=0)) / np.sqrt(np.sum(np.abs(coeffs1)**2, axis=0) * np.sum(np.abs(coeffs2)**2, axis=0))
# print(f'Wavelet Coherence: {wavelet_coherence.mean()}')
#
# # Compute CCA
# from sklearn.cross_decomposition import CCA
# cca = CCA(n_components=1)
# cca.fit(positions1, positions2)
# positions1_c, positions2_c = cca.transform(positions1, positions2)
# print(f'Canonical Correlation: {np.corrcoef(positions1_c.T, positions2_c.T)[0, 1]}')
#
#
# ########### Example ML Workflow:
# # from sklearn.model_selection import train_test_split
# # from sklearn.ensemble import RandomForestClassifier
# # from sklearn.metrics import accuracy_score
# #
# # # Assuming features and labels are prepared
# # features = np.array([[dtw_distance, lag, wavelet_coherence.mean(), cca_score]])
# # labels = np.array([0, 1])  # Example labels for synchronized (1) and not synchronized (0)
# #
# # # Split data
# # X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)
# #
# # # Train model
# # model = RandomForestClassifier()
# # model.fit(X_train, y_train)
# #
# # # Evaluate model
# # y_pred = model.predict(X_test)
# # print(f'Accuracy: {accuracy_score(y_test, y_pred)}')


# import json
#
# def load_json(file_path):
#     with open(file_path, 'r') as file:
#         data = json.load(file)
#     return data
#
# # Load the data
# data1 = load_json('data4.json')
# data2 = load_json('mirrored_data4.json')
# import numpy as np
#
# def extract_positions(data):
#     positions = []
#     for frame in data:
#         frame_positions = []
#         for finger in frame['fingers']:
#             tip_position = finger['TipPosition']
#             frame_positions.append([tip_position['x'], tip_position['y'], tip_position['z']])
#         positions.append(np.mean(frame_positions, axis=0))
#     return np.array(positions)
#
# positions1 = extract_positions(data1)
# positions2 = extract_positions(data2)
#
#
# from scipy.spatial.distance import euclidean
# from fastdtw import fastdtw
#
# distance, path = fastdtw(positions1, positions2, dist=euclidean)
# print("DTW Distance:", distance)
#
#
# from scipy.signal import correlate
#
# def cross_correlation(a, b):
#     correlation = correlate(a[:, 0], b[:, 0])
#     return correlation
#
# correlation = cross_correlation(positions1, positions2)
# print("Cross-Correlation:", correlation)
#
#
# import pywt
# import matplotlib.pyplot as plt
#
# def wavelet_coherence(a, b):
#     scales = np.arange(1, 128)
#     cwt_a, _ = pywt.cwt(a[:, 0], scales, 'morl')
#     cwt_b, _ = pywt.cwt(b[:, 0], scales, 'morl')
#     coherence = np.abs(np.mean(cwt_a * np.conj(cwt_b), axis=0))
#     return coherence
#
# coherence = wavelet_coherence(positions1, positions2)
# plt.plot(coherence)
# plt.title("Wavelet Coherence")
# plt.show()
#
# from sklearn.cross_decomposition import CCA
#
# cca = CCA(n_components=1)
# cca.fit(positions1, positions2)
# X_c, Y_c = cca.transform(positions1, positions2)
# correlation = np.corrcoef(X_c.T, Y_c.T)[0, 1]
# print("CCA Correlation:", correlation)

import json
import numpy as np
from scipy.spatial.distance import euclidean
from fastdtw import fastdtw
from scipy.signal import correlate
import pywt
import matplotlib.pyplot as plt
from sklearn.cross_decomposition import CCA

# Function to load JSON lines
def load_json_lines(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            data.append(json.loads(line))
    return data

# Function to extract positions
def extract_positions(data):
    positions = []
    for frame in data:
        frame_positions = []
        for finger in frame['fingers']:
            tip_position = finger['TipPosition']
            frame_positions.append([tip_position['x'], tip_position['y'], tip_position['z']])
        positions.append(np.mean(frame_positions, axis=0))
    return np.array(positions)

# Function to mirror data
def mirror_data(data):
    return -data

# Load the data
data1 = load_json_lines('data_pool_2/data4.json')
data2 = load_json_lines('data_pool_2/mirrored_data4.json')
# data2 = load_json_lines('mirrored_data4_distroyed.json')
# data2 = load_json_lines('suffle.json')

# Extract positions
positions1 = extract_positions(data1)
positions2 = extract_positions(data2)

# Mirror the second dataset if it is not already mirrored
# positions2 = mirror_data(positions2)

# Dynamic Time Warping (DTW)
distance, path = fastdtw(positions1, positions2, dist=euclidean)
print("DTW Distance:", distance)

# Normalize DTW distance
normalized_distance = distance / len(positions1)
print("Normalized DTW Distance:", normalized_distance)

# Establishing Baseline Distances for Comparison
# Assuming sync_seq1, sync_seq2 are highly synchronized sequences
# and diff_seq1, diff_seq2 are very different sequences

sync_seq1, sync_seq2 = positions1, positions1  # Example for synchronized
diff_seq1, diff_seq2 = positions1, np.flip(positions1, axis=0)  # Example for very different

distance_sync, _ = fastdtw(sync_seq1, sync_seq2, dist=euclidean)
distance_diff, _ = fastdtw(diff_seq1, diff_seq2, dist=euclidean)

print("DTW Distance (Highly Synchronized):", distance_sync)
print("DTW Distance (Very Different):", distance_diff)

# Cross-Correlation
def cross_correlation(a, b):
    correlation = correlate(a[:, 0], b[:, 0])
    return correlation

correlation = cross_correlation(positions1, positions2)
print("Cross-Correlation:", correlation)

# Wavelet Coherence
def wavelet_coherence(a, b):
    scales = np.arange(1, 128)
    cwt_a, _ = pywt.cwt(a[:, 0], scales, 'morl')
    cwt_b, _ = pywt.cwt(b[:, 0], scales, 'morl')
    coherence = np.abs(np.mean(cwt_a * np.conj(cwt_b), axis=0))
    return coherence

coherence = wavelet_coherence(positions1, positions2)
plt.plot(coherence)
plt.title("Wavelet Coherence")
plt.show()

# Canonical Correlation Analysis (CCA)
cca = CCA(n_components=1)
cca.fit(positions1, positions2)
X_c, Y_c = cca.transform(positions1, positions2)
correlation = np.corrcoef(X_c.T, Y_c.T)[0, 1]
print("CCA Correlation:", correlation)
