from .parsed_lsr import ParsedLSR
from .layer import Layer
from .bead import Bead


# Парсер .lsr файлов.
# Хранит лист слоев, каждый из которых хранит лист контуров, каждый из которых хранит лист векторов

class LSRFile:
    layers: list[Layer]  # Лист слоев
    __beads: list[Bead]  # Сквозной лист контуров
    path: str  # Путь до файла

    def __init__(self, path: str) -> None:  # В конструктор необходимо передать путь до .lsr
        self.layers = []
        self.__beads = []
        self.path = path
        self.__parse_lsr_file()  # Запуск логики

    def __parse_lsr_file(self) -> None:
        f = open(self.path, "r")
        self.__parsing(f)  # Это можно обернуть в try except
        f.close()

    def __parsing(self, file) -> None:
        first_check_in_file = True  # Нужно для инициализации самой первой высоты (last_z_coord)
        last_z_coord = 0
        bead_counter = -1  # Сквозные счетчики
        layer_counter = 0
        new_bead_flag = False  # Необходимо для корректного добавления нового контура в соответствующий слой

        layer = Layer(layer_counter)  # Самый первый слой
        self.layers.append(layer)

        for line in file:  # Цикл может сломаться, если перед самым первым BEAD будет встречена цифра в начале строки
            if "BEAD" in line:  # Либо BEAD (контур)
                # Если BEAD:
                bead_counter += 1
                current_bead = Bead(number=bead_counter)  # Создаем новый контур
                self.__beads.append(current_bead)  # Добавляем в сквозной лист контуров
                new_bead_flag = True  # В слой сразу добавлять нельзя, т.к. слой может быть новым

            elif line[0].isdigit():  # Либо G-код. Тупо по цифре в начале
                # Если G-код:
                words = self.__get_all_words(line)  # Разбирает строку по пробелам
                self.__beads[bead_counter].add_bead_string(words)  # Добавляет строку в последний контур

                z_coord = float(words[6])  # Получаем текущую z координату

                if first_check_in_file:  # Инициализация самой первой z координаты. Гарантирует, что не создастся пустой первый слой
                    last_z_coord = z_coord
                    first_check_in_file = False

                if z_coord - last_z_coord != 0:  # Если есть разница между текущей и предыдущей координатой, то новый слой
                    self.layers[layer_counter].resolve_layer_height()  # Сначала в предыдущем определить высоту

                    layer_counter += 1

                    layer = Layer(layer_counter)  # Создать новый
                    current_bead = self.__beads[bead_counter]
                    layer.add_bead(current_bead)  # В него добавить текущий контур
                    self.layers.append(layer)

                    new_bead_flag = False
                else:
                    if new_bead_flag:  # Если же слой не новый, но новая строка в новом контуре
                        new_bead_flag = False
                        current_bead = self.__beads[bead_counter]
                        self.layers[layer_counter].add_bead(current_bead)  # То текущий контур добавить в текущий слой
                last_z_coord = z_coord

        self.layers[layer_counter].resolve_layer_height()  # После окончания цикла определить высоту в последнем слое

    @staticmethod
    def __get_all_words(line: str) -> list[str]:
        return line.split(" ")

    # Для парсинга одного файла. Делает из self лист листов, отдает ParsedLSR
    # Далее можно получить в желаемом виде
    def parse(self) -> ParsedLSR:
        result = []

        for layer in self.layers:  # Послойная итерация
            bead_list = []
            for bead in layer.beads:  # Проход по контурам слоя
                bead_list.append(bead.bead_coords)
            result.append(bead_list)  # Добавление листа, соответствующего слою, с листом контуров

        return ParsedLSR(result)
