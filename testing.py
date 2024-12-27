import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.transform import Rotation as R

# Ideal Rotation Data: 180 degrees about the y-axis
data15 = """
Acceleration X: 0.00, Y: 0.00, Z: 9.81 m/s^2
Rotation X: 0.00, Y: 1, Z: 0.00 rad/s
Temperature: 25.00 degC
Acceleration X: 0.00, Y: 0.00, Z: 9.81 m/s^2
Rotation X: 0.00, Y: 1, Z: 0.00 rad/s
Temperature: 25.05 degC
Acceleration X: 0.00, Y: 0.00, Z: 9.81 m/s^2
Rotation X: 0.00, Y: 1, Z: 0.00 rad/s
Temperature: 25.10 degC
Acceleration X: 0.00, Y: 0.00, Z: 9.81 m/s^2
Rotation X: 0.00, Y: 1, Z: 0.00 rad/s
Temperature: 25.15 degC
Acceleration X: 0.00, Y: 0.00, Z: 9.81 m/s^2
Rotation X: 0.00, Y: 1, Z: 0.00 rad/s
Temperature: 25.20 degC
Acceleration X: 0.00, Y: 0.00, Z: 9.81 m/s^2
Rotation X: 0.00, Y: 1, Z: 0.00 rad/s
Temperature: 25.25 degC
Acceleration X: 0.00, Y: -0.00, Z: 9.81 m/s^2
Rotation X: 0.00, Y: 1, Z: 0.00 rad/s
Temperature: 25.30 degC
Acceleration X: 0.00, Y: 0.00, Z: 9.81 m/s^2
Rotation X: 0.00, Y: 1, Z: 0.00 rad/s
Temperature: 25.35 degC
Acceleration X: 0.00, Y: 0.00, Z: 9.81 m/s^2
Rotation X: 0.00, Y: 1, Z: 0.00 rad/s
Temperature: 25.40 degC
Acceleration X: 0.00, Y: 0.00, Z: 9.81 m/s^2
Rotation X: 0.00, Y: 1, Z: 0.00 rad/s
Temperature: 25.45 degC
Acceleration X: 0.00, Y: 0.00, Z: 9.81 m/s^2
Rotation X: 0.00, Y: 1, Z: 0.00 rad/s
Temperature: 25.50 degC
Acceleration X: 0.00, Y: 0.00, Z: 9.81 m/s^2
Rotation X: 0.00, Y: 1, Z: 0.00 rad/s
Temperature: 25.55 degC
"""

# Ideal Rotation Data: 180 degrees about the z-axis
data10 = """
Acceleration X: 0.00, Y: 0.00, Z: 9.81 m/s^2
Rotation X: 0.00, Y: 0.00, Z: 3.14 rad/s
Temperature: 25.00 degC
Acceleration X: 0.00, Y: 0.00, Z: 9.81 m/s^2
Rotation X: 0.00, Y: 0.00, Z: 3.14 rad/s
Temperature: 25.05 degC
Acceleration X: 0.00, Y: 0.00, Z: 9.81 m/s^2
Rotation X: 0.00, Y: 0.00, Z: 3.14 rad/s
Temperature: 25.10 degC
Acceleration X: 0.00, Y: 0.00, Z: 9.81 m/s^2
Rotation X: 0.00, Y: 0.00, Z: 3.14 rad/s
Temperature: 25.15 degC
Acceleration X: 0.00, Y: 0.00, Z: 9.81 m/s^2
Rotation X: 0.00, Y: 0.00, Z: 3.14 rad/s
Temperature: 25.20 degC
Acceleration X: 0.00, Y: 0.00, Z: 9.81 m/s^2
Rotation X: 0.00, Y: 0.00, Z: 3.14 rad/s
Temperature: 25.25 degC
Acceleration X: 0.00, Y: -0.00, Z: 9.81 m/s^2
Rotation X: 0.00, Y: 0.00, Z: 3.14 rad/s
Temperature: 25.30 degC
Acceleration X: 0.00, Y: 0.00, Z: 9.81 m/s^2
Rotation X: 0.00, Y: 0.00, Z: 3.14 rad/s
Temperature: 25.35 degC
Acceleration X: 0.00, Y: 0.00, Z: 9.81 m/s^2
Rotation X: 0.00, Y: 0.00, Z: 3.14 rad/s
Temperature: 25.40 degC
Acceleration X: 0.00, Y: 0.00, Z: 9.81 m/s^2
Rotation X: 0.00, Y: 0.00, Z: 3.14 rad/s
Temperature: 25.45 degC
Acceleration X: 0.00, Y: 0.00, Z: 9.81 m/s^2
Rotation X: 0.00, Y: 0.00, Z: 3.14 rad/s
Temperature: 25.50 degC
Acceleration X: 0.00, Y: 0.00, Z: 9.81 m/s^2
Rotation X: 0.00, Y: 0.00, Z: 3.14 rad/s
Temperature: 25.55 degC
"""

