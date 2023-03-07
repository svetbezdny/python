import pandas as pd
from  os import listdir
from time import time


# раскомментировать нужную строку
         
period = pd.to_datetime('today').strftime('%Y-%m')                              # текущий месяц в формате yyyy-mm
# period = (pd.to_datetime('today') - pd.offsets.Day(30)).strftime('%Y-%m')     # предыдущий месяц в формате yyyy-mm


start = time()

path = '.' # путь к папке
file_name = f'file_{period[-2:] + period[:4]}.xlsx'  # имя сохраняемого файла

lst = [i for i in listdir(path+period) if i.lower().endswith('.csv')]   # список файлов в папке

try:
    excel1 = pd.DataFrame()
    done_lst = []
    for file in lst: 
        try:
            data1 = pd.read_csv(path + period + '/' + file, header=None, encoding='utf-8')  # цикл для utf-8
            done_lst.append(file)
        except:
            continue
        excel1 = pd.concat([excel1, data1])

    excel2 = pd.DataFrame()
    for file in [i for i in lst if i not in done_lst]:  # список файлов после первого цикла
        data2 = pd.read_csv(path + period + '/' + file, header=None, encoding='cp1251') # цикл для windows
        excel2 = pd.concat([excel2, data2])

    pd.concat([excel1, excel2]).to_excel(f'{path}/{file_name}', sheet_name='data', header=False, index=False)
except Exception:
    print('Ошибка в обработке файла:', Exception)

print('Обработка файлов окончена.') 
print(f'Файл {file_name} софрмирован.')
print(f'Время - {round(time() - start, 2)} сек.')