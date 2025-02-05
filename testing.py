import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.transform import Rotation as R
import json

def load_config(filename):
    with open(filename, 'r') as file:
        config_data = json.load(file)
    return config_data

config = load_config('config.json')
GLOBAL_DT = config['GLOBAL_DT']

from data_files import data # import data from other file

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

dt = GLOBAL_DT # setting global dt here 
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