# Sample Rotations Data
data4 = """
Acceleration X: -0.56, Y: 1.53, Z: 8.92 m/s^2
Rotation X: -0.06, Y: -0.02, Z: 0.03 rad/s
Temperature: 34.88 degC

Acceleration X: -0.57, Y: 1.63, Z: 8.94 m/s^2
Rotation X: -0.07, Y: -0.08, Z: 0.03 rad/s
Temperature: 34.90 degC

Acceleration X: -0.30, Y: 1.75, Z: 8.91 m/s^2
Rotation X: -0.05, Y: -0.05, Z: 0.01 rad/s
Temperature: 34.92 degC

Acceleration X: 0.40, Y: 1.85, Z: 8.89 m/s^2
Rotation X: -0.04, Y: -0.04, Z: 0.06 rad/s
Temperature: 34.94 degC

Acceleration X: 2.38, Y: 2.22, Z: 8.23 m/s^2
Rotation X: 0.04, Y: -0.86, Z: 0.05 rad/s
Temperature: 34.97 degC

Acceleration X: 4.90, Y: 2.57, Z: 7.63 m/s^2
Rotation X: 0.06, Y: -0.45, Z: 0.06 rad/s
Temperature: 34.98 degC

Acceleration X: 6.91, Y: 4.01, Z: 5.01 m/s^2
Rotation X: 0.05, Y: -1.02, Z: -0.25 rad/s
Temperature: 35.01 degC

Acceleration X: 8.22, Y: 5.03, Z: -0.59 m/s^2
Rotation X: 0.47, Y: -1.11, Z: -0.13 rad/s
Temperature: 35.05 degC

Acceleration X: 6.02, Y: 4.01, Z: -8.35 m/s^2
Rotation X: 0.96, Y: -1.76, Z: -0.28 rad/s
Temperature: 35.13 degC

Acceleration X: 2.05, Y: 2.16, Z: -10.70 m/s^2
Rotation X: -0.00, Y: -0.31, Z: 0.50 rad/s
Temperature: 35.21 degC

Acceleration X: -0.07, Y: 2.12, Z: -11.05 m/s^2
Rotation X: -0.08, Y: -0.11, Z: 0.03 rad/s
Temperature: 35.24 degC

Acceleration X: 0.17, Y: 2.31, Z: -10.65 m/s^2
Rotation X: -0.06, Y: 0.03, Z: 0.02 rad/s
Temperature: 35.30 degC

Acceleration X: 0.37, Y: 2.46, Z: -10.66 m/s^2
Rotation X: -0.05, Y: -0.04, Z: 0.07 rad/s
Temperature: 35.34 degC

Acceleration X: 0.75, Y: 2.47, Z: -10.45 m/s^2
Rotation X: -0.11, Y: -0.03, Z: 0.01 rad/s
Temperature: 35.38 degC

"""

