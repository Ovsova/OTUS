import csv


class DirectoryData:
    """чтение файла"""

    def read(self):
        try:
            print('4', )
            file_read = open('directory_enquiries.csv', 'r', encoding='UTF-8')
            file_reader = csv.reader(file_read, dialect='excel', delimiter=',')
            for line in file_reader:
                if len(line) == 0:
                    print('Файл пуст \n')
                else:
                    return file_reader
        except FileNotFoundError:
            return print('Скорее всего файла-справочника не существует \n')
