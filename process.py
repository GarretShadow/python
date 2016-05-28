import csv
import logging
import sys
from urllib.parse import quote_plus
from urllib.request import urlopen
from datetime import datetime


def process(data):
    print("Месяц   MAX значение")
    by_month_max = {month: -1 for month in range(1, 13)}
    global by_month_max
    try:
        for date, close in data.items():
            if by_month_max[date] < close:
                by_month_max[date] = close
        for m_val in range(1, 13):
            print(repr(m_val).rjust(4), repr(by_month_max[m_val]).rjust(12), end='\n')
        #     if month == int(time[1]):
        #         if maximum < num:
        #             maximum = num
        #     elif flag2 == 1:
        #         voc[str(month)] = maximum
        #         print(repr(month).rjust(4), repr(maximum).rjust(12), end='\n')
        #         month = int(time[1])
        #         maximum = num
        #     else:
        #         flag2 = 1
        #         month = int(time[1])
        #         maximum = num
        # voc[str(month)] = maximum
    except:
        print('Неправильный формат данных')
        logging.error('Неправильный формат данных')


def writeFile (filename):
    try:
        f = open(filename, 'w')
        f.write('Выведены максимальное значение для цены закрытия по месяцам.\nМесяц   MAX значение\n')
        for k, v in by_month_max.items():
            f.write(str(k) +"       " + str(v) + '\n')
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
        return
    data = {}
    f.readline()
    for row in csv.reader(f, delimiter=','):
        data[int(row[0].split('-')[1])] = float(row[4])
    process(data)


def process_network(symbol, start, end):
    url = "http://www.google.com/finance/historical?q={0}&startdate={1}&enddate={2}&output=csv"
    url = url.format(symbol.upper(), quote_plus(start.strftime('%b %d, %Y')), quote_plus(end.strftime('%b %d, %Y')))
    b_data = urlopen(url).readlines()
    data = {}
    for row in b_data[1:]:  # Пропускаем первую строку с именами колонок
        smth = row.decode().strip().split(',')
        time = datetime.strptime(smth[0], '%d-%b-%y')
        data[int(datetime.strftime(time, '%m'))] = float(smth[4])
    process(data)