# Validate Acc,Vel,Pos Graphs
data5 = """
Acceleration X: 1.62, Y: 0.20, Z: 8.93 m/s^2
Rotation X: -0.08, Y: -0.02, Z: 0.03 rad/s
Temperature: 33.73 degC

Acceleration X: 1.66, Y: 0.13, Z: 8.92 m/s^2
Rotation X: -0.07, Y: -0.01, Z: 0.03 rad/s
Temperature: 33.78 degC

Acceleration X: 1.80, Y: 0.01, Z: 8.88 m/s^2
Rotation X: -0.20, Y: -0.20, Z: -0.04 rad/s
Temperature: 33.79 degC

Acceleration X: 1.95, Y: -0.30, Z: 8.72 m/s^2
Rotation X: 0.01, Y: 0.05, Z: -0.04 rad/s
Temperature: 33.81 degC

Acceleration X: 2.13, Y: 0.25, Z: 8.83 m/s^2
Rotation X: -0.08, Y: -0.09, Z: -0.03 rad/s
Temperature: 33.82 degC

Acceleration X: 2.47, Y: 0.49, Z: 8.31 m/s^2
Rotation X: -0.04, Y: -0.10, Z: 0.02 rad/s
Temperature: 33.83 degC

Acceleration X: 3.00, Y: 0.52, Z: 8.41 m/s^2
Rotation X: -0.06, Y: -0.12, Z: 0.04 rad/s
Temperature: 33.84 degC

Acceleration X: 2.97, Y: 0.52, Z: 8.85 m/s^2
Rotation X: -0.07, Y: -0.02, Z: 0.02 rad/s
Temperature: 33.85 degC

Acceleration X: 2.82, Y: 0.51, Z: 8.67 m/s^2
Rotation X: -0.15, Y: -0.07, Z: 0.01 rad/s
Temperature: 33.88 degC

Acceleration X: 2.89, Y: 0.11, Z: 8.76 m/s^2
Rotation X: -0.11, Y: 0.01, Z: 0.04 rad/s
Temperature: 33.88 degC

Acceleration X: 3.27, Y: -0.43, Z: 8.71 m/s^2
Rotation X: -0.19, Y: 0.03, Z: 0.07 rad/s
Temperature: 33.89 degC

Acceleration X: 2.72, Y: -0.84, Z: 8.49 m/s^2
Rotation X: -0.15, Y: 0.04, Z: 0.02 rad/s
Temperature: 33.91 degC

Acceleration X: 1.89, Y: -0.48, Z: 8.86 m/s^2
Rotation X: -0.13, Y: 0.03, Z: 0.10 rad/s
Temperature: 33.94 degC"""

