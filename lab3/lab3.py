import csv
import random
import numpy
import pandas
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

Titles = ['Id', 'Имя', 'Пол', 'Год рождения', 'Год начала работы', 'Подразделение', 'Должность', 'Оклад', 'Кол-во проектов']

Names = ['Adrian', 'Ashley', 'Charles', 'Williams', 'Earl', 'Davis', 'Elliot', 'Taylor', 'Gabriel',
         'Harry', 'Julian', 'Louis', 'Neil', 'Shayne', 'Tyler', 'Wayne', 'Nicholas']

LastNames = ['Peters', 'Gibson', 'Martin', 'Williams', 'Jordan', 'Jackson', 'Grant', 'Davis', 'Lewis',
         'Florence', 'Bronte', 'Bell', 'Adams', 'Mills', 'Evans', 'Collins', 'Campbell']

Sex = ['Жен', 'Муж']

Stores = ['Мобильная разработка', 'Работа с данными', 'HR', 'Тех. поддержка', 'Веб разработка', 'Администрирование']

Posts = ['Системный аналитик', 'Back-end разработчик', 'Front-end разработчик', 'Системный адмнистратор',
         'Руководитель отдела', 'Стажер', 'Дизайнер', 'Тестировщик']


def np_statistics(column, csv_list, headers):
    print('По параметру ' + headers[column] + '\n')
    stat = []

    for row in csv_list:
        x = int(row[column])
        stat.append(x)

    statist = numpy.array(stat)

    print('Мин. значение: ' + str(numpy.min(statist)))
    print('Макс. значение: ' + str(numpy.max(statist)))
    print('Стандарт. отклонение: ' + str(numpy.std(statist)))
    print('Дисперсия: ' + str(numpy.var(statist)))
    print('Медиана: ' + str(numpy.median(statist)))
    print('Мода: ' + str(mode(statist)) + '\n')
    print('Мат. ожидание: ' + str(numpy.mean(statist)))


def pandas_statistics(dataframe, column):
    print('По параметру ' + column + ':\n')
    print('Мин. значение: ' + str(dataframe[column].min()))
    print('Макс. значение: ' + str(dataframe[column].max()))
    print('Стандарт. отклонение: ' + str(dataframe[column].std()))
    print('Дисперсия: ' + str(dataframe[column].var()))
    print('Медиана: ' + str(dataframe[column].median()))
    print('Мода: ' + str(dataframe[column].mode()) + '\n')
    print('Мат. ожидание: ' + str(dataframe[column].mean()))


# Мода
def mode(values):
    dict = {}
    for elem in values:
        if elem in dict:
            dict[elem] += 1
        else:
            dict[elem] = 1
    v = list(dict.values())
    k = list(dict.keys())

    return k[v.index(max(v))]

# данные
with open('dataFrame.csv', 'w') as f:
    writer = csv.writer(f, lineterminator="\r")
    writer.writerow(Titles)
    for i in range(1, 1500):
        name = random.choice(Names) + " " + random.choice(LastNames)
        sex = random.choice(Sex)
        birthdate = random.randrange(1967, 2004, 1)
        stage = random.randrange(birthdate + 18, 2023, 1)
        store = random.choice(Stores)
        poste = random.choice(Posts)
        payment = random.randrange(90000, 400000, 5000)
        works = random.randrange(0, 20, 1)
        row = [i, name, sex, birthdate, stage, store, poste, payment, works]
        writer.writerow(row)

# чтение данных
my_list = list()

with open('dataFrame.csv') as f:
    reader = csv.reader(f)
    headers = next(reader)
    for row in reader:
        my_list.append(row)

np_statistics(3, my_list, headers)
np_statistics(7, my_list, headers)
np_statistics(8, my_list, headers)

df = pandas.read_csv('dataFrame.csv', header=0, index_col=0)

pandas_statistics(df, 'BirthDate')
pandas_statistics(df, 'Salary')
pandas_statistics(df, 'Works')


data = [df["Sex"].value_counts()["Муж"], df["Sex"].value_counts()["Жен"]]
plt.pie(data, labels=["Женщины", "Мужчины"])
plt.title("Диаграмма распределения полов сотрудников в компании")
plt.ylabel("")
plt.show()


graf1 = df['Store'].hist()
plt.xlabel('department')
plt.ylabel('number of employees')
plt.xticks(rotation=90)
plt.title("Количество сотрудников в отделах")
plt.show()


plt.figure(figsize=(16, 10), dpi=80)
plt.plot_date(df["Start working"], df["Salary"])
plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
plt.ylabel('salary')
plt.xlabel('dates')
plt.title("Изменение зарплаты во времени")
plt.show()
