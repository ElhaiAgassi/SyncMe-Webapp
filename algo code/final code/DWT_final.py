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


# # Load the data
# data1 = load_json('data_pool_5/sync_right_hand_data.json')
# data2 = load_json('data_pool_5/sync_left_hand_data.json')
#
# # Extract palm positions
# positions1 = extract_palm_positions(data1)
# positions2 = extract_palm_positions(data2)
#
# # Controlled DTW comparison for Palm Position
# normalized_distance_position, dist_position = controlled_dtw(positions1, positions2, data1, data2, margin=0,
#                                                              window_size=5)
# print("DTW Distance with Margin (Position):", dist_position)
# print("Normalized Controlled DTW Distance with Margin (Position):", normalized_distance_position)
# print()
#
# # Extract palm velocities
# velocities1 = extract_palm_velocities(data1)
# velocities2 = extract_palm_velocities(data2)
#
# # Controlled DTW comparison for Palm Velocity
# normalized_distance_velocity, dist_velocity = controlled_dtw(velocities1, velocities2, data1, data2, margin=0,
#                                                              window_size=5)
# print("DTW Distance with Margin (Velocity):", dist_velocity)
# print("Normalized Controlled DTW Distance with Margin (Velocity):", normalized_distance_velocity)
# print()
#
# # Extract tip positions
# tip_positions1 = extract_tip_positions(data1)
# tip_positions2 = extract_tip_positions(data2)
#
# # Controlled DTW comparison for Tip Position
# normalized_distance_tip_position, dist_tip_position = controlled_dtw(tip_positions1, tip_positions2, data1, data2,
#                                                                      margin=0, window_size=5)
# print("DTW Distance with Margin (Tip Position):", dist_tip_position)
# print("Normalized Controlled DTW Distance with Margin (Tip Position):", normalized_distance_tip_position)
# print()
#
# # Extract and compare Wrist Positions
# wrist_positions1 = extract_wrist_positions(data1)
# wrist_positions2 = extract_wrist_positions(data2)
#
# # Controlled DTW comparison for Wrist Position
# normalized_distance_wrist, dist_wrist = controlled_dtw(wrist_positions1, wrist_positions2, data1, data2, margin=0,
#                                                        window_size=5)
# print("DTW Distance with Margin (Wrist Position):", dist_wrist)
# print("Normalized Controlled DTW Distance with Margin (Wrist Position):", normalized_distance_wrist)
# print()
#
# # **Extract and compare Bone Positions for each finger individually**
# for finger_index in range(5):  # Assuming there are 5 fingers
#     bone_positions1 = extract_finger_bone_positions(data1, finger_index)
#     bone_positions2 = extract_finger_bone_positions(data2, finger_index)
#
#     # Controlled DTW comparison for Bone Positions for each finger
#     normalized_distance_bone, dist_bone = controlled_dtw(bone_positions1, bone_positions2, data1, data2, margin=0,
#                                                          window_size=5)
#     print(f"DTW Distance with Margin (Bone Position) for Finger {finger_index + 1}:", dist_bone)
#     print(f"Normalized Controlled DTW Distance with Margin (Bone Position) for Finger {finger_index + 1}:",
#           normalized_distance_bone)
#     print()
