import json
import numpy as np
from copy import deepcopy


# Класс, хранящий результат парсера.

# Позволяет получать результат в различных видах:
# 1. get_as_list() - получить в виде питон-листа
# 2. get_as_json() - получить в виде json-строки. Можно передать все те же необязательные параметры, что и в json.dumps
# Для больших файлов работает с затупом
# 3. get_as_numpy_array() - получить в виде numpy массива. Можно передать False, тогда не будет создаваться deepcopy
# оригинального массива. Увеличивает скорость, но все последующие вызовы get_as_list() и get_as_json()
# будут возвращать массив, форматированный под numpy (частично заполненный None)
# Для больших файлов работает совсем медленно из-за np.array(big_list_of_lists)
# 4. save_into_json_file() - сохранить на диск в .json. Необходимо передать отрытый файл.
# 5. save_as_lsr() - сохранить на диск в .lsr. Необходимо передать отрытый файл.
# Можно передать все те же необязательные параметры, что и в json.dump()

class ParsedLSR:
    python_list_representation: list[list[list[list[float]]]]
    file_strings: list[str]

    def __init__(self, list_of_layers: list, file_strings: list[str]) -> None:
        self.python_list_representation = list_of_layers
        self.file_strings = file_strings

    def __repr__(self) -> str:
        return str(self.python_list_representation)

    def get_as_list(self) -> list[list[list[list[float]]]]:
        return self.python_list_representation

    def get_as_json(self, skipkeys=False, ensure_ascii=True, check_circular=True,
                    allow_nan=True, cls=None, indent=None, separators=None,
                    default=None, sort_keys=False) -> str:
        return json.dumps(self.python_list_representation, skipkeys=skipkeys, ensure_ascii=ensure_ascii,
                          check_circular=check_circular, allow_nan=allow_nan, cls=cls, indent=indent,
                          separators=separators, default=default, sort_keys=sort_keys)

    def save_into_json_file(self, file, skipkeys=False, ensure_ascii=True, check_circular=True,
                            allow_nan=True, cls=None, indent=None, separators=None,
                            default=None, sort_keys=False) -> None:
        json.dump(self.python_list_representation, fp=file, skipkeys=skipkeys, ensure_ascii=ensure_ascii,
                  check_circular=check_circular, allow_nan=allow_nan, cls=cls, indent=indent, separators=separators,
                  default=default, sort_keys=sort_keys)

    # Частично заполняет массив None, т.к. необходимо определить однозначную размерность массива
    # Размерность массива - (макс. кол-во слоев, макс. кол-во контуров, макс. кол-во векторов, 3)
    # Все то, что меньше максимума - дополняется None
    def get_as_numpy_array(self, need_to_deepcopy: bool = True) -> np.ndarray:
        dimention = self.__resolve_array_dimension()  # Работает быстро
        print(dimention)
        new_numpyable_list = self.__create_new_numpyable_list(dimention,
                                                              need_to_deepcopy)  # Работает быстро с затупом на deepcopy
        return np.array(new_numpyable_list)  # Работает медленно

    def __resolve_array_dimension(self) -> tuple:
        layers_count = len(self.python_list_representation)
        bead_count = max(len(layer) for layer in self.python_list_representation)
        beads = []
        for layer in self.python_list_representation:
            for bead in layer:
                beads.append(len(bead))
        bead_coords_count = max(beads)
        coords_count = 3
        return layers_count, bead_count, bead_coords_count, coords_count

    # Не всегда new)
    def __create_new_numpyable_list(self, dimension: tuple, need_to_deepcopy: bool) -> list:
        none_coords = [None, None, None]
        max_beads_in_layer = dimension[1]  # Максимальная длина слоя
        max_beads_coords_in_bead = dimension[2]  # Максимальная длина контура

        if need_to_deepcopy:  # Если нужна deepcopy, то она создается, если нет, используется оригинальный результат
            new_list = deepcopy(self.python_list_representation)
        else:
            new_list = self.python_list_representation

        for i, layer in enumerate(new_list):  # Итерация по слоям. Слой - лист контуров

            if len(layer) < max_beads_in_layer:  # Длина слоя. Если не максимальна:
                layer_difference = max_beads_in_layer - len(layer)
                need_to_extend = self.__create_list_of_empty_beads(layer_difference)
                layer.extend(need_to_extend)  # Дополняется пустыми контурами

            for j, bead in enumerate(layer):  # Итерация по контурам. Контур - лист векторов

                if len(bead) < max_beads_coords_in_bead:  # Длина контура. Если не максимальна:
                    difference = max_beads_coords_in_bead - len(bead)
                    need_to_extend = [none_coords] * difference
                    bead.extend(need_to_extend)  # Дополняется n массивами с 3-мя None

        return new_list

    @staticmethod
    def __create_list_of_empty_beads(list_range: int) -> list:
        return [[] for _ in range(0, list_range)]

    def save_as_lsr(self, file) -> None:
        for file_string in self.file_strings:
            file.write(file_string + "\n")
