from DWT_final import *
from CCA_final import *
from CroosCorrelation_final import *
from Wavlet_final import *
from split_left_right import *

hand_recordings = 'data_pool_7/synced2.json'
left_hand, right_hand = split_json_by_hand(hand_recordings)

data1 = right_hand
data2 = left_hand

########################################## DWT ###################################################
print("########## DWT ##########")
# Extract palm positions
positions1 = extract_palm_positions(data1)
positions2 = extract_palm_positions(data2)

# Controlled DTW comparison for Palm Position
normalized_distance_position, dist_position = controlled_dtw(positions1, positions2, data1, data2, margin=0,
                                                             window_size=5)
print("DTW Distance with Margin (Position):", dist_position)
print("Normalized Controlled DTW Distance with Margin (Position):", normalized_distance_position)
print()

# Extract palm velocities
velocities1 = extract_palm_velocities(data1)
velocities2 = extract_palm_velocities(data2)

# Controlled DTW comparison for Palm Velocity
normalized_distance_velocity, dist_velocity = controlled_dtw(velocities1, velocities2, data1, data2, margin=0,
                                                             window_size=5)
print("DTW Distance with Margin (Velocity):", dist_velocity)
print("Normalized Controlled DTW Distance with Margin (Velocity):", normalized_distance_velocity)
print()

# Extract tip positions
tip_positions1 = extract_tip_positions(data1)
tip_positions2 = extract_tip_positions(data2)

# Controlled DTW comparison for Tip Position
normalized_distance_tip_position, dist_tip_position = controlled_dtw(tip_positions1, tip_positions2, data1, data2,
                                                                     margin=0, window_size=5)
print("DTW Distance with Margin (Tip Position):", dist_tip_position)
print("Normalized Controlled DTW Distance with Margin (Tip Position):", normalized_distance_tip_position)
print()

# Extract and compare Wrist Positions
wrist_positions1 = extract_wrist_positions(data1)
wrist_positions2 = extract_wrist_positions(data2)

# Controlled DTW comparison for Wrist Position
normalized_distance_wrist, dist_wrist = controlled_dtw(wrist_positions1, wrist_positions2, data1, data2, margin=0,
                                                       window_size=5)
print("DTW Distance with Margin (Wrist Position):", dist_wrist)
print("Normalized Controlled DTW Distance with Margin (Wrist Position):", normalized_distance_wrist)
print()

# **Extract and compare Bone Positions for each finger individually**
for finger_index in range(5):  # Assuming there are 5 fingers
    bone_positions1 = extract_finger_bone_positions(data1, finger_index)
    bone_positions2 = extract_finger_bone_positions(data2, finger_index)

    # Controlled DTW comparison for Bone Positions for each finger
    normalized_distance_bone, dist_bone = controlled_dtw(bone_positions1, bone_positions2, data1, data2, margin=0,
                                                         window_size=5)
    print(f"DTW Distance with Margin (Bone Position) for Finger {finger_index + 1}:", dist_bone)
    print(f"Normalized Controlled DTW Distance with Margin (Bone Position) for Finger {finger_index + 1}:",
          normalized_distance_bone)
    print()
########################################## DWT ###################################################

########################################## CCA ###################################################
print("########## CCA ##########")
# Extract finger bone vectors for both hands
finger_vectors1 = extract_finger_vectors(data1)
finger_vectors2 = extract_finger_vectors(data2)

# Truncate both finger vector datasets to the shortest length
finger_vectors1, finger_vectors2 = truncate_to_shortest(finger_vectors1, finger_vectors2)

# Apply mirror transformation to the left hand's data_pool_6
finger_vectors2_mirrored = apply_mirror_transformation(finger_vectors2)

# Compare fingers using CCA
compare_fingers_with_cca(finger_vectors1, finger_vectors2_mirrored)

# Extract Palm-to-Tip vectors for both hands
palm_to_tip_vectors1 = extract_palm_to_tip_vectors(data1)
palm_to_tip_vectors2 = extract_palm_to_tip_vectors(data2)

# Truncate both Palm-to-Tip vector datasets to the shortest length
palm_to_tip_vectors1, palm_to_tip_vectors2 = truncate_to_shortest(palm_to_tip_vectors1, palm_to_tip_vectors2)

# Apply mirror transformation to Palm-to-Tip vectors
palm_to_tip_vectors2_mirrored = apply_mirror_transformation(palm_to_tip_vectors2)

# Compare Palm-to-Tip vectors using CCA
compare_palm_to_tip_vectors(palm_to_tip_vectors1, palm_to_tip_vectors2_mirrored)
print()
########################################## CCA ###################################################

