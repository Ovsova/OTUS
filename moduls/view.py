import csv


class DirectoryData:
    """чтение файла"""
    @classmethod
    def read(cls, filepath):
        try:

            file_read = open(filepath, 'r', encoding='UTF-8')
            file_reader = list(csv.reader(file_read, dialect='excel', delimiter=','))
            for line in file_reader:
                if len(line) == 0:
                    print('Файл пуст \n')
                else:
                    return file_reader
        except FileNotFoundError:
            return print('Скорее всего файла-справочника не существует \n')
