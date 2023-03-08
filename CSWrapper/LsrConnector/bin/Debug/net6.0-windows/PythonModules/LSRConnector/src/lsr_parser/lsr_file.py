from .parser.layer import Layer
from .parser.lsr_parser import LSRParser


class LSRFile:
    layers: list[Layer]  # Лист слоев
    __path: str  # Путь до файла

    def __init__(self, path: str) -> None:  # В конструктор необходимо передать путь до .lsr
        self.layers = []
        self.__path = path
        self.layers = LSRParser(path).parse()

    def __repr__(self) -> str:
        result_string = ""
        for layer in self.layers:
            result_string += str(layer)
        return result_string

