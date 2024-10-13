'''
Dynamic Time Warping (DTW) is an algorithm for measuring the similarity between two temporal sequences that may vary in speed.
The main idea is to align the sequences in a way that minimizes the total distance between them.
This can handle sequences of different lengths and can align sequences even if they are out of phase.

here we are working with a distance so we need to use abs on all the data !!!
'''

import json
import numpy as np
from scipy.spatial.distance import euclidean
from fastdtw import fastdtw

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

# Load the data
data1 = load_json('data_pool_2/data4.json')
data2 = load_json('data_pool_2/mirrored_data4.json')
# data2 = load_json('data_pool_2/suffle.json')

# Extract palm positions
positions1 = extract_palm_positions(data1)
positions2 = extract_palm_positions(data2)

# Dynamic Time Warping (DTW) using Palm Position
distance_position, path_position = fastdtw(positions1, positions2, dist=euclidean)
print("DTW Distance (Position):", distance_position)

# Normalize DTW distance for Palm Position
normalized_distance_position = distance_position / len(positions1)
print("Normalized DTW Distance (Position):", normalized_distance_position)

# Extract palm velocities
velocities1 = extract_palm_velocities(data1)
velocities2 = extract_palm_velocities(data2)

# Dynamic Time Warping (DTW) using Palm Velocity
distance_velocity, path_velocity = fastdtw(velocities1, velocities2, dist=euclidean)
print("DTW Distance (Velocity):", distance_velocity)

# Normalize DTW distance for Palm Velocity
normalized_distance_velocity = distance_velocity / len(velocities1)
print("Normalized DTW Distance (Velocity):", normalized_distance_velocity)

# Extract tip positions
tip_positions1 = extract_tip_positions(data1)
tip_positions2 = extract_tip_positions(data2)

# Dynamic Time Warping (DTW) using Tip Position
distance_tip_position, path_tip_position = fastdtw(tip_positions1, tip_positions2, dist=euclidean)
print("DTW Distance (Tip Position):", distance_tip_position)

# Normalize DTW distance for Tip Position
normalized_distance_tip_position = distance_tip_position / len(tip_positions1)
print("Normalized DTW Distance (Tip Position):", normalized_distance_tip_position)
