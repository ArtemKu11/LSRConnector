class CommentLine:
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
    frc_value: str
    start_time: float

    def __init__(self, list_info: tuple[str]) -> None:
        self.__map_list_to_attribute(list_info)

    def __repr__(self) -> str:
        return f"# COMMENT ({self.power} {self.arc_x} {self.arc_y} {self.arc_z} {self.first_x} {self.first_y} " \
               f"{self.first_z} {self.second_x} {self.second_y} {self.second_z} " \
               f"{self.radius} {self.velocity} {self.frc_value} {self.start_time}) COMMENT"

    def __map_list_to_attribute(self, list_info: tuple[str]) -> None:
        if len(list_info) == 16:
            self.power = int(list_info[2][1:])
            self.arc_x = float(list_info[3])
            self.arc_y = float(list_info[4])
            self.arc_z = float(list_info[5])
            self.first_x = float(list_info[6])
            self.first_y = float(list_info[7])
            self.first_z = float(list_info[8])
            self.second_x = float(list_info[9])
            self.second_y = float(list_info[10])
            self.second_z = float(list_info[11])
            self.radius = float(list_info[12])
            self.velocity = float(list_info[13])
            self.frc_value = ""
            self.start_time = float(list_info[14][:-1])
        elif len(list_info) == 17:
            self.power = int(list_info[2][1:])
            self.arc_x = float(list_info[3])
            self.arc_y = float(list_info[4])
            self.arc_z = float(list_info[5])
            self.first_x = float(list_info[6])
            self.first_y = float(list_info[7])
            self.first_z = float(list_info[8])
            self.second_x = float(list_info[9])
            self.second_y = float(list_info[10])
            self.second_z = float(list_info[11])
            self.radius = float(list_info[12])
            self.velocity = float(list_info[13])
            self.frc_value = list_info[14]
            self.start_time = float(list_info[15][:-1])
        else:
            print(list_info)
            raise ValueError("В конструктор CommentLine передан контейнер неверной длины")

    def set_height(self, new_height: float) -> None:
        self.first_z = new_height
        self.second_z = new_height

    def set_first_coordinates(self, new_coordinates: tuple[float]):
        self.first_x = float(new_coordinates[0])
        self.first_y = float(new_coordinates[1])
        self.first_z = float(new_coordinates[2])

    def get_first_coordinates(self) -> tuple:
        return self.first_x, self.first_y, self.first_z
