from .bead import Bead
from .layer import Layer


class LSRParser:
    __layers: list[Layer]  # Лист слоев
    __beads: list[Bead]  # Сквозной лист контуров
    __path: str  # Путь до файла

    __first_check_in_file: bool  # Нужно для инициализации самой первой высоты (last_z_coord)
    __last_z_coord: float
    __bead_counter: int  # Сквозные счетчики
    __layer_counter: int
    __current_bead: Bead

    def __init__(self, path: str) -> None:
        self.__layers = []
        self.__beads = []
        self.__path = path

        self.__first_check_in_file = True
        self.__last_z_coord = 0
        self.__bead_counter = 0
        self.__layer_counter = 0
        self.__current_bead = None

    def parse(self) -> list[Layer]:
        file = open(self.__path, "r")
        self.__create_first_layer()
        for line in file:
            if line.startswith("# COMMENT"):  # Либо COMMENT
                self.__create_new_bead()  # Тогда создаем новый контур
                self.__add_comment_string_to_current_bead(line)
                self.__bead_counter += 1

                if self.__first_check_in_file:
                    self.__layers[-1].beads.append(self.__current_bead)
                    self.__first_check_in_file = False
                    continue

                self.__resolve_new_layer_creation()  # И возможно новый слой
                self.__layers[-1].beads.append(self.__current_bead)
            elif line[0].isdigit():  # Либо G-код. Тупо по цифре в начале
                self.__assert_none_bead()
                self.__add_default_string_to_current_bead(line)
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

    def __add_comment_string_to_current_bead(self, line: str):
        self.__current_bead.add_comment_line(line.strip().split(" "))

    def __resolve_new_layer_creation(self):
        if self.__current_bead.height - self.__last_z_coord != 0:
            self.__layers[-1].resolve_layer_height()  # Обновить высоту предыдущего
            self.__layer_counter += 1
            self.__layers.append(Layer(self.__layer_counter))  # Создать новый слой

    def __assert_none_bead(self):
        if self.__current_bead is None:
            raise RuntimeError("Встречена цифра до создания какого-либо контура. Такого быть не должно")

    def __add_default_string_to_current_bead(self, line: str):
        self.__current_bead.add_default_line(line.strip().split(" "))
