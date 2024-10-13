# import json
# import numpy as np
# from scipy.spatial.distance import euclidean
# from fastdtw import fastdtw

# # Function to load JSON data
# def load_json(file_path):
#     with open(file_path, 'r') as file:
#         data = [json.loads(line) for line in file]
#     return data

# # Function to extract palm positions
# def extract_palm_positions(data):
#     positions = []
#     for frame in data:
#         palm_position = frame['PalmPosition']
#         positions.append([abs(palm_position['x']), abs(palm_position['y']), abs(palm_position['z'])])
#     return np.array(positions)

# # Function to extract palm velocities
# def extract_palm_velocities(data):
#     velocities = []
#     for frame in data:
#         palm_velocity = frame['PalmVelocity']
#         velocities.append([abs(palm_velocity['x']), abs(palm_velocity['y']), abs(palm_velocity['z'])])
#     return np.array(velocities)

# # Function to extract tip positions
# def extract_tip_positions(data):
#     positions = []
#     for frame in data:
#         frame_positions = []
#         for finger in frame['fingers']:
#             tip_position = finger['TipPosition']
#             frame_positions.append([abs(tip_position['x']), abs(tip_position['y']), abs(tip_position['z'])])
#         positions.append(np.mean(frame_positions, axis=0))
#     return np.array(positions)

# # Main function to perform DTW analysis on two JSON files
# def analyze_sync(json_file1, json_file2):
#     data1 = load_json(json_file1)
#     data2 = load_json(json_file2)

#     # Extract palm positions
#     positions1 = extract_palm_positions(data1)
#     positions2 = extract_palm_positions(data2)

#     # Dynamic Time Warping (DTW) using Palm Position
#     distance_position, path_position = fastdtw(positions1, positions2, dist=euclidean)
#     normalized_distance_position = distance_position / len(positions1)

#     # Extract palm velocities
#     velocities1 = extract_palm_velocities(data1)
#     velocities2 = extract_palm_velocities(data2)

#     # Dynamic Time Warping (DTW) using Palm Velocity
#     distance_velocity, path_velocity = fastdtw(velocities1, velocities2, dist=euclidean)
#     normalized_distance_velocity = distance_velocity / len(velocities1)

#     # Extract tip positions
#     tip_positions1 = extract_tip_positions(data1)
#     tip_positions2 = extract_tip_positions(data2)

#     # Dynamic Time Warping (DTW) using Tip Position
#     distance_tip_position, path_tip_position = fastdtw(tip_positions1, tip_positions2, dist=euclidean)
#     normalized_distance_tip_position = distance_tip_position / len(tip_positions1)

#     # Return the results instead of printing them
#     return {
#         "distance_position": distance_position,
#         "normalized_distance_position": normalized_distance_position,
#         "distance_velocity": distance_velocity,
#         "normalized_distance_velocity": normalized_distance_velocity,
#         "distance_tip_position": distance_tip_position,
#         "normalized_distance_tip_position": normalized_distance_tip_position
#     }
import json
import sys
import numpy as np
from scipy.spatial.distance import euclidean
from fastdtw import fastdtw

# Ensure the script receives exactly two arguments (the paths to the JSON files)
if len(sys.argv) != 3:
    print("Usage: python DWTUnity.py <json_file1> <json_file2>")
    sys.exit(1)

json_file1 = sys.argv[1]
json_file2 = sys.argv[2]

# Function to load JSON data
def load_json(file_path):
    with open(file_path, 'r') as file:
        data = [json.loads(line) for line in file]
    return data

# Function to perform the analysis
def analyze_sync(json_file1, json_file2):
    data1 = load_json(json_file1)
    data2 = load_json(json_file2)

    # Sample logic: You can replace this with your actual DTW analysis logic
    positions1 = np.random.rand(100, 3)  # Dummy data for example purposes
    positions2 = np.random.rand(100, 3)  # Dummy data for example purposes

    distance, _ = fastdtw(positions1, positions2, dist=euclidean)
    normalized_distance = distance / len(positions1)

    # Return results to Unity
    result = {
        "distance_position": distance,
        "normalized_distance_position": normalized_distance
    }

    print(result)

# Run the analysis
analyze_sync(json_file1, json_file2)
