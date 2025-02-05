"""
All data is here. Data under the variable "data" is imported to the other file.
So current data you want to test should be assigned "data" as var.
This is like a cache of data that we want to switch around between. Long term
data files should be kept in the /data folder as .txt files.
"""

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

# this is the data from arduino with .1
data = """ 
Acceleration X: 8.38, Y: -5.02, Z: 1.80 m/s^2
Rotation X: -0.07, Y: -0.01, Z: 0.02 rad/s
Temperature: 31.94 degC

Acceleration X: 8.39, Y: -5.05, Z: 1.74 m/s^2
Rotation X: -0.08, Y: -0.04, Z: 0.06 rad/s
Temperature: 31.96 degC

Acceleration X: 8.40, Y: -5.04, Z: 1.80 m/s^2
Rotation X: -0.06, Y: -0.03, Z: 0.05 rad/s
Temperature: 31.98 degC

Acceleration X: 8.35, Y: -5.08, Z: 1.79 m/s^2
Rotation X: -0.07, Y: -0.04, Z: 0.06 rad/s
Temperature: 31.99 degC

Acceleration X: 8.37, Y: -5.13, Z: 1.78 m/s^2
Rotation X: -0.10, Y: -0.01, Z: 0.05 rad/s
Temperature: 32.00 degC

Acceleration X: 8.42, Y: -5.14, Z: 1.77 m/s^2
Rotation X: -0.11, Y: -0.01, Z: 0.06 rad/s
Temperature: 32.02 degC

Acceleration X: 8.38, Y: -5.19, Z: 1.85 m/s^2
Rotation X: -0.06, Y: 0.06, Z: 0.06 rad/s
Temperature: 32.04 degC

Acceleration X: 8.30, Y: -5.24, Z: 1.84 m/s^2
Rotation X: -0.00, Y: 0.16, Z: 0.14 rad/s
Temperature: 32.06 degC

Acceleration X: 8.03, Y: -5.39, Z: 2.21 m/s^2
Rotation X: -0.07, Y: 0.06, Z: 0.12 rad/s
Temperature: 32.06 degC

Acceleration X: 8.21, Y: -5.29, Z: 1.93 m/s^2
Rotation X: -0.06, Y: 0.06, Z: 0.11 rad/s
Temperature: 32.10 degC

Acceleration X: 7.75, Y: -5.35, Z: 2.31 m/s^2
Rotation X: -0.02, Y: 0.03, Z: 0.15 rad/s
Temperature: 32.11 degC

Acceleration X: 8.03, Y: -5.43, Z: 2.06 m/s^2
Rotation X: -0.06, Y: -0.02, Z: 0.02 rad/s
Temperature: 32.12 degC

Acceleration X: 7.91, Y: -5.48, Z: 2.30 m/s^2
Rotation X: -0.08, Y: -0.03, Z: 0.04 rad/s
Temperature: 32.14 degC

Acceleration X: 8.09, Y: -5.52, Z: 2.18 m/s^2
Rotation X: -0.05, Y: -0.04, Z: 0.11 rad/s
Temperature: 32.16 degC

Acceleration X: 8.20, Y: -6.06, Z: 2.68 m/s^2
Rotation X: -0.07, Y: 0.13, Z: 0.31 rad/s
Temperature: 32.17 degC

Acceleration X: 7.50, Y: -5.97, Z: 2.60 m/s^2
Rotation X: -0.21, Y: 0.12, Z: 0.30 rad/s
Temperature: 32.19 degC

Acceleration X: 7.42, Y: -6.57, Z: 3.30 m/s^2
Rotation X: -0.50, Y: -0.25, Z: 0.08 rad/s
Temperature: 32.20 degC

Acceleration X: 7.81, Y: -6.16, Z: 1.24 m/s^2
Rotation X: -0.43, Y: -0.14, Z: 0.25 rad/s
Temperature: 32.19 degC

Acceleration X: 7.49, Y: -6.19, Z: 0.85 m/s^2
Rotation X: -0.50, Y: -0.30, Z: 0.21 rad/s
Temperature: 32.21 degC

Acceleration X: 6.94, Y: -6.70, Z: 1.09 m/s^2
Rotation X: -0.32, Y: -0.12, Z: 0.28 rad/s
Temperature: 32.23 degC
"""

