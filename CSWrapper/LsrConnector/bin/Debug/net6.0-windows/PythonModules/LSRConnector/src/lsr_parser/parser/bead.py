from builtins import RuntimeError

from .comment_line import CommentLine
from .default_line import DefaultLine


class Bead:
    number: int  # Номер контура (сквозной)
    comment_line: CommentLine
    lines: list[DefaultLine]
    height: float  # Высота контура

    def __init__(self, number: int) -> None:
        self.number = number
        self.height = None  # Это кстати может привести к багу) Нужно быть аккуратнее
        self.comment_line = None
        self.lines = []

    def __repr__(self) -> str:
        result_string = str(self.comment_line) + "\n"
        for line in self.lines:
            result_string += str(line) + "\n"
        return result_string

    def add_default_line(self, line: list[str]) -> None:  # Приходит разобранная по пробелам строка.
        default_line = DefaultLine(tuple(line))
        self.lines.append(default_line)
        if self.height is None:  # При первой строке сетается высота. Проблемы могут быть, если контур пустой
            self.height = default_line.second_z

    def add_comment_line(self, line: list[str]) -> None:  # Приходит разобранная по пробелам строка.
        if self.comment_line is not None:
            raise RuntimeError(
                f"Попытка добавления второй строки с комментарием в один слой. Номер слоя: {self.number}")
        else:
            comment_line = CommentLine(tuple(line))
            self.comment_line = comment_line
            if self.height is None:  # При первой строке сетается высота. Проблемы могут быть, если контур пустой
                self.height = comment_line.second_z

    def set_height(self, height: float) -> None:  # Если нужно у всего контура поменять высоту. Используется в Layer
        self.comment_line.set_height(height)
        for line in self.lines:
            line.set_height(height)

    # Транзитивные функции, обеспечивающие функционал соответствующих функций в Layer

    def set_first_coords_in_comment_string(self, coords: tuple[float]):
        self.comment_line.set_first_coordinates(coords)

    def get_last_second_coords(self) -> tuple[float]:
        return self.lines[-1].get_second_coordinates()

    def get_simple_coords(self) -> list:
        result = []
        for line in self.lines:
            result.append(list(line.get_simple_coords()))
        return result

    def get_file_strings(self) -> list:
        result = []
        result.append(str(self.comment_line))
        for line in self.lines:
            result.append(str(line))
        return result

    def get_first_comment_coordinates(self) -> tuple:
        return self.comment_line.get_first_coordinates()
