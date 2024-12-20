import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.transform import Rotation as R

data = """
Acceleration X: -1.04, Y: 6.12, Z: 6.79 m/s^2
Rotation X: -0.14, Y: -0.05, Z: 0.03 rad/s
Temperature: 32.38 degC

Acceleration X: -0.93, Y: 6.11, Z: 6.82 m/s^2
Rotation X: 0.03, Y: 0.06, Z: 0.08 rad/s
Temperature: 32.44 degC

Acceleration X: -1.09, Y: 6.39, Z: 6.56 m/s^2
Rotation X: 0.08, Y: 0.03, Z: 0.00 rad/s
Temperature: 32.50 degC

Acceleration X: -1.18, Y: 6.58, Z: 6.34 m/s^2
Rotation X: -0.10, Y: -0.04, Z: 0.04 rad/s
Temperature: 32.55 degC

Acceleration X: -1.13, Y: 6.54, Z: 6.39 m/s^2
Rotation X: -0.05, Y: -0.04, Z: 0.02 rad/s
Temperature: 32.60 degC

Acceleration X: -1.11, Y: 6.56, Z: 6.39 m/s^2
Rotation X: -0.06, Y: -0.01, Z: 0.03 rad/s
Temperature: 32.64 degC

Acceleration X: -1.13, Y: 6.58, Z: 6.38 m/s^2
Rotation X: -0.05, Y: -0.01, Z: 0.02 rad/s
Temperature: 32.67 degC

Acceleration X: -1.28, Y: 6.68, Z: 6.24 m/s^2
Rotation X: -0.01, Y: 0.06, Z: 0.03 rad/s
Temperature: 32.71 degC

Acceleration X: -1.94, Y: 6.32, Z: 6.34 m/s^2
Rotation X: -0.17, Y: 0.27, Z: -0.00 rad/s
Temperature: 32.75 degC

Acceleration X: -0.62, Y: 2.14, Z: 8.87 m/s^2
Rotation X: -0.33, Y: -0.09, Z: -0.10 rad/s
Temperature: 32.79 degC

Acceleration X: -0.43, Y: 1.86, Z: 8.96 m/s^2
Rotation X: -0.09, Y: -0.02, Z: 0.06 rad/s
Temperature: 32.78 degC

Acceleration X: -0.38, Y: 2.01, Z: 8.94 m/s^2
Rotation X: 0.03, Y: -0.03, Z: 0.07 rad/s
Temperature: 32.75 degC

Acceleration X: -0.48, Y: 6.51, Z: 6.54 m/s^2
Rotation X: 0.80, Y: 0.02, Z: -0.02 rad/s
Temperature: 32.71 degC

Acceleration X: -1.48, Y: 8.46, Z: 4.27 m/s^2
Rotation X: 0.11, Y: -0.09, Z: 0.06 rad/s
Temperature: 32.71 degC

Acceleration X: -0.13, Y: 7.78, Z: 4.70 m/s^2
Rotation X: -0.19, Y: -0.18, Z: 0.08 rad/s
Temperature: 32.77 degC

Acceleration X: 1.40, Y: 8.07, Z: 4.63 m/s^2
Rotation X: -0.07, Y: -0.25, Z: 0.17 rad/s
Temperature: 32.82 degC

Acceleration X: 2.54, Y: 8.07, Z: 4.17 m/s^2
Rotation X: -0.07, Y: -0.26, Z: 0.24 rad/s
Temperature: 32.82 degC

Acceleration X: 3.46, Y: 7.75, Z: 3.86 m/s^2
Rotation X: -0.06, Y: -0.08, Z: 0.21 rad/s
Temperature: 32.84 degC

Acceleration X: 5.70, Y: 6.84, Z: 3.65 m/s^2
Rotation X: -0.23, Y: -0.62, Z: 0.57 rad/s
Temperature: 32.85 degC

Acceleration X: 7.60, Y: 5.27, Z: 3.01 m/s^2
Rotation X: -0.15, Y: -0.19, Z: 0.17 rad/s
Temperature: 32.87 degC

Acceleration X: 7.01, Y: 5.85, Z: 3.92 m/s^2
Rotation X: -0.10, Y: 0.36, Z: -0.19 rad/s
Temperature: 32.88 degC

Acceleration X: 5.75, Y: 6.02, Z: 4.77 m/s^2
Rotation X: -0.12, Y: 0.11, Z: -0.10 rad/s
Temperature: 32.90 degC

Acceleration X: 4.80, Y: 6.48, Z: 6.22 m/s^2
Rotation X: -0.11, Y: 0.34, Z: -0.14 rad/s
Temperature: 32.91 degC

Acceleration X: 3.26, Y: 6.22, Z: 6.53 m/s^2
Rotation X: -0.08, Y: 0.29, Z: -0.21 rad/s
Temperature: 32.96 degC

Acceleration X: 0.93, Y: 6.77, Z: 6.37 m/s^2
Rotation X: 0.06, Y: 0.22, Z: -0.31 rad/s
Temperature: 32.96 degC

Acceleration X: -0.30, Y: 7.19, Z: 5.97 m/s^2
Rotation X: -0.23, Y: -0.15, Z: 0.14 rad/s
Temperature: 32.97 degC
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
gravity_vector = (initial_acc / norm_g) * 9.80665

positions = [np.zeros(3)]
velocities = [np.zeros(3)]

# Orientation tracking:
# Start with identity orientation
current_orientation = R.from_euler('xyz', [0,0,0], degrees=False)
orientations = [current_orientation]

for i in range(1, num_samples):
    # Remove gravity
    acc_linear = accelerations[i] - gravity_vector

    # Integrate for velocity and position
    v = velocities[-1] + acc_linear * dt
    p = positions[-1] + v * dt

    velocities.append(v)
    positions.append(p)

    # Orientation update:
    # Integrate gyro (in rad/s) over dt to get rotation vector
    omega = rotations[i]  # [gx, gy, gz]
    delta_theta = omega * dt  # small rotation
    delta_rotation = R.from_rotvec(delta_theta)
    current_orientation = orientations[-1] * delta_rotation
    orientations.append(current_orientation)

positions = np.array(positions)
time = np.arange(num_samples)*dt

# Extract Euler angles (roll, pitch, yaw)
euler_angles = []
for o in orientations:
    # 'xyz' convention: roll around X, pitch around Y, yaw around Z
    euler = o.as_euler('xyz', degrees=True)  # in degrees
    euler_angles.append(euler)
euler_angles = np.array(euler_angles)
roll = euler_angles[:,0]
pitch = euler_angles[:,1]
yaw = euler_angles[:,2]

# Plot raw accelerations (m/s²)
plt.figure()
plt.plot(time, accelerations[:,0], label='Ax (m/s²)')
plt.plot(time, accelerations[:,1], label='Ay (m/s²)')
plt.plot(time, accelerations[:,2], label='Az (m/s²)')
plt.title('Raw Accelerations')
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (m/s²)')
plt.legend()
plt.grid(True)

# Plot Roll, Pitch, Yaw
plt.figure()
plt.plot(time, roll, label='Roll (deg)')
plt.plot(time, pitch, label='Pitch (deg)')
plt.plot(time, yaw, label='Yaw (deg)')
plt.title('Roll, Pitch, Yaw vs Time')
plt.xlabel('Time (s)')
plt.ylabel('Angle (degrees)')
plt.legend()
plt.grid(True)

# Plot Positions (cm)
plt.figure()
plt.plot(time, positions[:,0], label='X Position (m)')
plt.plot(time, positions[:,1], label='Y Position (m)')
plt.plot(time, positions[:,2], label='Z Position (m)')
plt.xlabel('Time (s)')
plt.ylabel('Position (cm)')
plt.title('Position vs Time (with Gravity Removed)')
plt.legend()
plt.grid(True)

plt.show()