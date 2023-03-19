from builtins import RuntimeError

from .lsr_line import LSRLine


class Bead:
    number: int  # Номер контура (сквозной)
    lines: list[LSRLine]
    height: float  # Высота контура

    def __init__(self, number: int) -> None:
        self.number = number
        self.height = None  # Это кстати может привести к багу) Нужно быть аккуратнее
        self.lines = []

    def __repr__(self) -> str:
        result_string = ""
        for line in self.lines:
            result_string += str(line) + "\n"
        return result_string

    def add_line(self, line: list[str]) -> None:  # Приходит разобранная по пробелам строка.
        default_line = LSRLine(tuple(line))
        self.lines.append(default_line)
        if self.height is None:  # При первой строке сетается высота. Проблемы могут быть, если контур пустой
            self.height = default_line.second_z

    def set_height(self, height: float) -> None:  # Если нужно у всего контура поменять высоту. Используется в Layer
        for line in self.lines:
            line.set_height(height)

    # Транзитивные функции, обеспечивающие функционал соответствующих функций в Layer

    def get_last_second_coords(self) -> tuple[float]:
        return self.lines[-1].get_second_coordinates()

    def get_simple_coords(self) -> list:
        result = []
        for line in self.lines:
            result.append(list(line.get_simple_coords()))
        return result

    def get_file_strings(self) -> list:
        result = []
        for line in self.lines:
            result.append(str(line))
        return result
