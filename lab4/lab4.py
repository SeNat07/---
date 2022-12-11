import math
import random
from math import sqrt
import csv
import pylab
from matplotlib import pyplot as pl
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split

# для 3 классов
parametrs = ["продукт", "сладость", "хруст", "класс"]
products = [
    ['яблоко', 7, 7, 0],
    ['салат', 2, 5, 1],
    ['бекон', 1, 2, 2],
    ['банан', 9, 1, 0],
    ['орехи', 1, 5, 2],
    ['рыба', 1, 1, 2],
    ['сыр', 1, 1, 2],
    ['виноград', 8, 1, 0],
    ['морковь', 2, 8, 1],
    ['апельсин', 6, 1, 0],
    ['дыня', 8, 7, 0],
    ['цукини', 2, 6, 1],
    ['помело', 4, 2, 0],
    ['кальмар', 1, 1, 2],
    ['репа', 4, 9, 1],
    ['креветки', 1, 3, 2],
    ['помидор', 5, 2, 1],
    ['абрикос', 7, 4, 0],
    ['баклажан', 2, 4, 1],
    ['тыква', 4, 6, 1],
    ['перец', 4, 7, 1],
    ['творог', 2, 2, 2],
    ['лук', 1, 6, 1],
    ['фасоль', 1, 2, 2]]

products2 = [
    ['груша', 7, 7, 0],
    ['помидор', 5, 2, 1],
    ['салат', 2, 5, 1],
    ['бекон', 1, 2, 2],
    ['торт', 10, 3, 3],
    ['помидор', 5, 2, 1],
    ['шоколад', 9, 4, 3],
    ['банан', 9, 1, 0],
    ['орехи', 1, 5, 2],
    ['слойка', 5, 5, 3],
    ['сухарь', 5, 10, 3],
    ['апельсин', 6, 1, 0],
    ['дыня', 8, 7, 0],
    ['цукини', 2, 6, 1],
    ['хлеб', 3, 5, 3],
    ['помело', 4, 2, 0],
    ['кальмар', 1, 1, 2],
    ['репа', 4, 9, 1],
    ['печенье', 8, 8, 3],
    ['креветки', 1, 3, 2],
    ['вафли', 8, 10, 3],
    ['абрикос', 7, 4, 0],
    ['баклажан', 2, 4, 1],
    ['тыква', 4, 6, 1],
    ['перец', 4, 7, 1],
    ['творог', 2, 2, 2],
    ['лук', 1, 6, 1],
    ['фасоль', 1, 2, 2]]

file1 = 'data1.csv'
file2 = 'data2.csv'

dataFrame1=[]
dataFrame2=[]

# запись и чтение 1 пула даных
with open(file1, 'w', newline='', encoding='utf-16') as w_f:
    writer = csv.writer(w_f)
    writer.writerow(parametrs)
    writer.writerows(products)

with open(file1, 'r', encoding='utf-16') as r_f:
    reader = csv.DictReader(r_f, delimiter=",")
    dataFrame1=[[int(row['сладость']), int(row['хруст']), int(row['класс'])] for row in reader]

# запись и чтение 2 пула данных
with open(file2, 'w', newline='', encoding='utf-16') as w_f:
    writer = csv.writer(w_f)
    writer.writerow(parametrs)
    writer.writerows(products2)

with open(file2, 'r', encoding='utf-16') as r_f:
    reader = csv.DictReader(r_f, delimiter=",")
    dataFrame2=[[int(row['сладость']), int(row['хруст']), int(row['класс'])] for row in reader]

# классификация метрическим классификатором
def knn_class(data, test_size, k):

    # размеры выборок
    train_data = data[0:int(len(data)*(1-test_size))]
    test_data = data[int(len(data)*(1-test_size)):]

    def dist(a, b):
        return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

    result_classification = []
    count_classes = len(set([train_data[i][2] for i in range(len(train_data))]))

    for test_item in test_data:
        test_dist = [[dist(test_item[0:2], train_data[i][0:2]), train_data[i][2]] for i in range(len(train_data))]
        weight_of_class = [0] * count_classes
        for near_neighbor in sorted(test_dist)[0:k + 1]:
            weight_of_class[near_neighbor[1]] += 1
        result_classification.append(next(number_class for number_class in range(count_classes)
                                          if weight_of_class[number_class] == max(weight_of_class)))

    classifier_accuracy = sum([int(result_classification[i] == test_data[i][2])
                               for i in range(len(test_data))]) / (len(test_data))
    print("Качество метрич. классификатора", float(str(classifier_accuracy))*100, "%", "кол-во учитываемых соседей=", k)
    return result_classification

# классификация с помощью sklearn

def knn_sclearn(data, test_size, k):
    target = list(data[i][2] for i in range(len(data)))
    X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=test_size, shuffle=False, stratify=None)

    knn_classifier = KNeighborsClassifier(k)
    knn_classifier.fit(X_train, y_train)
    result_classification = knn_classifier.predict(X_test)
    print("Качество sclearn классификатора", metrics.accuracy_score(y_test, result_classification)*100, "%", "кол-во учитываемых соседей=", k)
    return result_classification

#графики
def show(type_classifier, data, test_size, k):

    train_data = data[0:int(len(data) * (1 - test_size))]
    test_data = data[int(len(data) * (1 - test_size)):]

    result_class = type_classifier(data, test_size, k)

    fig, ax = pl.subplots(figsize=(5, 5))
    scatter = ax.scatter([train_data[i][0] for i in range(len(train_data))],
                         [train_data[i][1] for i in range(len(train_data))],
                         c=[train_data[i][2] for i in range(len(train_data))],
                         marker="o",
                         alpha=0.3)

    ax.scatter([test_data[i][0] for i in range(len(test_data))],
               [test_data[i][1] for i in range(len(test_data))],
               c=result_class,
               marker="*",
               alpha=0.3)

    legend = ax.legend(*scatter.legend_elements(), title="Классы")
    ax.add_artist(legend)
    ax.title.set_text("Классификация продуктов")
    ax.set_xlabel("Сладость")
    ax.set_ylabel("Хруст")
    ax.text(0, 0, "* - тест")
    pl.show()

show(knn_class, dataFrame1, 0.4, 5)
show(knn_sclearn, dataFrame1, 0.4, 5)
show(knn_class, dataFrame2, 0.2, 3)
show(knn_sclearn, dataFrame2, 0.2, 3)

