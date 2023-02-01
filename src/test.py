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
        files = connect_two_files(vnut, vnesh)  # 3. Если все нормально, соединить эти два файла

        print(f"Слоев: {len(files)},\nВ первом слое контуров: {len(files[0])},\n"
              f"В первом слое в первом контуре векторов: {len(files[0][0])},\n"
              f"В первом слое в первом контуре в первом векторе координат: {len(files[0][1][0])}")

        files = risky_connect_two_files("Vnut_lightweight.lsr", "Vnesh_lightweight.lsr")  # 4. Ну либо одной строкой, но бех проверок

        print(f"Слоев: {len(files)},\nВ первом слое контуров: {len(files[0])},\n"
              f"В первом слое в первом контуре векторов: {len(files[0][0])},\n"
              f"В первом слое в первом контуре в первом векторе координат: {len(files[0][1][0])}")

        pretty_print(files)
