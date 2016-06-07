import argparse
import datetime
import logging
import sys

from process import write_file, process_file, process_network
from indicator import indicator_read

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
    parser.add_argument("-i", "--indicator", help="считает Стохасти́ческий осциллятор")
    # parser.add_argument("-t", "--time", choices=["n", "y"], help="позволяет определить период данных")
    args = parser.parse_args()

    # настройка логирования
    try:
        level = getattr(logging, args.log.upper(), None)
        logging.basicConfig(filename='app.log', level=level)
    except:
        logging.error("Unexpected error:", sys.exc_info()[0])
    logging.info('Программа запущена')  # Вывод информационных соообщений

    # инициализация дат
    start, end = datetime.date(2015, 1, 1), datetime.date(2015, 12, 31)

    #print('Данная программа выводит максимальное значение для цены закрытия по месяцам.')
    # if args.file:
    #     process_file(args.file, start, end)  # функция выполняет обработку файла
    # elif args.symbol:
    #     process_network(args.symbol, start, end)  # читать данные по сети


    indicator_read(args.file)


    # запись в файл
    # try:
    #     if args.save() != "":
    #         write_file('out.txt')
    # except:
    #     logging.error("Не удалось записать в файл")


