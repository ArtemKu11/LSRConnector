from lsr_parser.lsr_file import LSRFile
from lsr_parser.parser.layer import Layer
from lsr_parser.parsed_lsr import ParsedLSR


# Осуществляет соединение двух G-кодов по следующим правилам:
# 1. Выбирается наименьший G-код по количеству слоев
# 2. Он итерируется. Каждому слою этого файла соответствует какой-либо слой из большего файла
# 3. Каждому слою из большего файла либо соответствует строго один файл из меньшего, либо не соответствует вообще
# 3. Конфликт высот решается приведением к наименьшей высоте из двух наиболее близких друг к другу слоев
# 4. После итерации наименьшего докладываются слои из большего
class DownToUpConnector:
    header = "# POWER, ARC VECTOR, START POINT (X,Y,Z), END POINT, (X,Y,Z), RADIUS, VELOCITY, START TIME"
    first_file: LSRFile
    second_file: LSRFile
    list_of_simple_coords = []  # X, Y, Z
    file_strings = []  # Готовые файловые строки

    first_file_layers: list[Layer]  # Слои из первого файла
    second_file_layers: list[Layer]  # Слои из второго файла
    sorted_result: list[Layer]  # Список всех слоев, отсортированных и приведенных к одной высоте
    bead_counter: int  # Счетчик BEAD

    def __init__(self, first_file: LSRFile, second_file: LSRFile) -> None:
        self.first_file = first_file
        self.second_file = second_file
        self.list_of_simple_coords = []
        self.file_strings = []
        self.first_file_layers = []
        self.second_file_layers = []
        self.sorted_result = []
        self.bead_counter = 0

    def connect_two_files(self) -> ParsedLSR:
        self.__sort_layers()
        self.file_strings.append(self.header)
        self.__add_everything()
        return ParsedLSR(self.list_of_simple_coords, self.file_strings)

    def __sort_layers(self):
        self.first_file_layers = self.first_file.layers
        self.second_file_layers = self.second_file.layers

        if len(self.first_file_layers) < len(self.second_file_layers):  # Выбирается наименьший файл. Он и итерируется
            self.__iterate_file(True)
        else:
            self.__iterate_file(False)  # Если равны, то итерироваться будет второй, а склеиваться будет 1-2-1-2....

    def __iterate_file(self, first_file: bool) -> None:
        less_layers = self.second_file_layers
        large_layers = self.first_file_layers
        if first_file:
            less_layers = self.first_file_layers
            large_layers = self.second_file_layers

        for layer in less_layers:  # Берется слой из меньшего файла
            height = layer.height
            index = self.__find_near_layer(height, large_layers)  # Ищется ближайший к нему слой из большего файла
            layer.set_height(large_layers[
                                 index].height)  # Высота слоя из меньшего файла приводится к высоте ближайшего слоя из большего файла

            for i in range(0, index + 1):  # Сначала добавляются слои из большего файла перед тем, который ближайший
                self.sorted_result.append(large_layers[i])

            self.sorted_result.append(layer)  # Затем добавляется слой из меньшего файла
            large_layers = large_layers[index + 1:]  # Удаляются использованные слои из большего файла

        for layer in large_layers:  # После итерации наименьшего файла докладываются оставшиеся слои из большего
            self.sorted_result.append(layer)

    def __find_near_layer(self, height: float, large_layers: list[Layer]) -> int:
        min_diff = abs(large_layers[
                           0].height - height)  # 0 слой - это не самый первый слой в файле, а самый первый из неиспользованных
        min_i = 0
        for i, large_file_layer in enumerate(large_layers):
            large_file_layer_height = large_file_layer.height  # Берем высоту слоя из большего файла
            diff = abs(large_file_layer_height - height)
            if diff > min_diff:  # Сравниваем с высотой нашего слоя из меньшего файла
                return min_i  # Если больше, то возвращаем предыдущую минимальную
            else:
                min_diff = diff  # Если меньше, то сетаем в минимальную
                min_i = i
        return min_i

    def __add_everything(self):
        bead_list = []
        last_layer: Layer = None
        for layer in self.sorted_result:
            self.__add_file_strings(layer)
            if last_layer is not None:
                if last_layer.height != layer.height:
                    self.list_of_simple_coords.append(bead_list)
                    bead_list = []
            bead_list.extend(layer.get_simple_coords())
            last_layer = layer
        if len(bead_list) > 0:
            self.list_of_simple_coords.append(bead_list)

    def __add_simple_coords(self, layer: Layer):
        bead_list = []
        bead_list.append(layer.get_simple_coords())
        self.list_of_simple_coords.append(bead_list)

    def __add_file_strings(self, layer: Layer):
        # print(len(layer.beads))
        for bead in layer.beads:
            self.file_strings.append(f"# ( BEAD {self.bead_counter} )")
            self.bead_counter += 1
            self.file_strings.extend(bead.get_file_strings())