# IDEAL POSITION
data = """ 
Acceleration X: 0.00, Y: 0.00, Z: -9.81 m/s^2
Rotation X: 0.00, Y: 0.00, Z: 0.00 rad/s
Temperature: 25.00 degC

Acceleration X: 0.00, Y: 0.00, Z: -9.81 m/s^2
Rotation X: 0.00, Y: 0.00, Z: 0.00 rad/s
Temperature: 25.05 degC

Acceleration X: 0.00, Y: 0.00, Z: -9.81 m/s^2
Rotation X: 0.00, Y: 0.00, Z: 0.00 rad/s
Temperature: 25.10 degC

Acceleration X: 0.00, Y: 0.00, Z: -9.81 m/s^2
Rotation X: 0.00, Y: 0.00, Z: 0.00 rad/s
Temperature: 25.15 degC

Acceleration X: 0.00, Y: 0.00, Z: -7.81 m/s^2
Rotation X: 0.00, Y: 0.00, Z: 0.00 rad/s
Temperature: 25.20 degC

Acceleration X: 0.00, Y: 0.00, Z: -7.81 m/s^2
Rotation X: 0.00, Y: 0.00, Z: 0.00 rad/s
Temperature: 25.25 degC

Acceleration X: 0.00, Y: 0.00, Z: -7.81 m/s^2
Rotation X: 0.00, Y: 0.00, Z: 0.00 rad/s
Temperature: 25.30 degC

Acceleration X: 0.00, Y: 0.00, Z: -7.81 m/s^2
Rotation X: 0.00, Y: 0.00, Z: 0.00 rad/s
Temperature: 25.35 degC

Acceleration X: 0.00, Y: 0.00, Z: -11.81 m/s^2
Rotation X: 0.00, Y: 0.00, Z: 0.00 rad/s
Temperature: 25.60 degC

Acceleration X: 0.00, Y: 0.00, Z: -11.81 m/s^2
Rotation X: 0.00, Y: 0.00, Z: 0.00 rad/s
Temperature: 25.65 degC

Acceleration X: 0.00, Y: 0.00, Z: -11.81 m/s^2
Rotation X: 0.00, Y: 0.00, Z: 0.00 rad/s
Temperature: 25.70 degC

Acceleration X: 0.00, Y: 0.00, Z: -11.81 m/s^2
Rotation X: 0.00, Y: 0.00, Z: 0.00 rad/s
Temperature: 25.75 degC

Acceleration X: 0.00, Y: 0.00, Z: -9.81 m/s^2
Rotation X: 0.00, Y: 0.00, Z: 0.00 rad/s
Temperature: 25.40 degC

Acceleration X: 0.00, Y: 0.00, Z: -9.81 m/s^2
Rotation X: 0.00, Y: 0.00, Z: 0.00 rad/s
Temperature: 25.45 degC

Acceleration X: 0.00, Y: 0.00, Z: -9.81 m/s^2
Rotation X: 0.00, Y: 0.00, Z: 0.00 rad/s
Temperature: 25.50 degC

Acceleration X: 0.00, Y: 0.00, Z: -9.81 m/s^2
Rotation X: 0.00, Y: 0.00, Z: 0.00 rad/s
Temperature: 25.55 degC

Acceleration X: 0.00, Y: 0.00, Z: -11.81 m/s^2
Rotation X: 0.00, Y: 0.00, Z: 0.00 rad/s
Temperature: 25.60 degC

Acceleration X: 0.00, Y: 0.00, Z: -11.81 m/s^2
Rotation X: 0.00, Y: 0.00, Z: 0.00 rad/s
Temperature: 25.65 degC

Acceleration X: 0.00, Y: 0.00, Z: -11.81 m/s^2
Rotation X: 0.00, Y: 0.00, Z: 0.00 rad/s
Temperature: 25.70 degC

Acceleration X: 0.00, Y: 0.00, Z: -11.81 m/s^2
Rotation X: 0.00, Y: 0.00, Z: 0.00 rad/s
Temperature: 25.75 degC

Acceleration X: 0.00, Y: 0.00, Z: -7.81 m/s^2
Rotation X: 0.00, Y: 0.00, Z: 0.00 rad/s
Temperature: 25.20 degC

Acceleration X: 0.00, Y: 0.00, Z: -7.81 m/s^2
Rotation X: 0.00, Y: 0.00, Z: 0.00 rad/s
Temperature: 25.25 degC

Acceleration X: 0.00, Y: 0.00, Z: -7.81 m/s^2
Rotation X: 0.00, Y: 0.00, Z: 0.00 rad/s
Temperature: 25.30 degC

Acceleration X: 0.00, Y: 0.00, Z: -7.81 m/s^2
Rotation X: 0.00, Y: 0.00, Z: 0.00 rad/s
Temperature: 25.35 degC

Acceleration X: 0.00, Y: 0.00, Z: -9.81 m/s^2
Rotation X: 0.00, Y: 0.00, Z: 0.00 rad/s
Temperature: 25.00 degC

Acceleration X: 0.00, Y: 0.00, Z: -9.81 m/s^2
Rotation X: 0.00, Y: 0.00, Z: 0.00 rad/s
Temperature: 25.05 degC

Acceleration X: 0.00, Y: 0.00, Z: -9.81 m/s^2
Rotation X: 0.00, Y: 0.00, Z: 0.00 rad/s
Temperature: 25.10 degC

Acceleration X: 0.00, Y: 0.00, Z: -9.81 m/s^2
Rotation X: 0.00, Y: 0.00, Z: 0.00 rad/s
Temperature: 25.15 degC
"""

