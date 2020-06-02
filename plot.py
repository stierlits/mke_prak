import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.tri as tri
import numpy as np


def draw_napr_by_count(counts, naprxx, napryy, naprxy):
    fig, ax0 = plt.subplots(1)

    ax0.plot(counts, naprxx, 'r')
    ax0.plot(napryy, counts, 'g')
    ax0.plot(naprxy, counts, 'b')
    ax0.grid()

    plt.show()
    # рисую график сеточной сходимости на одном графике, красный - хх, зеленый - уу, синий - ху


def draw_grid(coordinates: list, connectivity: list, naprxx: np.ndarray, napryy: np.ndarray, naprxy: np.ndarray):
    fig, (ax0, ax1, ax2) = plt.subplots(3)
    x, y = get_x_y_arrays(coordinates)
    triangulation = get_triangulation(x, y, connectivity)

    set_up_ax(fig, ax0, triangulation, naprxx)
    set_up_ax(fig, ax1, triangulation, napryy)
    set_up_ax(fig, ax2, triangulation, naprxy)

    plt.show()
    # рисую график напряжений


def get_x_y_arrays(coordinates: list):
    n = len(coordinates)
    x = np.empty(n)
    y = np.empty(n)

    for i in range(n):
        x[i] = coordinates[i][0]
        y[i] = coordinates[i][1]

    return x, y
    # создаю массивы х и у отдельно


def get_triangulation(x, y, connectivity: list) -> mpl.tri.Triangulation:
    # noinspection PyTypeChecker
    return tri.Triangulation(x, y, triangles=connectivity)
    # триангуляций


def set_up_ax(fig, ax, triangulation, d: np.ndarray):
    cax = ax.tripcolor(triangulation, facecolors=d, edgecolors='k', cmap=plt.get_cmap('jet'))

    fig.colorbar(cax, ax=ax)
    # раскрашиваю элементы
