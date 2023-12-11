import os
from collections import namedtuple
from logging import FileHandler, Formatter, Logger

FileInfo = namedtuple('FileInfo', 'name extension is_dir parent_dir')


def dir_info(path):
    for root, dirs, files in os.walk(path):
        for name in sorted(dirs + files):
            name, extension = os.path.splitext(name)
            is_dir = os.path.isdir(os.path.join(root, name))
            cur_dir = path.split(os.sep)[-1]
            parent_dir = cur_dir if os.path.abspath(
                root) == path else cur_dir + "\\" + os.path.relpath(root, path)
            yield FileInfo(name, extension, is_dir, parent_dir)


def main():
    log_format = Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    log = Logger('dir_info')
    file_handler = FileHandler('info.log')
    file_handler.setFormatter(log_format)
    log.addHandler(file_handler)
    with open('info.log', 'w') as f:
        # for file_info in dir_info(input('Введите путь до директории: ')):
        for file_info in dir_info(r'C:\Users\komp\Desktop\gbr\python\python\HW\HW9'):
            print(
                f'Имя {"каталога" if file_info.is_dir else "файла"}: {file_info.name}  Расширение: {file_info.extension}  Флаг каталога: {file_info.is_dir}  Название родительского каталога: {file_info.parent_dir}')
            log.info(
                f'Имя {"каталога" if file_info.is_dir else "файла"}: {file_info.name}  Расширение: {file_info.extension}  Флаг каталога: {file_info.is_dir}  Название родительского каталога: {file_info.parent_dir}')


if __name__ == "__main__":
    main()
