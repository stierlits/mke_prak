import pathlib


def read_grid_file(file_name: str):
    with pathlib.Path(file_name).open('r') as f:
        # Пропускаю хедер файла
        for line in f:
            if line == '*NODE\n':
                break
        # Парсим комментарий с индексами колонок
        coordinates_comment = f.readline()
        coordinates_comment_elements = coordinates_comment.split()
        coordinates_comment_elements.remove('$')
        nid_col_index = coordinates_comment_elements.index('nid')
        x_col_index = coordinates_comment_elements.index('x')
        y_col_index = coordinates_comment_elements.index('y')

        # Читаю координаты
        coordinates_raw = []
        for line in f:
            if line == '$\n':
                break
            line_elements = line.split()
            nid = int(line_elements[nid_col_index])
            x = float(line_elements[x_col_index])
            y = float(line_elements[y_col_index])
            coordinates_raw.append((nid, x, y))
        coordinates_raw.sort(key=lambda e: e[0])
        coordinates = [(e[1], e[2]) for e in coordinates_raw]

        # Пропускаю еще комментарии

        for line in f:
            if line == '*ELEMENT_SHELL\n':
                break

        # Читаю матрицу `connectivity`
        connectivity = []
        for line in f:
            if line == '*END\n':
                break
            line_elements = line.split()
            n1 = int(line_elements[2]) - 1
            n2 = int(line_elements[3]) - 1
            n3 = int(line_elements[4]) - 1
            connectivity.append((n1, n2, n3))

    return coordinates, connectivity
