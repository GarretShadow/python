import argparse
import datetime
import logging
import sys

# import time
from process import writeFile, process_file, process_network

if __name__ == "__main__":
    # проверка аргументов
    # try:
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-sb", "--symbol", help="работает с интернет-документом")
    group.add_argument("-f", "--file", help="работает с файлом")
    parser.add_argument("-s", "--save", help="сохранит результат в файл")
    parser.add_argument("-lf", "--logfile", help="определяет имя лог файла")
    parser.add_argument("-l", "--log", help="уровень логирования")
    # parser.add_argument("-t", "--time", choices=["n", "y"], help="позволяет определить период данных")
    args = parser.parse_args()

    # настройка логирования
    try:
        level = getattr(logging, args.log.upper(), None)
        logging.basicConfig(filename='app.log', level=level)
    except:
        print("Unexpected error:", sys.exc_info()[0])
    logging.info('Программа запущена')  # Вывод информационных соообщений

    # инициализация дат
    start, end = datetime.date(2015, 1, 1), datetime.date(2015, 12, 31)
    # try:
    #     if args.time == "y":
    #         print("Введите начало и конец периода наблюдения:")
    #         #считать start, end = datetime.date(args.start_t), datetime.date(args.end_t)
    # except:
    #     print("Неправильный формат дат")
    #     logging.error("Неправильный формат дат")

    print('Данная программа выводит максимальное значение для цены закрытия по месяцам.')
    if args.file:
        process_file(args.file, start, end)  # функция выполняет обработку файла
    elif args.symbol:
        process_network(args.symbol, start, end)  # читать данные по сети

    # запись в файл
    try:
        writeFile('out.txt')
    except:
        print('')
    # if (args.save() is not None):
    #     writeFile('out_app.txt')

