from .lsr_parser_here import LSRFile
from .lsr_parser_here import Layer
from .parsed_lsr import ParsedLSR


# Функция, принимающая две строки - пути до двух файлов, и соединяющая их в лоб
# Т.е. лучше всего использовать, когда есть уверенность, что файлы норм
# Алгоритм разрешения ошибок:
# 1. Если разная высота слоев - приводится к минимальной
# 2. Если разное количество слоев - соединится минимальное количество этих слоев. Остальные просто отбросятся
def risky_connect_two_files(first_lsr_file_path: str, second_lsr_file_path: str) -> ParsedLSR:
    first_lsr_file = LSRFile(first_lsr_file_path)
    second_lsr_file = LSRFile(second_lsr_file_path)
    return connect_two_files(first_lsr_file, second_lsr_file)


# Функция, принимающая два LSRFile - уже распарсенные файлы.
# Алгоритм разрешения ошибок:
# 1. Если разная высота слоев - приводится к минимальной
# 2. Если разное количество слоев - соединится минимальное количество этих слоев. Остальные просто отбросятся
def connect_two_files(first_lsr_file: LSRFile, second_lsr_file: LSRFile) -> ParsedLSR:
    first_layers_lenght = len(first_lsr_file.layers)
    second_layers_lenght = len(second_lsr_file.layers)
    connect_range = min(first_layers_lenght, second_layers_lenght)  # 1. Выбирается минимальное кол-во слоев для итерации
    result = []

    for i in range(0, connect_range):  # Послойная итерация
        first_file_layer = first_lsr_file.layers[i]
        second_file_layer = second_lsr_file.layers[i]
        if first_file_layer.height != second_file_layer.height:  # 2. Если высоты разные, то приводится к минимальной
            resolve_height_difference(first_file_layer, second_file_layer)
        bead_list = []
        for bead in first_file_layer.beads:  # Проход по контурам слоя первого файла
            bead_list.append(bead.bead_coords)
        for bead in second_file_layer.beads:  # Проход по контурам слоя второго файла
            bead_list.append(bead.bead_coords)
        result.append(bead_list)  # Добавление листа, соответствующего слою, с листом контуров

    return ParsedLSR(result)


# Функция, проверяющая, можно ли соединять файлы. Возвращает:
# 0 - если проблем не найдено
# 1 - если есть несовпадения по высоте слоев
# 2 - если разное количество слоев
# 3 - если и то, и другое
# Можно передать print_errors=True, тогда будет лог ошибок в консоль
def check_joinable(first_lsr_file: LSRFile, second_lsr_file: LSRFile, print_errors: bool = False) -> int:
    first_layers = first_lsr_file.layers
    second_layers = second_lsr_file.layers
    warn_layer_length_flag = False
    warn_x3_diff_flag = False

    iter_range = len(first_layers)
    if len(first_layers) != len(
            second_layers):  # Определение, до какого слоя итерироваться (т.к. слоев может быть разное кол-во)
        warn_layer_length_flag = True
        iter_range = min(len(first_layers), len(second_layers))  # Выбор минимального
        if print_errors:
            print(
                f"WARN: количество слоев не совпадают\nFirst File: {len(first_layers)}\nSecond File: {len(second_layers)}")

    for i in range(0, iter_range):  # Проверка высоты слоев
        if first_layers[i].height != second_layers[i].height:
            if print_errors:
                print(f"Слой {i}. {first_layers[i].height} != {second_layers[i].height}")
            warn_x3_diff_flag = True

    if print_errors and warn_layer_length_flag:
        print(
            f"WARN: количество слоев не совпадают\nFirst File: {len(first_layers)}\nSecond File: {len(second_layers)}")

    if (not warn_x3_diff_flag) and (not warn_layer_length_flag):
        if print_errors:
            print("Все отлично! Все координаты совпадают")
        return 0

    if warn_layer_length_flag and warn_x3_diff_flag:
        return 3
    if warn_layer_length_flag:
        return 2
    if warn_x3_diff_flag:
        return 1


def resolve_height_difference(first_file_layer: Layer, second_file_layer: Layer) -> None:
    min_height = min(first_file_layer.height, second_file_layer.height)
    if first_file_layer.height < second_file_layer.height:
        second_file_layer.set_height(min_height)
    else:
        first_file_layer.set_height(min_height)
