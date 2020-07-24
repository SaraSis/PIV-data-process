import numpy as np


# input array is a 1-d array
def smooth(u_array, length, window):
    us_array = np.zeros(length)

    for k in range(length):
        if int(window / 2) < k < length - int(window / 2):
            us_array[k] \
                = np.mean(u_array[k - int(window / 2):k + int(window / 2)])
        else:
            us_array[k] = u_array[k]

    return us_array
