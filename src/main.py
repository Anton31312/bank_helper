from utils import *

FILE_URL = "help_files\operations.json"


def main():
    try:
        operations_list = load_file(FILE_URL)
        operations = make_operations(operations_list)
        print(get_executed_five(operations))
    except FileNotFoundError:
        print("~!Ошибка!~\nФайл не найден")


if __name__ == "__main__":
    main()