from lsr_parser import LSRFile, DefaultConnector, CleverConnector


def compare_two_files(f_file: str, s_file: str):
    f = open(f_file, "r")
    f_file_lines = f.readlines()
    f.close()

    f = open(s_file, "r")
    s_file_lines = f.readlines()
    f.close()

    for i, line in enumerate(f_file_lines):
        if line != s_file_lines[i]:
            print(f"Не равна линия номер {i}")
            print(f"{line} != {s_file_lines[i]}")
    if len(f_file_lines) != len(s_file_lines):
        print("Не равно количество линий")
        print(f"{len(f_file_lines)} != {len(s_file_lines)}")


if __name__ == '__main__':
    vnut = LSRFile("Vnut_lightweight.lsr")  # 1. Определить 2 файла
    vnesh = LSRFile("Vnesh_lightweight.lsr")
    file1 = open("result.lsr", "w")
    file2 = open("result2.lsr", "w")
    DefaultConnector(vnut, vnesh).connect_two_files().save_as_lsr(file1)  # 2. Отдать соединителю
    CleverConnector(vnut, vnesh).connect_two_files().save_as_lsr(file2)
    file1.close()
    file2.close()

    compare_two_files("result.lsr", "result2.lsr")
    print("done")
