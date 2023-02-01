# Класс, хранящий контур. (Почему-то в .lsr файле помечается BEAD. Отсюда и название)
# Хранит в себе координаты векторов контура и высоту контура

class Bead:
    number: int  # Номер контура (сквозной)
    bead_coords: list[list[float]]  # Координаты векторов X Y Z в виде [[x1, y1, z1], [x2, y2, z2], ...]
    height: float  # Высота контура

    def __init__(self, number: int) -> None:
        self.number = number
        self.bead_coords = []
        self.height = None  # Это кстати может привести к багу) Нужно быть аккуратнее

    def add_bead_string(self, line: list[str]) -> None:  # Приходит разобранная по пробелам строка.
        x = float(line[4])
        y = float(line[5])
        z = float(line[6])
        if self.height is None:  # При первой строке сетается высота. Проблемы могут быть, если контур пустой
            self.height = z
        self.bead_coords.append([x, y, z])

    def print_bead_coords(self):  # Для отладки
        for line in self.bead_coords:
            print(line)

    def set_height(self, height: float) -> None:  # Если нужно у всего контура поменять высоту. Используется в Layer
        for bead_coord in self.bead_coords:
            bead_coord[2] = height
