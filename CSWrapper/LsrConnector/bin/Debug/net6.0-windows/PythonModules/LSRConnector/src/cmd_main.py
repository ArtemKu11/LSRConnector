import sys
from lsr_parser import LSRFile, DownToUpConnector

if __name__ == '__main__':
    if len(sys.argv) != 4:
        raise ValueError("Неверное количество аргументов командной строки")
    first_file_path = sys.argv[1]
    second_file_path = sys.argv[2]
    result_file_path = sys.argv[3]

    print(f"Первый файл: {first_file_path}")
    print(f"Второй файл: {second_file_path}")
    print(f"Файл с результатом: {result_file_path}\n")

    print("Парсинг первого файла...")
    first_lsr_file = LSRFile(first_file_path)
    print(f"Слоев в первом файле: {len(first_lsr_file.layers)}\n")

    print("Парсинг второго файла...")
    second_lsr_file = LSRFile(second_file_path)
    print(f"Слоев во втором файле: {len(second_lsr_file.layers)}\n")


    print("Соединение...")
    connect_result = DownToUpConnector(first_lsr_file, second_lsr_file).connect_two_files()
    print(f"Слоев в результате: {len(connect_result.get_as_list())}\n")

    print("Сохранение...")
    result_file = open(result_file_path, "w")
    try:
        connect_result.save_as_lsr(result_file)
    except Exception as e:
        result_file.close()
        raise e
    result_file.close()

    print("Успешно!")
