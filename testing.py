import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.transform import Rotation as R

# Sample data (use your actual data)
data = """
aX = -6096 | aY = 96 | aZ = 13780 | gX = -532 | gY = 361 | gZ = 302
aX = -6172 | aY = 160 | aZ = 13812 | gX = -497 | gY = 99 | gZ = 273
aX = -6456 | aY = 152 | aZ = 13640 | gX = -566 | gY = 2264 | gZ = 241
aX = -6828 | aY = -68 | aZ = 13284 | gX = -366 | gY = 95 | gZ = -373
aX = -6816 | aY = -32 | aZ = 13544 | gX = -394 | gY = -952 | gZ = 193
aX = -7160 | aY = 1844 | aZ = 13312 | gX = -641 | gY = 378 | gZ = 510
aX = -6924 | aY = 2412 | aZ = 13540 | gX = -407 | gY = 363 | gZ = 854
aX = -6932 | aY = -1720 | aZ = 13424 | gX = -536 | gY = -1625 | gZ = 92
aX = -6348 | aY = -276 | aZ = 13476 | gX = -470 | gY = -406 | gZ = 136
aX = -6968 | aY = -328 | aZ = 13376 | gX = -601 | gY = 1555 | gZ = -118
aX = -7160 | aY = 4 | aZ = 13152 | gX = -498 | gY = 365 | gZ = 309
aX = -7356 | aY = 148 | aZ = 13136 | gX = -442 | gY = 365 | gZ = 296
"""

# Define scaling factors
ACCEL_SCALE = 1 / 32768.0  # ±2g range
GYRO_SCALE = 250 / 32768.0 # ±250°/s range
G_CONVERSION = 9.80665

accelerometer_data = []
gyroscope_data = []

for line in data.strip().split('\n'):
    parts = line.strip().split('|')
    ax_raw = float(parts[0].split('=')[1])
    ay_raw = float(parts[1].split('=')[1])
    az_raw = float(parts[2].split('=')[1])
    gx_raw = float(parts[3].split('=')[1])
    gy_raw = float(parts[4].split('=')[1])
    gz_raw = float(parts[5].split('=')[1])

    # Convert raw accelerometer data to m/s²
    ax = ax_raw * ACCEL_SCALE * G_CONVERSION
    ay = ay_raw * ACCEL_SCALE * G_CONVERSION
    az = az_raw * ACCEL_SCALE * G_CONVERSION

    # Convert raw gyroscope data to rad/s
    gx = np.deg2rad(gx_raw * GYRO_SCALE)
    gy = np.deg2rad(gy_raw * GYRO_SCALE)
    gz = np.deg2rad(gz_raw * GYRO_SCALE)

    accelerometer_data.append([ax, ay, az])
    gyroscope_data.append([gx, gy, gz])

accelerometer_data = np.array(accelerometer_data)
gyroscope_data = np.array(gyroscope_data)

num_samples = len(accelerometer_data)
dt = 0.5  # seconds

# Initial orientation estimate based on gravity:
acc_initial = accelerometer_data[0]
acc_initial_normalized = acc_initial / np.linalg.norm(acc_initial)
g_fixed = np.array([0, 0, 9.80665])
g_fixed_normalized = g_fixed / np.linalg.norm(g_fixed)

# Align sensor Z-axis with gravity (assuming no initial rotation about gravity axis)
initial_orientation = R.align_vectors([g_fixed_normalized], [acc_initial_normalized])[0]

orientations = [initial_orientation]
positions = [np.zeros(3)]
velocities = [np.zeros(3)]

for i in range(1, num_samples):
    # Update orientation from gyro (this is simplistic and will drift)
    omega = gyroscope_data[i]
    delta_theta = omega * dt
    delta_rotation = R.from_rotvec(delta_theta)
    current_orientation = orientations[-1] * delta_rotation
    orientations.append(current_orientation)

    # Rotate accelerometer reading into fixed frame
    acc_body = accelerometer_data[i]
    acc_fixed_frame = current_orientation.apply(acc_body)

    # Subtract gravity
    acc_linear = acc_fixed_frame - g_fixed

    # Integrate acceleration to get velocity and position
    v = velocities[-1] + acc_linear * dt
    p = positions[-1] + v * dt

    velocities.append(v)
    positions.append(p)

positions = np.array(positions)
time = np.arange(num_samples)*dt

# Plot raw accelerometer data
fig_a = plt.figure()
ax_a = fig_a.add_subplot(111)
ax_a.plot(time, accelerometer_data[:,0], label='Ax (m/s²)')
ax_a.plot(time, accelerometer_data[:,1], label='Ay (m/s²)')
ax_a.plot(time, accelerometer_data[:,2], label='Az (m/s²)')
ax_a.set_title("Accelerometer Data")
ax_a.set_xlabel('Time (s)')
ax_a.set_ylabel('Acceleration (m/s²)')
ax_a.legend()

# Plot raw gyroscope data
fig_g = plt.figure()
ax_g = fig_g.add_subplot(111)
ax_g.plot(time, gyroscope_data[:,0], label='Gx (rad/s)')
ax_g.plot(time, gyroscope_data[:,1], label='Gy (rad/s)')
ax_g.plot(time, gyroscope_data[:,2], label='Gz (rad/s)')
ax_g.set_title("Gyroscope Data")
ax_g.set_xlabel('Time (s)')
ax_g.set_ylabel('Angular Velocity (rad/s)')
ax_g.legend()

# Plot the integrated positions (Keep in mind these will likely drift!)
fig_p = plt.figure()
ax_p = fig_p.add_subplot(111, projection='3d')
ax_p.plot(positions[:,0], positions[:,1], positions[:,2], marker='o')
ax_p.set_xlabel('X (m)')
ax_p.set_ylabel('Y (m)')
ax_p.set_zlabel('Z (m)')
ax_p.set_title("Estimated Trajectory (Likely with Drift)")

plt.show()