# Rotation Matrix + Position
data = """ 
Acceleration X: 0.00, Y: 0.00, Z: -9.81 m/s^2
Rotation X: 0.00, Y: 0.00, Z: 0.00 rad/s
Temperature: 25.00 degC

Acceleration X: 0.00, Y: 0.00, Z: -9.81 m/s^2
Rotation X: 0.00, Y: 0.00, Z: 0.00 rad/s
Temperature: 25.05 degC

Acceleration X: 0.00, Y: 0.00, Z: -9.81 m/s^2
Rotation X: 0.00, Y: 0.00, Z: 0.00 rad/s
Temperature: 25.10 degC

Acceleration X: 0.00, Y: 0.00, Z: -9.81 m/s^2
Rotation X: 0.00, Y: 0.00, Z: 0.00 rad/s
Temperature: 25.15 degC

Acceleration X: 0.00, Y: 0.00, Z: -7.81 m/s^2
Rotation X: 0.00, Y: 0.00, Z: 0.00 rad/s
Temperature: 25.20 degC

Acceleration X: 0.00, Y: 0.00, Z: -7.81 m/s^2
Rotation X: 0.00, Y: 0.00, Z: 0.00 rad/s
Temperature: 25.25 degC

Acceleration X: 0.00, Y: 0.00, Z: -7.81 m/s^2
Rotation X: 0.00, Y: 0.00, Z: 0.00 rad/s
Temperature: 25.30 degC

Acceleration X: 0.00, Y: 0.00, Z: -7.81 m/s^2
Rotation X: 0.00, Y: 0.00, Z: 0.00 rad/s
Temperature: 25.35 degC

Acceleration X: 0.00, Y: 0.00, Z: -11.81 m/s^2
Rotation X: 0.00, Y: 0.00, Z: 0.00 rad/s
Temperature: 25.60 degC

Acceleration X: 0.00, Y: 0.00, Z: -11.81 m/s^2
Rotation X: 0.00, Y: 0.00, Z: 0.00 rad/s
Temperature: 25.65 degC

Acceleration X: 0.00, Y: 0.00, Z: -11.81 m/s^2
Rotation X: 0.00, Y: 0.00, Z: 0.00 rad/s
Temperature: 25.70 degC

Acceleration X: 0.00, Y: 0.00, Z: -11.81 m/s^2
Rotation X: 0.00, Y: 0.00, Z: 0.00 rad/s
Temperature: 25.75 degC

Acceleration X: 0.00, Y: 0.00, Z: -9.81 m/s^2
Rotation X: 0.00, Y: 0.00, Z: 0.00 rad/s
Temperature: 25.40 degC

Acceleration X: 0.00, Y: 0.00, Z: -9.81 m/s^2
Rotation X: 0.00, Y: 0.00, Z: 0.00 rad/s
Temperature: 25.45 degC

Acceleration X: 0.00, Y: 0.00, Z: -9.81 m/s^2
Rotation X: 0.00, Y: 0.00, Z: 0.00 rad/s
Temperature: 25.50 degC

Acceleration X: 0.00, Y: 0.00, Z: -9.81 m/s^2
Rotation X: 0.00, Y: 0.00, Z: 0.00 rad/s
Temperature: 25.55 degC

Acceleration X: -9.81, Y: 0.00, Z: 0 m/s^2
Rotation X: 0.00, Y: 3.14, Z: 0.00 rad/s
Temperature: 25.40 degC

Acceleration X: 0.00, Y: 0.00, Z: 9.81 m/s^2
Rotation X: 0.00, Y: 3.14, Z: 0.00 rad/s
Temperature: 25.45 degC

Acceleration X: 0.00, Y: 0.00, Z: 9.81 m/s^2
Rotation X: 0.00, Y: 0, Z: 0.00 rad/s
Temperature: 25.50 degC

Acceleration X: 0.00, Y: 0.00, Z: 9.81 m/s^2
Rotation X: 0.00, Y: 0, Z: 0.00 rad/s
Temperature: 25.55 degC

Acceleration X: 0.00, Y: 0.00, Z: 11.81 m/s^2
Rotation X: 0.00, Y: 0.00, Z: 0.00 rad/s
Temperature: 25.60 degC

Acceleration X: 0.00, Y: 0.00, Z: 11.81 m/s^2
Rotation X: 0.00, Y: 0.00, Z: 0.00 rad/s
Temperature: 25.65 degC

Acceleration X: 0.00, Y: 0.00, Z: 11.81 m/s^2
Rotation X: 0.00, Y: 0.00, Z: 0.00 rad/s
Temperature: 25.70 degC

Acceleration X: 0.00, Y: 0.00, Z: 11.81 m/s^2
Rotation X: 0.00, Y: 0.00, Z: 0.00 rad/s
Temperature: 25.75 degC

Acceleration X: 0.00, Y: 0.00, Z: 7.81 m/s^2
Rotation X: 0.00, Y: 0.00, Z: 0.00 rad/s
Temperature: 25.20 degC

Acceleration X: 0.00, Y: 0.00, Z: 7.81 m/s^2
Rotation X: 0.00, Y: 0.00, Z: 0.00 rad/s
Temperature: 25.25 degC

Acceleration X: 0.00, Y: 0.00, Z: 7.81 m/s^2
Rotation X: 0.00, Y: 0.00, Z: 0.00 rad/s
Temperature: 25.30 degC

Acceleration X: 0.00, Y: 0.00, Z: 7.81 m/s^2
Rotation X: 0.00, Y: 0.00, Z: 0.00 rad/s
Temperature: 25.35 degC

Acceleration X: 0.00, Y: 0.00, Z: 9.81 m/s^2
Rotation X: 0.00, Y: 0.00, Z: 0.00 rad/s
Temperature: 25.00 degC

Acceleration X: 0.00, Y: 0.00, Z: 9.81 m/s^2
Rotation X: 0.00, Y: 0.00, Z: 0.00 rad/s
Temperature: 25.05 degC

Acceleration X: 0.00, Y: 0.00, Z: 9.81 m/s^2
Rotation X: 0.00, Y: 0.00, Z: 0.00 rad/s
Temperature: 25.10 degC

Acceleration X: 0.00, Y: 0.00, Z: 9.81 m/s^2
Rotation X: 0.00, Y: 0.00, Z: 0.00 rad/s
Temperature: 25.15 degC
"""

