class LSRLine:
    power: int
    arc_x: float
    arc_y: float
    arc_z: float
    first_x: float
    first_y: float
    first_z: float
    second_x: float
    second_y: float
    second_z: float
    radius: float
    velocity: float
    start_time: float

    def __init__(self, list_info: tuple[str]) -> None:
        self.__map_list_to_attribute(list_info)

    def __repr__(self) -> str:
        return f"{self.power} {self.arc_x} {self.arc_y} {self.arc_z} {self.first_x} {self.first_y} {self.first_z} " \
               f"{self.second_x} {self.second_y} {self.second_z} {self.radius} {self.velocity} {self.start_time}"

    def __map_list_to_attribute(self, list_info: tuple[str]) -> None:
        if len(list_info) != 13:
            raise ValueError("В конструктор LSRLine передан контейнер неверной длины")
        else:
            self.power = int(list_info[0])
            self.arc_x = float(list_info[1])
            self.arc_y = float(list_info[2])
            self.arc_z = float(list_info[3])
            self.first_x = float(list_info[4])
            self.first_y = float(list_info[5])
            self.first_z = float(list_info[6])
            self.second_x = float(list_info[7])
            self.second_y = float(list_info[8])
            self.second_z = float(list_info[9])
            self.radius = float(list_info[10])
            self.velocity = float(list_info[11])
            self.start_time = float(list_info[12])

    def set_height(self, new_height: float):
        self.first_z = new_height
        self.second_z = new_height

    def get_second_coordinates(self) -> tuple[float]:
        return self.second_x, self.second_y, self.second_z

    def get_simple_coords(self) -> tuple:
        return float(self.first_x), float(self.first_y), float(self.first_z)

    def get_first_coordinates(self) -> tuple:
        return self.first_x, self.first_y, self.first_z