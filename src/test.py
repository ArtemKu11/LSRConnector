from lsr_parser import LSRFile, check_joinable, connect_two_files, risky_connect_two_files


def pretty_print(files_list: list) -> None:
    for number, layers in enumerate(files_list):
        print(f"СЛОЙ {number}")
        for b_number, beads in enumerate(layers):
            print(f"  КОНТУР {b_number}")
            for coords in beads:
                print(f"   {coords}")


if __name__ == '__main__':
    vnut = LSRFile("Vnut_lightweight.lsr")  # 1. Определить два LSR файла
    vnesh = LSRFile("Vnesh_lightweight.lsr")
    check_result = check_joinable(vnut, vnesh, True)  # 2. Передать их в функцию, проверяющую ошибки соединения
    if (check_result != 3) and (check_result != 2):
        result = connect_two_files(vnut, vnesh)  # 3. Если все нормально, соединить эти два файла
        list_result = result.get_as_list()  # 4. Получить результат в нужном виде
        print(f"Слоев: {len(list_result)},\nВ первом слое контуров: {len(list_result[0])},\n"
              f"В первом слое в первом контуре векторов: {len(list_result[0][0])},\n"
              f"В первом слое в первом контуре в первом векторе координат: {len(list_result[0][1][0])}")

        list_result = risky_connect_two_files("Vnut_lightweight.lsr",
                                              "Vnesh_lightweight.lsr").get_as_list()  # 5. Ну либо одной строкой, но бех проверок

        print(f"Слоев: {len(list_result)},\nВ первом слое контуров: {len(list_result[0])},\n"
              f"В первом слое в первом контуре векторов: {len(list_result[0][0])},\n"
              f"В первом слое в первом контуре в первом векторе координат: {len(list_result[0][1][0])}")

        pretty_print(list_result)

        print(result.get_as_numpy_array())  # 6. Можно делать всякие штуки с результатом
        print(result.get_as_list())
        print(result.get_as_json(indent=4))

        file = open("my_json.json", "w")
        result.save_into_json_file(file, indent=4)
        file.close()

        print(LSRFile("Vnut_lightweight.lsr").parse().get_as_list())  # 7. Парсинг одного файла
