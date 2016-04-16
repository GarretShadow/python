import sys
import csv

def main(file_name):
    print(file_name)
    print('Данная функция выводит максимальное значение для цены закрытия по месяцам.')
    #input(AMD.csv)
    with open(file_name) as f:
        csv_file = csv.reader(f, delimiter=',')
        flag = 0
        maximum = -1
        month = -1
        print("Месяц   MAX значение")
        for row in csv_file:
            if flag == 0:
                flag = 1
                continue
            num = float(row[4])
            data = row[0].split('-')
            if month == int(data[1]):
                if maximum < num:
                    maximum = num
            else:
                #print(' {0:4d} {1:10d} '.format(month, maximum))
                print(month, '   ', maximum, '\n')
                month = int(data[1])
                maximum = num
            #massiv.append(float(row[4]))
            #print('\n'.join(float(row[4])))


if __name__ == "__main__":
    if len(sys.argv[1]) > 1:
        file_name = sys.argv[1]
        main(file_name)
    else:
        print('Необходимо указать имя файла')
