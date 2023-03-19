from lsr_parser.parser.bead import Bead
from lsr_parser.parser.layer import Layer


class LSRParser:
    __layers: list[Layer]  # Лист слоев
    __beads: list[Bead]  # Сквозной лист контуров
    __path: str  # Путь до файла

    __first_check_in_file: bool  # Нужно для инициализации самой первой высоты (last_z_coord)
    __last_z_coord: float
    __bead_counter: int  # Сквозные счетчики
    __layer_counter: int
    __current_bead: Bead
    __bead_creation_flag: bool

    def __init__(self, path: str) -> None:
        self.__layers = []
        self.__beads = []
        self.__path = path

        self.__first_check_in_file = True
        self.__last_z_coord = 0
        self.__bead_counter = 0
        self.__layer_counter = 0
        self.__current_bead = None
        self.__bead_creation_flag = False

    def parse(self) -> list[Layer]:
        file = open(self.__path, "r")
        self.__create_first_layer()
        for line in file:
            if "BEAD" in line:  # Либо Bead
                self.__create_new_bead()  # Создать bead, но никуда не добавлять, т.к. координаты еще неизвестны
                self.__bead_counter += 1
                if self.__first_check_in_file:
                    self.__layers[-1].add_bead(self.__current_bead)
                    self.__first_check_in_file = False
                    continue
                self.__bead_creation_flag = True
            elif line[0].isdigit():  # Либо G-код. Тупо по цифре в начале
                self.__assert_none_bead()
                if self.__bead_creation_flag:  # Необходимо для добавления bead в правильный layer
                    current_z_coord = float(line.strip().split(" ")[6])
                    self.__resolve_new_layer_creation(current_z_coord)
                    self.__layers[-1].add_bead(self.__current_bead)  # Т.к. контур создается раньше слоя, то его необходимо добавить
                    self.__bead_creation_flag = False
                self.__add_line_to_current_bead(line)
                self.__last_z_coord = self.__current_bead.height
        self.__layers[-1].resolve_layer_height()  # В самом конце обновить высоту последнего слоя
        file.close()
        return self.__layers

    def __create_first_layer(self):
        layer = Layer(self.__layer_counter)  # Самый первый слой
        self.__layers.append(layer)

    def __create_new_bead(self):
        self.__current_bead = Bead(number=self.__bead_counter)  # Создаем новый контур
        self.__beads.append(self.__current_bead)  # Добавляем в сквозной лист контуров

    def __resolve_new_layer_creation(self, current_z_coord: float):
        if current_z_coord - self.__last_z_coord != 0:
            self.__layers[-1].resolve_layer_height()  # Обновить высоту предыдущего
            self.__layer_counter += 1
            new_layer = Layer(self.__layer_counter)  # Создать новый слой
            self.__layers.append(new_layer)

    def __assert_none_bead(self):
        if self.__current_bead is None:
            raise RuntimeError("Встречена цифра до создания какого-либо контура. Такого быть не должно")

    def __add_line_to_current_bead(self, line: str):
        self.__current_bead.add_line(line.strip().split(" "))
