'''
In summary, CCA helps in understanding the extent to which two multidimensional
datasets are related to each other by finding the linear combinations of the
variables in each set that are maximally correlated.
This can be particularly useful in analyzing synchronization in movement data_pool_6,
as it quantifies the degree of similarity in the patterns of the two datasets.
'''

import json
import numpy as np
from sklearn.cross_decomposition import CCA
from sklearn.preprocessing import StandardScaler


# Load JSON data_pool_6
def load_json(file_path):
    with open(file_path, 'r') as file:
        data = [json.loads(line) for line in file]
    return data


# Extract bone vectors for each finger
def extract_finger_vectors(data):
    finger_vectors = []
    for frame in data:
        frame_vectors = []
        for finger in frame['fingers']:
            finger_bones = []
            for bone in finger['Bones']:
                next_joint = bone['NextJoint']
                prev_joint = bone['PrevJoint']
                # Vector between NextJoint and PrevJoint
                vector = [next_joint['x'] - prev_joint['x'], next_joint['y'] - prev_joint['y'],
                          next_joint['z'] - prev_joint['z']]
                finger_bones.append(vector)
            frame_vectors.append(np.mean(finger_bones, axis=0))  # Average vector for each finger
        finger_vectors.append(frame_vectors)  # All fingers for the frame
    return np.array(finger_vectors)


# Create vectors from PalmPosition to TipPosition
def extract_palm_to_tip_vectors(data):
    vectors = []
    for frame in data:
        palm_position = frame['PalmPosition']
        frame_vectors = []
        for finger in frame['fingers']:
            tip_position = finger['TipPosition']
            vector = [tip_position['x'] - palm_position['x'], tip_position['y'] - palm_position['y'],
                      tip_position['z'] - palm_position['z']]
            frame_vectors.append(vector)  # Vector from PalmPosition to each TipPosition
        vectors.append(frame_vectors)
    return np.array(vectors)


# Apply mirror transformation (flip x-axis)
def apply_mirror_transformation(data):
    mirrored_data = data.copy()
    mirrored_data[:, :, 0] = -mirrored_data[:, :, 0]  # Flip the x-axis for all vectors
    return mirrored_data


# Truncate datasets to the shortest length
def truncate_to_shortest(data1, data2):
    min_len = min(len(data1), len(data2))
    return data1[:min_len], data2[:min_len]


# Perform CCA on the corresponding fingers and vectors
def compare_fingers_with_cca(finger_vectors1, finger_vectors2):
    cca = CCA(n_components=1)
    correlations = []
    for i in range(5):  # Compare each of the 5 fingers
        # Extract finger data_pool_6 for both hands
        finger1 = finger_vectors1[:, i, :]
        finger2 = finger_vectors2[:, i, :]

        # Perform CCA
        scaler1 = StandardScaler()
        scaler2 = StandardScaler()
        finger1_scaled = scaler1.fit_transform(finger1)
        finger2_scaled = scaler2.fit_transform(finger2)

        X_c, Y_c = cca.fit_transform(finger1_scaled, finger2_scaled)
        correlation = np.corrcoef(X_c.T, Y_c.T)[0, 1]
        correlations.append(correlation)
        print(f"Finger {i + 1} CCA correlation:", correlation)
    return correlations


# Perform CCA on Palm-to-Tip vectors
def compare_palm_to_tip_vectors(vectors1, vectors2):
    cca = CCA(n_components=1)
    correlations = []
    for i in range(5):  # Compare each of the 5 Palm-to-Tip vectors (one per finger)
        # Extract vectors for both hands
        vector1 = vectors1[:, i, :]
        vector2 = vectors2[:, i, :]

        # Perform CCA
        scaler1 = StandardScaler()
        scaler2 = StandardScaler()
        vector1_scaled = scaler1.fit_transform(vector1)
        vector2_scaled = scaler2.fit_transform(vector2)

        X_c, Y_c = cca.fit_transform(vector1_scaled, vector2_scaled)
        correlation = np.corrcoef(X_c.T, Y_c.T)[0, 1]
        correlations.append(correlation)
        print(f"Palm-to-Tip Finger {i + 1} CCA correlation:", correlation)
    return correlations


# # Load data_pool_6 for both hands
# data1 = load_json('data_pool_7/sync_right_hand_data.json')
# data2 = load_json('data_pool_7/sync_left_hand_data.json')
#
# # Extract finger bone vectors for both hands
# finger_vectors1 = extract_finger_vectors(data1)
# finger_vectors2 = extract_finger_vectors(data2)
#
# # Truncate both finger vector datasets to the shortest length
# finger_vectors1, finger_vectors2 = truncate_to_shortest(finger_vectors1, finger_vectors2)
#
# # Apply mirror transformation to the left hand's data_pool_6
# finger_vectors2_mirrored = apply_mirror_transformation(finger_vectors2)
#
# # Compare fingers using CCA
# compare_fingers_with_cca(finger_vectors1, finger_vectors2_mirrored)
#
# # Extract Palm-to-Tip vectors for both hands
# palm_to_tip_vectors1 = extract_palm_to_tip_vectors(data1)
# palm_to_tip_vectors2 = extract_palm_to_tip_vectors(data2)
#
# # Truncate both Palm-to-Tip vector datasets to the shortest length
# palm_to_tip_vectors1, palm_to_tip_vectors2 = truncate_to_shortest(palm_to_tip_vectors1, palm_to_tip_vectors2)
#
# # Apply mirror transformation to Palm-to-Tip vectors
# palm_to_tip_vectors2_mirrored = apply_mirror_transformation(palm_to_tip_vectors2)
#
# # Compare Palm-to-Tip vectors using CCA
# compare_palm_to_tip_vectors(palm_to_tip_vectors1, palm_to_tip_vectors2_mirrored)
