'''
Cross-correlation is a measure of similarity between two signals as a function of the time-lag applied to one of them.
It essentially checks how well two signals match when one is shifted relative to the other.


Suppose you have two signals (or sequences of data_pool_6 points), a and b. These could be time series data_pool_6 representing hand movements in your case.
The cross-correlation function shifts one signal in time (or space) relative to the other signal and computes the similarity at each shift.


out put explanation:

Interpretation:
Maximum Correlation at Lag 0: This means the highest similarity occurs when the signals are aligned without any time shift.
This is a strong indicator that the movements are synchronized in time.

Value of Maximum Correlation (2.464): The magnitude of the correlation value itself is context-dependent,
but a relatively high value suggests strong synchronization.
Since your data_pool_6 is typically normalized, a value greater than 2 suggests good synchronization,
as values near or below 1 would indicate weaker correlation.

If the maximum correlation values are close to 1 and the lags are 0 or very small, the hands are likely synchronized.

Question: why did we need here to use abs on the data_pool_6 !!!!! ??????
'''

"""
there is no need to chang this code as the cross Correlation already dose the shifts this is what the lag is !
this works on folder 3 we still need to update the code to worck with 5 
"""

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
def extract_tip_positions(data):
    positions = []
    for frame in data:
        frame_positions = []
        for finger in frame['fingers']:
            tip_position = finger['TipPosition']
            frame_positions.append([tip_position['x'], tip_position['y'], tip_position['z']])
        positions.append(np.mean(frame_positions, axis=0))
    return np.array(positions)


# **New function to extract wrist positions**
def extract_wrist_positions(data):
    positions = []
    for frame in data:
        wrist_position = frame['WristPosition']
        positions.append([wrist_position['x'], wrist_position['y'], wrist_position['z']])
    return np.array(positions)


# **New function to extract bone positions for each finger individually**
def extract_finger_bone_positions(data, finger_index):
    bone_positions = []
    for frame in data:
        finger_bone_positions = []
        finger = frame['fingers'][finger_index]  # Extract the specific finger
        for bone in finger['Bones']:
            bone_prev_joint = bone['PrevJoint']
            bone_next_joint = bone['NextJoint']
            finger_bone_positions.append([bone_prev_joint['x'], bone_prev_joint['y'], bone_prev_joint['z']])
            finger_bone_positions.append([bone_next_joint['x'], bone_next_joint['y'], bone_next_joint['z']])
        bone_positions.append(
            np.mean(finger_bone_positions, axis=0))  # Average all bone joint positions for each finger
    return np.array(bone_positions)


# Function to compute normalized cross-correlation
def cross_correlation_normalized(a, b):
    a = (a - np.mean(a)) / (np.std(a) * len(a))
    b = (b - np.mean(b)) / np.std(b)
    return correlate(a, b)


# Function to compute correlation without lag
def correlation_without_lag(a, b):
    min_len = min(len(a), len(b))
    a = a[:min_len]
    b = b[:min_len]
    a = (a - np.mean(a)) / np.std(a)
    b = (b - np.mean(b)) / np.std(b)
    return np.dot(a, b) / len(a)


