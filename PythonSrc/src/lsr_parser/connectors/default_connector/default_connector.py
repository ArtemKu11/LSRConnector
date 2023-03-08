from lsr_parser.lsr_file import LSRFile
from lsr_parser.parser.layer import Layer
from lsr_parser.parsed_lsr import ParsedLSR


# Осуществляет соединение двух G-кодов по следующим правилам:
# 1. Выбирается наименьший G-код по количеству слоев
# 2. Он итерируется. На каждый слой одного кода приходится один слой из второго
# 3. Конфликт высот решается приведением к наименьшей высоте из двух
# 4. После итерации наименьшего докладываются слои из большего
class DefaultConnector:
    header = "# POWER, ARC VECTOR, START POINT (X,Y,Z), END POINT, (X,Y,Z), RADIUS, VELOCITY, START TIME"
    first_file: LSRFile
    second_file: LSRFile
    list_of_simple_coords = []  # X, Y, Z
    file_strings = []  # Готовые файловые строки
    layer_length_problem: bool  # Флаг для принта отб ошибке количества слоев
    last_coordinates: tuple  # Координаты, которые будут сетаться в START POINT (XYZ) в COMMENT строку
    bead_counter: int  # Счетчик BEAD

    def __init__(self, first_file: LSRFile, second_file: LSRFile) -> None:
        self.first_file = first_file
        self.second_file = second_file
        self.list_of_simple_coords = []
        self.file_strings = []
        self.layer_length_problem = False
        self.last_coordinates = ()
        self.bead_counter = 0

    def connect_two_files(self) -> ParsedLSR:
        enumerate_length = self.__resolve_symmetrically_enumerate_length()  # Наименьшее количество слоев
        self.__resolve_first_coordinates()  # Сетает в last_coordinates первые координаты с первого слоя
        self.file_strings.append(self.header)
        self.__add_symmetrically(enumerate_length)

        if self.layer_length_problem:
            result = self.__resolve_asymmetrically_enumerate_range()  # Возвращает range и файл, который надо доитерировать
            self.__add_asymmetrically((result[0], result[1]), result[2])

        return ParsedLSR(self.list_of_simple_coords, self.file_strings)

    def __resolve_symmetrically_enumerate_length(self):
        enumerate_length = len(self.first_file.layers)
        if len(self.first_file.layers) != len(self.second_file.layers):
            print("РАЗНОЕ КОЛИЧЕСТВО СЛОЕВ")
            enumerate_length = min(len(self.first_file.layers), len(self.second_file.layers))
            self.layer_length_problem = True
        return enumerate_length

    def __resolve_first_coordinates(self):
        self.last_coordinates = self.first_file.layers[0].get_first_comment_coordinates()

    def __add_symmetrically(self, enumerate_length: int) -> None:
        for i in range(0, enumerate_length):
            first_file_layer = self.first_file.layers[i]
            second_file_layer = self.second_file.layers[i]

            if first_file_layer.height != second_file_layer.height:  # Если высоты разные, то приводится к минимальной
                self.__resolve_height_difference(first_file_layer, second_file_layer)

            self.__add_simple_coords(first_file_layer, second_file_layer)
            self.__add_file_strings(first_file_layer, second_file_layer)

    def __resolve_height_difference(self, first_file_layer: Layer, second_file_layer: Layer) -> None:
        min_height = min(first_file_layer.height, second_file_layer.height)
        if first_file_layer.height < second_file_layer.height:
            second_file_layer.set_height(min_height)
        else:
            first_file_layer.set_height(min_height)
        print(f"РАЗНАЯ ВЫСОТА У СЛОЕВ: {first_file_layer.number}, {second_file_layer.number}")

    def __add_simple_coords(self, first_file_layer: Layer, second_file_layer: Layer):
        bead_list = []
        bead_list.extend(first_file_layer.get_simple_coords())
        bead_list.extend(second_file_layer.get_simple_coords())
        self.list_of_simple_coords.append(bead_list)  # Добавление листа, соответствующего слою, с листом контуров

    def __add_file_strings(self, first_file_layer: Layer, second_file_layer: Layer):
        first_file_layer.set_first_coords_into_comment_string(self.last_coordinates)  # Сетает START POINT в COMMENT строке
        second_file_layer.set_first_coords_into_comment_string(first_file_layer.get_last_second_coords())  # Сетает START POINT в COMMENT строке
        self.last_coordinates = second_file_layer.get_last_second_coords()

        for bead in first_file_layer.beads:
            self.file_strings.append(f"# ( BEAD {self.bead_counter} )")
            self.bead_counter += 1
            self.file_strings.extend(bead.get_file_strings())

        for bead in second_file_layer.beads:
            self.file_strings.append(f"# ( BEAD {self.bead_counter} )")
            self.bead_counter += 1
            self.file_strings.extend(bead.get_file_strings())

    def __resolve_asymmetrically_enumerate_range(self) -> tuple:
        first_value = min(len(self.first_file.layers), len(self.second_file.layers))
        second_value = max(len(self.first_file.layers), len(self.second_file.layers))
        required_file = self.first_file
        if second_value == len(self.second_file.layers):
            required_file = self.second_file
        return first_value, second_value, required_file

    def __add_asymmetrically(self, enumerate_range: tuple, required_file: LSRFile) -> None:
        for i in range(enumerate_range[0], enumerate_range[1]):
            file_layer = required_file.layers[i]

            bead_list = []
            bead_list.extend(file_layer.get_simple_coords())
            self.list_of_simple_coords.append(bead_list)

            file_layer.set_first_coords_into_comment_string(self.last_coordinates)

            for bead in file_layer.beads:
                self.file_strings.append(f"# ( BEAD {self.bead_counter} )")
                self.bead_counter += 1
                self.file_strings.extend(bead.get_file_strings())

            self.last_coordinates = file_layer.get_last_second_coords()
