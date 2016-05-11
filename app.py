import sys
import argparse
import csv
import datetime
import logging
from urllib.request import urlopen
from urllib.parse import quote_plus


def process(data):
    flag2 = 0
    maximum, month = -1, -1
    global voc
    voc = {'Месяц': 'MAX значение'}
    print("Месяц   MAX значение")
    try:
        for row in data:
            num = float(row[4])
            time = row[0].split('-')
            if month == int(time[1]):
                if maximum < num:
                    maximum = num
            elif flag2 == 1:
                voc[str(month)] = maximum
                print(repr(month).rjust(4), repr(maximum).rjust(12), end='\n')
                month = int(time[1])
                maximum = num
            else:
                flag2 = 1
                month = int(time[1])
                maximum = num
        voc[str(month)] = maximum
        print(repr(month).rjust(4), repr(maximum).rjust(12), end='\n')
    except:
        print('Неправильный формат данных')
        logging.error('Неправильный формат данных')

def writeFile (filename):
    try:
        f = open(filename, 'w')
        f.write('Выведены максимальное значение для цены закрытия по месяцам.\n')
        #vo = sorted(voc.keys())
        for k, v in voc.items():
            f.write(str(k) +"    " + str(v) + '\n')
        f.close()
    except:
        print("Ошибка при записи файла ", sys.exc_info()[0])
        logging.error("Ошибка при записи файла ", sys.exc_info()[0])

def process_file(file_name, start, end):
    try:
        f = open(file_name, 'r')
    except IOError:
        print('Не может открыть файл ', file_name)
        logging.error("Не может открыть файл", file_name)
    else:
        f.readline()
        process(csv.reader(f, delimiter=','))

def process_network(symbol, start, end):
    #start = datetime.date(2015, 1, 1)
    #end = datetime.date(2015, 12, 31)
    url = "http://www.google.com/finance/historical?q={0}&startdate={1}&enddate={2}&output=csv"
    url = url.format(symbol.upper(), quote_plus(start.strftime('%b %d, %Y')), quote_plus(end.strftime('%b %d, %Y')))
    data = urlopen(url).readlines()
    process(data)
    #for row in data[1:]:  # Пропускаем первую строку с именами колонок
        #print(row.decode().strip().split(','))

if __name__ == "__main__":
    # проверка аргументов
    try:
        parser = argparse.ArgumentParser()
        group = parser.add_mutually_exclusive_group()
        group.add_argument("-sb", "--symbol", help="работает с интернет-документом")
        group.add_argument("-f", "--file", help="работает с файлом")
        parser.add_argument("-s", "--save", help="сохранит результат в файл")
        parser.add_argument("-lf", "--logfile", help="определяет имя лог файла")
        parser.add_argument("-l", "--log", help="уровень логирования")
        #parser.add_argument("-t", "--time", choices=["n", "y"], help="позволяет определить период данных")
        args = parser.parse_args()

        # настройка логирования
        try:
            level = getattr(logging, args.log.upper(), None)
            logging.basicConfig(filename='app.log', level=level)
        except:
            print("Unexpected error:", sys.exc_info()[0])
        logging.info('Программа запущена')  # Вывод информационных соообщений

        #проверка дат
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

        #запись в файл
        writeFile(args.save)
    except:
        print("Ошибка ", sys.exc_info()[0])
        logging.info("Ошибка ", sys.exc_info()[0])