# .1 dt, standing completely sitll
data = """
Acceleration X: 87.03, Y: 12.28, Z: -7.10 m/s^2
Rotation X: 0.58, Y: 0.77, Z: 0.77 rad/s
Temperature: 50.08 degC

Acceleration X: -155.68, Y: -77.23, Z: 23.29 m/s^2
Rotation X: 5.18, Y: 5.18, Z: 0.20 rad/s
Temperature: 65.89 degC

Acceleration X: -155.68, Y: -77.23, Z: 23.29 m/s^2
Rotation X: 5.45, Y: 0.20, Z: -0.20 rad/s
Temperature: 65.89 degC

Acceleration X: -155.68, Y: -77.23, Z: 0.10 m/s^2
Rotation X: 5.45, Y: 5.45, Z: 0.20 rad/s
Temperature: 105.80 degC

Acceleration X: -155.68, Y: -77.23, Z: 24.52 m/s^2
Rotation X: 0.02, Y: 9.74, Z: -0.20 rad/s
Temperature: 67.40 degC

Acceleration X: -155.68, Y: -77.23, Z: 0.10 m/s^2
Rotation X: 5.72, Y: 0.20, Z: -0.20 rad/s
Temperature: 75.68 degC

Acceleration X: -155.68, Y: -77.23, Z: 0.10 m/s^2
Rotation X: 5.72, Y: 11.92, Z: -0.20 rad/s
Temperature: -35.75 degC

Acceleration X: -155.68, Y: -77.23, Z: 26.97 m/s^2
Rotation X: 0.00, Y: 5.99, Z: 0.20 rad/s
Temperature: 102.79 degC

Acceleration X: -155.68, Y: -77.23, Z: 26.97 m/s^2
Rotation X: 5.99, Y: 0.20, Z: -0.20 rad/s
Temperature: 36.53 degC

Acceleration X: -155.68, Y: -77.23, Z: 0.11 m/s^2
Rotation X: 6.27, Y: 6.47, Z: -0.20 rad/s
Temperature: 16.20 degC

Acceleration X: -155.68, Y: -77.23, Z: 0.11 m/s^2
Rotation X: 0.02, Y: -22.41, Z: -0.20 rad/s
Temperature: 97.52 degC

Acceleration X: -155.68, Y: -77.23, Z: 28.19 m/s^2
Rotation X: 0.00, Y: 6.54, Z: 26.36 rad/s
Temperature: 36.53 degC

Acceleration X: -155.68, Y: -77.23, Z: 0.11 m/s^2
Rotation X: 6.54, Y: 13.55, Z: -0.17 rad/s
Temperature: 68.15 degC

Acceleration X: -155.68, Y: -77.23, Z: 29.42 m/s^2
Rotation X: 6.54, Y: 6.54, Z: 0.20 rad/s
Temperature: 36.53 degC

Acceleration X: -155.68, Y: -77.23, Z: 30.65 m/s^2
Rotation X: 6.81, Y: 6.81, Z: 0.20 rad/s
Temperature: 74.18 degC

Acceleration X: -155.68, Y: -77.23, Z: 0.12 m/s^2
Rotation X: 0.03, Y: -14.51, Z: -0.20 rad/s
Temperature: 120.11 degC

Acceleration X: -155.68, Y: -77.23, Z: 0.12 m/s^2
Rotation X: 7.08, Y: 14.37, Z: -0.16 rad/s
Temperature: 8.67 degC

Acceleration X: -155.68, Y: -77.23, Z: 31.87 m/s^2
Rotation X: 0.00, Y: 7.08, Z: 29.08 rad/s
Temperature: 75.68 degC

Acceleration X: -155.68, Y: -77.23, Z: 31.87 m/s^2
Rotation X: 7.36, Y: 29.63, Z: -0.20 rad/s
Temperature: 36.53 degC

Acceleration X: -155.68, Y: -77.23, Z: 0.13 m/s^2
Rotation X: 7.36, Y: 0.20, Z: -0.20 rad/s
Temperature: 60.62 degC
"""