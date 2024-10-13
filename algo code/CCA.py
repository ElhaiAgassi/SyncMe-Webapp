'''
In summary, CCA helps in understanding the extent to which two multidimensional
datasets are related to each other by finding the linear combinations of the
variables in each set that are maximally correlated.
This can be particularly useful in analyzing synchronization in movement data,
as it quantifies the degree of similarity in the patterns of the two datasets.
'''

import json
import numpy as np
from sklearn.cross_decomposition import CCA

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

# Load the data
data1 = load_json('data_pool_2/data4.json')
data2 = load_json('data_pool_2/mirrored_data4.json')
# data2 = load_json('data_pool_2/suffle.json')

# Extract palm positions
positions1 = extract_palm_positions(data1)
positions2 = extract_palm_positions(data2)

# Canonical Correlation Analysis (CCA) using Palm Position
cca = CCA(n_components=1)
cca.fit(positions1, positions2)
X_c, Y_c = cca.transform(positions1, positions2)
correlation_position = np.corrcoef(X_c.T, Y_c.T)[0, 1]
print("CCA Correlation (Position):", correlation_position)

# Extract palm velocities
velocities1 = extract_palm_velocities(data1)
velocities2 = extract_palm_velocities(data2)

# Canonical Correlation Analysis (CCA) using Palm Velocity
cca.fit(velocities1, velocities2)
X_c, Y_c = cca.transform(velocities1, velocities2)
correlation_velocity = np.corrcoef(X_c.T, Y_c.T)[0, 1]
print("CCA Correlation (Velocity):", correlation_velocity)

# Extract tip positions
tip_positions1 = extract_tip_positions(data1)
tip_positions2 = extract_tip_positions(data2)

# Canonical Correlation Analysis (CCA) using Tip Position
cca.fit(tip_positions1, tip_positions2)
X_c, Y_c = cca.transform(tip_positions1, tip_positions2)
correlation_tip = np.corrcoef(X_c.T, Y_c.T)[0, 1]
print("CCA Correlation (Tip Position):", correlation_tip)