lines = [l.strip() for l in data.strip().split('\n') if l.strip()]

accelerations = []
rotations = []

for i in range(0, len(lines), 3):
    accel_line = lines[i]
    rot_line = lines[i+1]

    # Parse acceleration
    accel_str = accel_line.replace("Acceleration", "").replace("X:", "").replace("Y:", "").replace("Z:", "")
    parts = accel_str.split(',')
    ax = float(parts[0].strip())
    ay = float(parts[1].strip())
    az_str = parts[2].strip().split(' ')[0]
    az = float(az_str)

    # Parse rotation
    rot_str = rot_line.replace("Rotation", "").replace("X:", "").replace("Y:", "").replace("Z:", "")
    rparts = rot_str.split(',')
    gx = float(rparts[0].strip())
    gy = float(rparts[1].strip())
    gz_str = rparts[2].strip().split(' ')[0]
    gz = float(gz_str)

    accelerations.append([ax, ay, az])
    rotations.append([gx, gy, gz])

accelerations = np.array(accelerations)
rotations = np.array(rotations)

dt = 0.5
num_samples = len(accelerations)

# Estimate gravity from the first reading
initial_acc = accelerations[0]
norm_g = np.linalg.norm(initial_acc)
gravity_vector = (initial_acc / norm_g) * 9.81 # * 9.80665

positions = [np.zeros(3)]
velocities = [np.zeros(3)]
rawAccelerations = accelerations
rotatedAccelerations = accelerations
# accelerations[:,2] = accelerations[:,2] - gravity_vector[2]

# Orientation tracking:
# Start with identity orientation (Initial quaternion)
current_orientation = R.from_quat([0, 0, 0, 1])  
# current_orientation = R.from_euler('xyz', [0,0,0], degrees=False)
orientations = [current_orientation]

for i in range(1, num_samples):
    # Orientation update:
    # Integrate gyro (in rad/s) over dt to get rotation vector
    # omega = rotations[i]  # [gx, gy, gz]
    # delta_theta = omega * dt  # small rotation
    # delta_rotation = R.from_rotvec(delta_theta)
    # current_orientation = orientations[-1] * delta_rotation
    # orientations.append(current_orientation)
    # print(current_orientation.as_euler('xyz', degrees=True))

    omega = rotations[i]  # [gx, gy, gz]
    delta_rotation = R.from_rotvec(omega * dt)
    current_orientation = current_orientation * delta_rotation
    # current_orientation = R.from_quat(current_orientation.as_quat() / np.linalg.norm(current_orientation.as_quat())) # prevent numerical drift
    orientations.append(current_orientation)

    # Integrate for velocity and position
    acc_linear = np.linalg.inv(current_orientation.as_matrix()) @ accelerations[i]
    # acc_linear = accelerations[i]
    acc_linear[2] = acc_linear[2] - gravity_vector[2]
    rotatedAccelerations[i] = acc_linear
    # print(acc_linear)
    v = velocities[-1] + acc_linear * dt
    p = positions[-1] + v * dt

    velocities.append(v)
    positions.append(p)

rotatedAccelerations[0] = [0, 0, 0] 
positions = np.array(positions)
velocities = np.array(velocities)
time = np.arange(num_samples)*dt

# Extract Euler angles (roll, pitch, yaw)
# euler_angles = []
# for o in orientations:
#     # 'xyz' convention: roll around X, pitch around Y, yaw around Z
#     euler = o.as_euler('xyz', degrees=True)  # in degrees
#     euler_angles.append(euler)
# euler_angles = np.array(euler_angles)

euler_angles = []
for quat in orientations:
    #o = R.from_quat(quat)
    euler = quat.as_euler('xyz', degrees=True)
    euler_angles.append(euler)
euler_angles = np.array(euler_angles)

