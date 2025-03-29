import random

def task1():

    numbers = list(random.randint(1, 100) for i in range(5))

    a = int(input("Введите число: "))

    if a in numbers:
        print(f"Поздравляю, Вы угадали число {a}!")
    else:
        print("Нет такого числа!")

    print("Исходный список: ", numbers)


def task2():
    spisochek = list(random.randint(1, 50) for i in range(10))

    dupl = list()

    for i in spisochek:
        if spisochek.count(i) > 1 and i not in dupl:
            dupl.append(i)

    print(f"Первоначальный список: {spisochek}")

    if len(dupl) > 0:
        print(f"Список чисел, которые повторяются: {dupl}")
    else:
        print("В списке нет повторяющихся чисел")


def task3():
    weekdays = ("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье")
    a = int(input("Введите количество желаемых выходных на неделе: "))
    if 0<=a<=7:
        print(f"Ваши выходные дни: {weekdays[7-a:7]}")
        print(f"Ваши рабочие дни: {weekdays[:7-a]}")
    else:
        print("Ошибка: в неделе семь дней.")

def task4():
    mv4 = ["Абраменко", "Малахов", "Ярошевская", "Оржаховская", "Шахбалаева", "Добров", "Сажнев", "Гиносян", "Григорьева", "Гафуров"]
    g2 = ["Иванов", "Смирнов", "Сидоров", "Козлов", "Петров", "Яковлев", "Васильев", "Воробьев", "Федоров", "Подопригора"]
    team1 = tuple(random.sample(mv4, 5))
    team2 = tuple(random.sample(g2, 5))
    team = team1 + team2

    print(f"Наша группа: {mv4}\nДругая группа: {g2}\nКоманда: {team}\nДлина кортежа: {len(team)} ")

    alphteam = tuple(sorted(team))
    print("Отсортированная по алфавиту команда:", alphteam)

    ivanov = team.count("Иванов")
    if ivanov > 0:
        print(f"Фамилия 'Иванов' есть в команде, встречается {ivanov} раз.")
    else:
        print("Фамилии 'Иванов' нет в команде.")

tasks = [task1, task2, task3, task4]
index = int(input("Введите номер задания (от 1 до 4): "))

if 1 <= index <= 4:
    tasks[index - 1]()
else:
    print("Ошибка: введите номер от 1 до 4.")


