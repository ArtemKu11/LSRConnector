from .bead import Bead


class Layer:
    height: float  # Высота слоя, сетается по высоте первого вектора, первого контура при вызове resolve_layer_height()
    number: int  # Номер слоя, сквозной от 0
    beads: list[Bead]  # Лист контуров

    def __init__(self, number: int) -> None:
        self.number = number
        self.height = None  # Высота может остаться None, если высота первого контура будет None (если контур будет пуст)
        self.beads = []

    def __repr__(self) -> str:
        result_string = ""
        for bead in self.beads:
            result_string += str(bead)
        return result_string

    def add_bead(self, bead: Bead) -> None:  # Добавить контур
        self.beads.append(bead)

    def resolve_layer_height(self) -> None:  # Вызывается в конце заполнения слоя
        if len(self.beads) > 0:
            self.height = self.beads[0].height

    def set_height(self, height: float) -> None:  # Вызывается, если нужно разом у всего слоя рекурсивно поменять высоту
        for bead in self.beads:
            bead.set_height(height)
        self.height = height

    def get_last_second_coords(self) -> tuple[float]:  # Возвращает END POINT в последней строке последнего контура
        return self.beads[len(self.beads) - 1].get_last_second_coords()

    def get_file_strings(self):  # Возвращает слой в виде списка строк из lsr файла. Без BEAD counter
        files_strings = []
        for bead in self.beads:
            files_strings.extend(bead.get_file_strings())
        return files_strings

    def get_simple_coords(self) -> list:  # Возвращает слой в виде лита листов, в которых листы ... с [x, y, z]
        result = []
        for bead in self.beads:
            result.append(bead.get_simple_coords())
        return result