# # Load the data
# data1 = load_json('data_pool_3/sync_right_hand_data.json')
# data2 = load_json('data_pool_3/sync_left_hand_data.json')
#
# # Flip data for mirrored hand comparison
# positions2 = np.flip(extract_palm_positions(data2), axis=1)
#
# # Extract palm positions and perform cross-correlation
# positions1 = extract_palm_positions(data1)
# correlation_normalized = cross_correlation_normalized(positions1[:, 0], positions2[:, 0])
# max_corr = np.max(correlation_normalized)
# lag = np.argmax(correlation_normalized) - (len(positions1) - 1)
# corr_without_lag_positions = correlation_without_lag(positions1[:, 0], positions2[:, 0])
#
# print("Maximum Correlation (Normalized) with Lag (Palm Positions):", max_corr)
# print("Lag at Maximum Correlation:", lag)
# print("Correlation Without Lag (Palm Positions):", corr_without_lag_positions)
# print()
#
# # Extract palm velocities and perform cross-correlation
# velocities1 = extract_palm_velocities(data1)
# velocities2 = np.flip(extract_palm_velocities(data2), axis=1)
# correlation_velocity_normalized = cross_correlation_normalized(velocities1[:, 0], velocities2[:, 0])
# max_corr_velocity = np.max(correlation_velocity_normalized)
# lag_velocity = np.argmax(correlation_velocity_normalized) - (len(velocities1) - 1)
# corr_without_lag_velocities = correlation_without_lag(velocities1[:, 0], velocities2[:, 0])
#
# print("Maximum Correlation (Normalized) with Lag (Velocities):", max_corr_velocity)
# print("Lag at Maximum Correlation:", lag_velocity)
# print("Correlation Without Lag (Velocities):", corr_without_lag_velocities)
# print()
#
# # Extract tip positions and perform cross-correlation
# tip_positions1 = extract_tip_positions(data1)
# tip_positions2 = np.flip(extract_tip_positions(data2), axis=1)
# correlation_tip_normalized = cross_correlation_normalized(tip_positions1[:, 0], tip_positions2[:, 0])
# max_corr_tip = np.max(correlation_tip_normalized)
# lag_tip = np.argmax(correlation_tip_normalized) - (len(tip_positions1) - 1)
# corr_without_lag_tips = correlation_without_lag(tip_positions1[:, 0], tip_positions2[:, 0])
#
# print("Maximum Correlation (Normalized) with Lag (Tip Positions):", max_corr_tip)
# print("Lag at Maximum Correlation:", lag_tip)
# print("Correlation Without Lag (Tip Positions):", corr_without_lag_tips)
# print()
#
# # **Extract wrist positions and perform cross-correlation**
# wrist_positions1 = extract_wrist_positions(data1)
# wrist_positions2 = np.flip(extract_wrist_positions(data2), axis=1)
# correlation_wrist_normalized = cross_correlation_normalized(wrist_positions1[:, 0], wrist_positions2[:, 0])
# max_corr_wrist = np.max(correlation_wrist_normalized)
# lag_wrist = np.argmax(correlation_wrist_normalized) - (len(wrist_positions1) - 1)
# corr_without_lag_wrist = correlation_without_lag(wrist_positions1[:, 0], wrist_positions2[:, 0])
#
# print("Maximum Correlation (Normalized) with Lag (Wrist Positions):", max_corr_wrist)
# print("Lag at Maximum Correlation:", lag_wrist)
# print("Correlation Without Lag (Wrist Positions):", corr_without_lag_wrist)
# print()
#
# # **Extract and compare bone positions for each finger individually**
# for finger_index in range(5):  # Assuming there are 5 fingers
#     bone_positions1 = extract_finger_bone_positions(data1, finger_index)
#     bone_positions2 = np.flip(extract_finger_bone_positions(data2, finger_index), axis=1)
#
#     correlation_bone_normalized = cross_correlation_normalized(bone_positions1[:, 0], bone_positions2[:, 0])
#     max_corr_bone = np.max(correlation_bone_normalized)
#     lag_bone = np.argmax(correlation_bone_normalized) - (len(bone_positions1) - 1)
#     corr_without_lag_bone = correlation_without_lag(bone_positions1[:, 0], bone_positions2[:, 0])
#
#     print(f"Maximum Correlation (Normalized) with Lag (Finger {finger_index + 1} Bone Positions):", max_corr_bone)
#     print(f"Lag at Maximum Correlation (Finger {finger_index + 1}):", lag_bone)
#     print(f"Correlation Without Lag (Finger {finger_index + 1} Bone Positions):", corr_without_lag_bone)
#     print()