###################################### CroosCorrelation ##########################################
print("########## CroosCorrelation ##########")
################
# the file on axis = 1 is to take the mirrored hand and shift it to match the other hand
################

# Flip data for mirrored hand comparison
positions2 = np.flip(extract_palm_positions(data2), axis=1)

# Extract palm positions and perform cross-correlation
positions1 = extract_palm_positions(data1)
correlation_normalized = cross_correlation_normalized(positions1[:, 0], positions2[:, 0])
max_corr = np.max(correlation_normalized)
lag = np.argmax(correlation_normalized) - (len(positions1) - 1)
corr_without_lag_positions = correlation_without_lag(positions1[:, 0], positions2[:, 0])

print("Maximum Correlation (Normalized) with Lag (Palm Positions):", max_corr)
print("Lag at Maximum Correlation:", lag)
print("Correlation Without Lag (Palm Positions):", corr_without_lag_positions)
print()

# Extract palm velocities and perform cross-correlation
velocities1 = extract_palm_velocities(data1)
velocities2 = np.flip(extract_palm_velocities(data2), axis=1)
correlation_velocity_normalized = cross_correlation_normalized(velocities1[:, 0], velocities2[:, 0])
max_corr_velocity = np.max(correlation_velocity_normalized)
lag_velocity = np.argmax(correlation_velocity_normalized) - (len(velocities1) - 1)
corr_without_lag_velocities = correlation_without_lag(velocities1[:, 0], velocities2[:, 0])

print("Maximum Correlation (Normalized) with Lag (Velocities):", max_corr_velocity)
print("Lag at Maximum Correlation:", lag_velocity)
print("Correlation Without Lag (Velocities):", corr_without_lag_velocities)
print()

# Extract tip positions and perform cross-correlation
tip_positions1 = extract_tip_positions(data1)
tip_positions2 = np.flip(extract_tip_positions(data2), axis=1)
correlation_tip_normalized = cross_correlation_normalized(tip_positions1[:, 0], tip_positions2[:, 0])
max_corr_tip = np.max(correlation_tip_normalized)
lag_tip = np.argmax(correlation_tip_normalized) - (len(tip_positions1) - 1)
corr_without_lag_tips = correlation_without_lag(tip_positions1[:, 0], tip_positions2[:, 0])

print("Maximum Correlation (Normalized) with Lag (Tip Positions):", max_corr_tip)
print("Lag at Maximum Correlation:", lag_tip)
print("Correlation Without Lag (Tip Positions):", corr_without_lag_tips)
print()

# **Extract wrist positions and perform cross-correlation**
wrist_positions1 = extract_wrist_positions(data1)
wrist_positions2 = np.flip(extract_wrist_positions(data2), axis=1)
correlation_wrist_normalized = cross_correlation_normalized(wrist_positions1[:, 0], wrist_positions2[:, 0])
max_corr_wrist = np.max(correlation_wrist_normalized)
lag_wrist = np.argmax(correlation_wrist_normalized) - (len(wrist_positions1) - 1)
corr_without_lag_wrist = correlation_without_lag(wrist_positions1[:, 0], wrist_positions2[:, 0])

print("Maximum Correlation (Normalized) with Lag (Wrist Positions):", max_corr_wrist)
print("Lag at Maximum Correlation:", lag_wrist)
print("Correlation Without Lag (Wrist Positions):", corr_without_lag_wrist)
print()

# **Extract and compare bone positions for each finger individually**
for finger_index in range(5):  # Assuming there are 5 fingers
    bone_positions1 = extract_finger_bone_positions(data1, finger_index)
    bone_positions2 = np.flip(extract_finger_bone_positions(data2, finger_index), axis=1)

    correlation_bone_normalized = cross_correlation_normalized(bone_positions1[:, 0], bone_positions2[:, 0])
    max_corr_bone = np.max(correlation_bone_normalized)
    lag_bone = np.argmax(correlation_bone_normalized) - (len(bone_positions1) - 1)
    corr_without_lag_bone = correlation_without_lag(bone_positions1[:, 0], bone_positions2[:, 0])

    print(f"Maximum Correlation (Normalized) with Lag (Finger {finger_index + 1} Bone Positions):", max_corr_bone)
    print(f"Lag at Maximum Correlation (Finger {finger_index + 1}):", lag_bone)
    print(f"Correlation Without Lag (Finger {finger_index + 1} Bone Positions):", corr_without_lag_bone)
    print()
###################################### CroosCorrelation ##########################################

########################################### Wavelet ##############################################
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
########################################### Wavelet ##############################################