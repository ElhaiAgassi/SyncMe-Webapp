'''
Dynamic Time Warping (DTW) is an algorithm for measuring the similarity between two temporal sequences that may vary in speed.
The main idea is to align the sequences in a way that minimizes the total distance between them.
This can handle sequences of different lengths and can align sequences even if they are out of phase.

'''
import json
import numpy as np
from scipy.spatial.distance import euclidean
from fastdtw import fastdtw


# Load JSON data
def load_json(file_path):
    with open(file_path, 'r') as file:
        data = [json.loads(line) for line in file]
    return data


# Extract palm positions
def extract_palm_positions(data):
    positions = []
    for frame in data:
        palm_position = frame['PalmPosition']
        positions.append([abs(palm_position['x']), abs(palm_position['y']), abs(palm_position['z'])])
    return np.array(positions)


# Extract palm velocities
def extract_palm_velocities(data):
    velocities = []
    for frame in data:
        palm_velocity = frame['PalmVelocity']
        velocities.append([abs(palm_velocity['x']), abs(palm_velocity['y']), abs(palm_velocity['z'])])
    return np.array(velocities)


# Extract tip positions
def extract_tip_positions(data):
    positions = []
    for frame in data:
        frame_positions = []
        for finger in frame['fingers']:
            tip_position = finger['TipPosition']
            frame_positions.append([abs(tip_position['x']), abs(tip_position['y']), abs(tip_position['z'])])
        positions.append(np.mean(frame_positions, axis=0))
    return np.array(positions)


# Extract wrist positions
def extract_wrist_positions(data):
    positions = []
    for frame in data:
        wrist_position = frame['WristPosition']
        positions.append([abs(wrist_position['x']), abs(wrist_position['y']), abs(wrist_position['z'])])
    return np.array(positions)


# **New function: Extract and compare bone positions for each finger individually**
def extract_finger_bone_positions(data, finger_index):
    bone_positions = []
    for frame in data:
        finger_bone_positions = []
        finger = frame['fingers'][finger_index]  # Extract the specific finger
        for bone in finger['Bones']:
            bone_prev_joint = bone['PrevJoint']
            bone_next_joint = bone['NextJoint']
            # We compare both the previous joint and the next joint to get a full comparison of the bone
            finger_bone_positions.append(
                [abs(bone_prev_joint['x']), abs(bone_prev_joint['y']), abs(bone_prev_joint['z'])])
            finger_bone_positions.append(
                [abs(bone_next_joint['x']), abs(bone_next_joint['y']), abs(bone_next_joint['z'])])
        bone_positions.append(np.mean(finger_bone_positions, axis=0))  # Average out all bone joint positions
    return np.array(bone_positions)


# Function to perform DTW with manual control over the window size and margin of error
def controlled_dtw(data1, data2, file1, file2, margin=0, window_size=5):
    n = min(len(data1), len(data2))  # Use the length of the shortest sequence
    total_distance = 0

    for i in range(n):
        min_distance = float('inf')

        # Compare the current frame from data1 with a range of frames from data2
        for j in range(max(0, i - window_size), min(n, i + 1)):
            distance, _ = fastdtw(data1[i:i + 1], data2[j:j + 1], dist=euclidean)

            if distance < min_distance:
                min_distance = distance

        # Apply margin of error
        adjusted_distance = max(0, min_distance - margin)
        total_distance += distance

    # Normalize the total distance by the number of frames
    normalized_distance = total_distance / n
    return normalized_distance, total_distance