import numpy as np

import file_reader
import matr
import plot


def calc_and_draw(file_name):
    coordinates, connectivity = file_reader.read_grid_file(file_name)
    # считываю массивы координат и элементов
    # print(len(coordinates))
    # print(len(connectivity))

    naprxx, napryy, naprxy = matr.matr(
        np.array(coordinates), np.array(connectivity),
    )
    # вычисляю напряжения
    plot.draw_grid(coordinates, connectivity, naprxx, napryy, naprxy)
    # рисую график напряжения


def napr_by_count(files):
    n = len(files)

    max_naprxx = np.empty((n,))
    max_napryy = np.empty((n,))
    max_naprxy = np.empty((n,))
    counts = np.empty((n,))

    for i, file_name in enumerate(files):
        coordinates, connectivity = file_reader.read_grid_file(file_name)
        print(len(coordinates))
        print(len(connectivity))

        naprxx, napryy, naprxy = matr.matr(
            np.array(coordinates), np.array(connectivity),
        )

        counts[i] = len(connectivity)
        max_naprxx[i] = matr.max_napr(naprxx)
        max_napryy[i] = matr.max_napr(napryy)
        max_naprxy[i] = matr.max_napr(naprxy)

    plot.draw_napr_by_count(counts, max_naprxx, max_napryy, max_naprxy)
    # ищу максимум по всем напряжениям и рисую график сеточной сходимости


if __name__ == '__main__':
    # calc_and_draw(r'C:\Users\dashk\универ\прак\razb7.k')

    napr_by_count(
        [
            # r'C:\Users\dashk\универ\прак\razb1.k',
            # r'C:\Users\dashk\универ\прак\razb2.k',
            # r'C:\Users\dashk\универ\прак\razb3.k',
            # r'C:\Users\dashk\универ\прак\razb4.k',
            # r'C:\Users\dashk\универ\прак\razb5.k',
            # r'C:\Users\dashk\универ\прак\razb7.k',
            # r'C:\Users\dashk\универ\прак\razb8.k',
            # r'C:\Users\dashk\универ\прак\razb9.k',
            r'C:\Users\dashk\универ\прак\razb10.k',
            r'C:\Users\dashk\универ\прак\razb11.k',
            r'C:\Users\dashk\универ\прак\razb12.k',
            r'C:\Users\dashk\универ\прак\razb13.k',
            r'C:\Users\dashk\универ\прак\razb14.k',
            r'C:\Users\dashk\универ\прак\razb15.k',
            r'C:\Users\dashk\универ\прак\razb16.k',
            r'C:\Users\dashk\универ\прак\razb17.k',
            r'C:\Users\dashk\универ\прак\razb18.k',
            r'C:\Users\dashk\универ\прак\razb19.k',
            r'C:\Users\dashk\универ\прак\razb20.k',
        ]
    )
    # выбираю тут рисоват график напряжений или график сеточной сходимости
