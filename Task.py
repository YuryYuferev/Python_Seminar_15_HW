# Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК:
# C:\Users\Yury\Desktop\directory
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит: имя файла без расширения или название каталога,
# расширение, если это файл, флаг каталога, название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя логирование.

import os
import logging
from collections import namedtuple

# Создание объекта namedtuple для хранения информации о файле или каталоге
FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_directory'])

def get_file_info(path):

    file_info_list = []
    # Проверка существования директории
    if not os.path.exists(path):
        logging.error(f"The directory {path} does not exist")
        return file_info_list
    # Получение списка файлов и каталогов в директории
    try:
        for file_name in os.listdir(path):
            file_path = os.path.join(path, file_name)
            if os.path.isfile(file_path):
                name, extension = os.path.splitext(file_name)
                is_directory = False
            else:
                name, extension = file_name, ''
                is_directory = True
            parent_directory = os.path.basename(path)
            file_info = FileInfo(name, extension, is_directory, parent_directory)
            file_info_list.append(file_info)
            logging.info(f"Added file/catalog: {file_name}")
    except Exception as e:
        logging.error(f"Error while retrieving content information: {str(e)}")
    return file_info_list
def save_file_info(file_info_list, output_file):

    try:
        with open(output_file, 'w') as file:
            for file_info in file_info_list:
                file.write(f"Name: {file_info.name}\n")
                file.write(f"Extension: {file_info.extension}\n")
                file.write(f"Directory: {'Yes' if file_info.is_directory else 'No'}\n")
                file.write(f"Parent Directory: {file_info.parent_directory}\n")
                file.write("--------------------\n")
        logging.info(f"The information is saved to a file: {output_file}")
    except Exception as e:
        logging.error(f"Error when saving information: {str(e)}")
def main():
    # Настройка логирования
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        filename='directory_info.log'
    )
    # Получение пути до директории из командной строки (C:\Users\Yury\Desktop\directory)
    path = input("Enter the directory path: ")
    # Получение информации о содержимом директории
    file_info_list = get_file_info(path)
    # Сохранение информации в текстовый файл
    save_file_info(file_info_list, 'file_info.txt')

if __name__ == "__main__":
    main()
