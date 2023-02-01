from .bead import Bead


# Класс, хранящий слой.
# Хранит в себе лист контуров этого слоя и высоту слоя (сетается по высоте первого вектора, первого контура)

class Layer:
    height: float  # Высота слоя, сетается по высоте первого вектора, первого контура
    number: int  # Номер слоя, сквозной от 0
    beads: list[Bead]  # Лист контуров

    def __init__(self, number: int) -> None:
        self.number = number
        self.height = None  # Высота может остаться None, если высота первого контура будет None (если контур будет пуст)
        self.beads = []

    def add_bead(self, bead: Bead) -> None:
        self.beads.append(bead)

    def resolve_layer_height(self) -> None:  # Вызывается в конце заполнения слоя
        if len(self.beads) > 0:
            self.height = self.beads[0].height

    def set_height(self, height: float) -> None:  # Вызывается, если нужно разом у всего слоя рекурсивно поменять высоту
        for bead in self.beads:
            bead.set_height(height)
