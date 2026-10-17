values = []
import csv
column = input("Какой столбец анализировать? ")
with open("students.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        value = float(row[column])
        values.append(value)
print(values)
print("Количество:", len(values))
print("Минимум:", min(values))
print("Максимум:", max(values))
print("Среднее:", sum(values) / len(values))