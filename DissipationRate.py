import numpy as np


def dis_compute(ut_array, vt_array, delta, nu, uv_size):
    udx = np.zeros(uv_size)
    vdz = np.zeros(uv_size)

    for i in range(2, uv_size[0]):
        for j in range(2, uv_size[1]):
            vdz[i, j, :] = (3 * vt_array[i, j, :]
                            - 4 * vt_array[i - 1, j, :]
                            + vt_array[i - 2, j, :]) / (2 * delta)
            udx[i, j, :] = (3 * ut_array[i, j, :]
                            - 4 * ut_array[i, j - 1, :]
                            + ut_array[i, j - 2, :]) / (2 * delta)
    udx[:, 0:1, :] = (-3 * ut_array[:, 0:1, :]
                      + 4 * ut_array[:, 1:2, :]
                      - ut_array[:, 2:3, :]) / (2 * delta)
    vdz[0:1, :, :] = (-3 * vt_array[0:1, :, :]
                      - 4 * vt_array[1:2, :, :]
                      + vt_array[2:3, :, :]) / (2 * delta)
    dis = 4 * nu * (udx ** 2 + vdz ** 2 + udx * vdz +
                    3 * ((udx + vdz) ** 2) / 4)

    return dis
