import sys
import csv

def main(file_name):
    print(file_name)
    print('Данная функция выводит максимальное значение для цены закрытия по месяцам.')
    #input(AMD.csv)
    with open(file_name) as f:
        f.readline()
        csv_file = csv.reader(f, delimiter=',')
        flag2 = 0
        maximum = -1
        month = -1
        print("Месяц   MAX значение")
        for row in csv_file:
            num = float(row[4])
            data = row[0].split('-')
            if month == int(data[1]):
                if maximum < num:
                    maximum = num
            elif flag2 == 1:
                print(repr(month).rjust(4), repr(maximum).rjust(12), end='\n')
                #print(' {0:5d} {1:5d} '.format(month, maximum))
                #print(month, '   ', maximum)
                month = int(data[1])
                maximum = num
            else:
                flag2 = 1
                month = int(data[1])
                maximum = num
            #massiv.append(float(row[4]))
            #print('\n'.join(float(row[4])))
        print(repr(month).rjust(4), repr(maximum).rjust(12), end='\n')
        #print(month, '   ', maximum)


if __name__ == "__main__":
    if len(sys.argv[1]) > 1:
        file_name = sys.argv[1]
        main(file_name)
    else:
        print('Необходимо указать имя файла')
