import numpy as np
import math


def matr(coordinates: np.ndarray, connectivity: np.ndarray):
    num_nodes = coordinates.size // 2
    num_elem = connectivity.size // 3
    # количество узлов и количество элементов
    # q = np.array([[1/6, 1/6], [2/3, 1/6], [1/6, 2/3]])
    w = np.array([1 / 6, 1 / 6, 1 / 6])

    # qi = np.empty((9, 2))
    wi = np.empty((9, 1))
    for i in range(9):
        wi[i] = (1 / 6) * (1 / 6)

    # функции формы для треугольных элементов
    kmatr = np.zeros((num_nodes * 2, num_nodes * 2))
    # матрица жесткости
    for m in range(num_elem):
        nodes = connectivity[m]
        c = coordinates[nodes]
        sta = math.sqrt((c[0][0] - c[1][0]) * (c[0][0] - c[1][0]) + (c[0][1] - c[1][1]) * (c[0][1] - c[1][1]))
        stb = math.sqrt((c[1][0] - c[2][0]) * (c[1][0] - c[2][0]) + (c[1][1] - c[2][1]) * (c[1][1] - c[2][1]))
        stc = math.sqrt((c[2][0] - c[0][0]) * (c[2][0] - c[0][0]) + (c[2][1] - c[0][1]) * (c[2][1] - c[0][1]))
        p = (sta + stb + stc) / 2
        pl = math.sqrt(p * (p - sta) * (p - stb) * (p - stc))
        b = np.array([[c[1][1] - c[2][1], 0, c[2][1] - c[0][1], 0, c[0][1] - c[1][1], 0],
                      [0, c[2][0] - c[1][0], 0, c[0][0] - c[2][0], 0, c[1][0] - c[0][0]],
                      [c[2][0] - c[1][0], c[1][1] - c[2][1], c[0][0] - c[2][0], c[2][1] - c[0][1], c[1][0] - c[0][0],
                       c[0][1] - c[1][1]]])
        b = b / (2 * pl)
        d = np.array([[2 * 10 ** 7 * 0.75 / (1.25 * 0.5), 2 * 10 ** 7 * 0.25 / (1.25 * 0.5 * 0.75), 0],
                      [2 * 10 ** 7 * 0.25 / (1.25 * 0.5 * 0.75), 2 * 10 ** 7 * 0.75 / (1.25 * 0.5), 0],
                      [0, 0, 2 * 10 ** 7 / (2 * 1.5)]])
        slagaemoe_k = np.dot(b.transpose(), d)
        slagaemoe_k = np.dot(slagaemoe_k, b)
        kel = slagaemoe_k * wi[0] * 9
        for i in range(3):
            for j in range(3):
                kmatr[nodes[i] * 2, nodes[j] * 2] = kmatr[nodes[i] * 2, nodes[j] * 2] + kel[i * 2, j * 2]
                kmatr[nodes[i] * 2, nodes[j] * 2 + 1] = kmatr[nodes[i] * 2, nodes[j] * 2 + 1] + kel[i * 2, j * 2 + 1]
                kmatr[nodes[i] * 2 + 1, nodes[j] * 2] = kmatr[nodes[i] * 2 + 1, nodes[j] * 2] + kel[i * 2 + 1, j * 2]
                kmatr[nodes[i] * 2 + 1, nodes[j] * 2 + 1] = kmatr[nodes[i] * 2 + 1, nodes[j] * 2 + 1] + kel[
                    i * 2 + 1, j * 2 + 1]

    f = np.zeros(num_nodes * 2)
    # матрица правых частей
    u = np.zeros(num_nodes * 2)
    # матрица узловых перемещений

    for m in range(num_elem):
        nodes = connectivity[m]
        c = coordinates[nodes]
        fel = np.array([0, 0, 0, 0, 0, 0])
        if (c[0][0] == -10) and (c[1][0] == -10):
            fel[0] = -22000 * math.fabs(c[0][1] - c[1][1])
            fel[2] = -22000 * math.fabs(c[0][1] - c[1][1])
            # f[nodes[0] * 2] = f[nodes[0] * 2] + fel[0]
            f[nodes[0] * 2] = fel[0]
            # f[nodes[1] * 2] = f[nodes[0] * 2] + fel[2]
            f[nodes[1] * 2] = fel[2]
        if (c[1][0] == -10) and (c[2][0] == -10):
            fel[2] = -22000 * math.fabs(c[1][1] - c[2][1])
            fel[4] = -22000 * math.fabs(c[1][1] - c[2][1])
            # f[nodes[1] * 2] = f[nodes[1] * 2] + fel[2]
            f[nodes[1] * 2] = fel[2]
            # f[nodes[2] * 2] = f[nodes[2] * 2] + fel[4]
            f[nodes[2] * 2] = fel[4]
        if (c[2][0] == -10) and (c[0][0] == -10):
            fel[0] = -22000 * math.fabs(c[2][1] - c[0][1])
            fel[4] = -22000 * math.fabs(c[2][1] - c[0][1])
            # f[nodes[0] * 2] = f[nodes[0] * 2] + fel[0]
            f[nodes[0] * 2] = fel[0]
            # f[nodes[2] * 2] = f[nodes[2] * 2] + fel[4]
            f[nodes[2] * 2] = fel[4]

    for m in range(num_elem):
        nodes = connectivity[m]
        c = coordinates[nodes]
        fel = np.array([0, 0, 0, 0, 0, 0])
        if (c[0][0] == 30) and (c[1][0] == 30):
            fel[0] = 44000 * math.fabs(c[0][1] - c[1][1])
            fel[2] = 44000 * math.fabs(c[0][1] - c[1][1])
            f[nodes[0] * 2] = fel[0]
            f[nodes[1] * 2] = fel[2]
        if (c[1][0] == 30) and (c[2][0] == 30):
            fel[2] = 44000 * math.fabs(c[1][1] - c[2][1])
            fel[4] = 44000 * math.fabs(c[1][1] - c[2][1])
            f[nodes[1] * 2] = fel[2]
            f[nodes[2] * 2] = fel[4]
        if (c[2][0] == 30) and (c[0][0] == 30):
            fel[0] = 44000 * math.fabs(c[2][1] - c[0][1])
            fel[4] = 44000 * math.fabs(c[2][1] - c[0][1])
            f[nodes[0] * 2] = fel[0]
            f[nodes[2] * 2] = fel[4]

    for i in range(num_nodes):
        if coordinates[i][1] == 0:
            kmatr[i, ] = 0
            kmatr[:, i] = 0
            kmatr[i, i] = 1
            f[i] = 0

    u = np.linalg.solve(kmatr, f)
    ux = np.zeros(num_nodes)
    uy = np.zeros(num_nodes)
    for i in range(num_nodes):
        ux[i] = u[i * 2]
        uy[i] = u[i * 2 + 1]
    for i in range(num_nodes):
        coordinates[i][0] = coordinates[i][0] + ux[i]
        coordinates[i][1] = coordinates[i][1] + uy[i]

    deformmatr = np.zeros((num_elem, 3))
    # матрица деформаций
    naprmatr = np.zeros((num_elem, 3))
    # матрица напряжений
    for m in range(num_elem):
        nodes = connectivity[m]
        c = coordinates[nodes]
        uloc = [ux[nodes[0]], uy[nodes[0]], ux[nodes[1]], uy[nodes[1]], ux[nodes[2]], uy[nodes[2]]]
        sta = math.sqrt((c[0][0] - c[1][0]) * (c[0][0] - c[1][0]) + (c[0][1] - c[1][1]) * (c[0][1] - c[1][1]))
        stb = math.sqrt((c[1][0] - c[2][0]) * (c[1][0] - c[2][0]) + (c[1][1] - c[2][1]) * (c[1][1] - c[2][1]))
        stc = math.sqrt((c[2][0] - c[0][0]) * (c[2][0] - c[0][0]) + (c[2][1] - c[0][1]) * (c[2][1] - c[0][1]))
        p = (sta + stb + stc) / 2
        pl = math.sqrt(p * (p - sta) * (p - stb) * (p - stc))
        b = np.array([[c[1][1] - c[2][1], 0, c[2][1] - c[0][1], 0, c[0][1] - c[1][1], 0],
                      [0, c[2][0] - c[1][0], 0, c[0][0] - c[2][0], 0, c[1][0] - c[0][0]],
                      [c[2][0] - c[1][0], c[1][1] - c[2][1], c[0][0] - c[2][0], c[2][1] - c[0][1], c[1][0] - c[0][0],
                       c[0][1] - c[1][1]]])
        b = b / (2 * pl)
        d = np.array([[2 * 10 ** 7 * 0.75 / (1.25 * 0.5), 2 * 10 ** 7 * 0.25 / (1.25 * 0.5 * 0.75), 0],
                      [2 * 10 ** 7 * 0.25 / (1.25 * 0.5 * 0.75), 2 * 10 ** 7 * 0.75 / (1.25 * 0.5), 0],
                      [0, 0, 2 * 10 ** 7 / (2 * 1.5)]])
        deform = np.dot(b, uloc)
        napr = np.dot(d, deform)
        for i in range(3):
            deformmatr[m][i] = deform[i]
            naprmatr[m][i] = napr[i]

    naprxx = np.zeros(num_elem)
    napryy = np.zeros(num_elem)
    naprxy = np.zeros(num_elem)
    # напряжения по всем направлениям
    for i in range(num_elem):
        naprxx[i] = naprmatr[i][0]
        napryy[i] = naprmatr[i][1]
        naprxy[i] = naprmatr[i][2]

    return naprxx, napryy, naprxy


def max_napr(napr: np.ndarray) -> float:
    a = np.max(np.abs(napr))
    print(a)
    return a
    # ищу максимальное напряжений