roll = euler_angles[:,0]
pitch = euler_angles[:,1]
yaw = euler_angles[:,2]

# # Initialize cumulative rotation
# cumulative_rotation = R.identity()

# # Lists to store cumulative angles
# roll_list, pitch_list, yaw_list = [], [], []

# for orientation in orientations:
#     # Combine with previous rotation
#     cumulative_rotation = cumulative_rotation * orientation
    
#     # Get Euler angles from cumulative rotation
#     euler = cumulative_rotation.as_euler('zxz', degrees=True)
    
#     roll_list.append(euler[0])
#     pitch_list.append(euler[1])
#     yaw_list.append(euler[2])

# # Convert to numpy arrays
# roll = np.array(roll_list)
# pitch = np.array(pitch_list)
# yaw = np.array(yaw_list)

# Plot raw accelerations (m/s²)
plt.subplot(3, 3, 1)
# plt.figure()
print(rotatedAccelerations)
plt.plot(time, rotatedAccelerations[:,0], label='Ax (m/s²)')
plt.plot(time, rotatedAccelerations[:,1], label='Ay (m/s²)')
plt.plot(time, rotatedAccelerations[:,2], label='Az (m/s²)')
plt.title('Accelerations')
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (m/s²) (with Gravity Removed)')
plt.legend()
plt.grid(True)

# Plot Roll, Pitch, Yaw
plt.subplot(3, 3, 2)
# plt.figure()
print("time:")
print(time)
print("roll:")
print(roll)
plt.plot(time, roll, label='Roll (deg)')
plt.plot(time, pitch, label='Pitch (deg)')
plt.plot(time, yaw, label='Yaw (deg)')
plt.title('Roll, Pitch, Yaw vs Time')
plt.xlabel('Time (s)')
plt.ylabel('Angle (degrees)')
plt.legend()
plt.grid(True)

# Plot Roll, Pitch, Yaw Rates
import math
plt.subplot(3, 3, 5)
# plt.figure()
plt.plot(time, 180*rotations[:,0]/math.pi, label='Roll Rate (deg/s)')
plt.plot(time, 180*rotations[:,1]/math.pi, label='Pitch Rate (deg/s)')
plt.plot(time, 180*rotations[:,2]/math.pi, label='Yaw Rate(deg/s)')
plt.title('Roll, Pitch, Yaw Rates vs Time')
plt.xlabel('Time (s)')
plt.ylabel('Angle (degrees/s)')
# plt.legend()
plt.grid(True)

# Plot Positions (m)
plt.subplot(3, 3, 7)
# plt.figure()
print(positions)
plt.plot(time, positions[:,0], label='X Position (m)')
plt.plot(time, positions[:,1], label='Y Position (m)')
plt.plot(time, positions[:,2], label='Z Position (m)')
plt.xlabel('Time (s)')
plt.ylabel('Position (cm)')
plt.title('Position vs Time (with Gravity Removed)')
# plt.legend()
plt.grid(True)

pos = positions

# Plot Velocities (m/s)
plt.subplot(3, 3, 4)
# plt.figure()
plt.plot(time, velocities[:,0], label='X Velocity (m/s)')
plt.plot(time, velocities[:,1], label='Y Velocity (m/s)')
plt.plot(time, velocities[:,2], label='Z Velocity (m/s)')
plt.xlabel('Time (s)')
plt.ylabel('Velocities (m/s)')
plt.title('Velocities vs Time (with Gravity Removed)')
# plt.legend()
plt.grid(True)

# Plot XY projection
plt.subplot(3, 3, 3)
# plt.figure()
plt.plot(pos[:,0], pos[:,1], marker='o')
plt.xlabel('X (cm)')
plt.ylabel('Y (cm)')
plt.title('XY Projection')
plt.axis('equal')
plt.grid(True)

# Plot XZ projection
plt.subplot(3, 3, 6)
# plt.figure()
plt.plot(pos[:,0], pos[:,2], marker='o')
plt.xlabel('X (cm)')
plt.ylabel('Z (cm)')
plt.title('XZ Projection')
plt.axis('equal')
plt.grid(True)

# Plot YZ projection
plt.subplot(3, 3, 9)
# plt.figure()
plt.plot(pos[:,1], pos[:,2], marker='o')
plt.xlabel('Y (cm)')
plt.ylabel('Z (cm)')
plt.title('YZ Projection')
plt.axis('equal')
plt.grid(True)

plt.show()