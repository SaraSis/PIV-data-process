# Needed open source library
from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt
# Needed self code
from Smooth import smooth
from DissipationRate import dis_compute

FilePath =                  # input the path of mat file, such as 'I:\\数据分析结果\\PIVlab\\D=5\\14+6'
FileName =                  # input the filename, such as '11.mat'
Data = loadmat(FilePath + '\\' + FileName)

# Initialization
# TimeLength defines the file length in time
# use TimeLength[1]
# FieldSize defines the width and height in space
# FieldSize[0] = height, FieldSize[1] = width
TimeLength = np.shape(Data['u_original'])
FieldSize = np.shape(Data['u_original'][0][0])
ArraySize = (FieldSize[0], FieldSize[1], TimeLength[0])

# Extract the velocity at selected point
# u, v are the 3-d arrays to store velocity data
u = np.zeros(ArraySize)
v = np.zeros(ArraySize)

for i in range(TimeLength[0]):
    u[:, :, i] = Data['u_original'][i][0]
    v[:, :, i] = Data['v_original'][i][0]

# Calculate the time-averaged velocity using by moving average
# us, vs represent the time-averaged velocity
# smooth is an user-defined function in smooth.py
us = np.zeros(ArraySize)
vs = np.zeros(ArraySize)
for i in range(FieldSize[0]):
    for j in range(FieldSize[1]):
        us[i, j, :] = smooth(u[i, j, :], TimeLength[0], 15)
        vs[i, j, :] = smooth(v[i, j, :], TimeLength[0], 15)

# ut, vt represent the turbulent velocity
ut = u - us
vt = v - vs

# An example shown below
# Calculate the turbulent kinetic energy dissipation rate
delta = Data['x'][0][0][0][1]-Data['x'][0][0][0][0]  # grid step distance
nu = 1.01E-6                                         # kinetic viscosity
Dissipation = dis_compute(ut, vt, delta, nu, ArraySize)

# Results visualization
plt.imshow(Dissipation[:, :, 900])
plt.show()
