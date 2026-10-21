# a = 44
# b = -312
# c = 11
# cnt = 0
# if a > 0:
#     cnt += 1
# if b > 0:
#     cnt += 1
# if c > 0:
#     cnt += 1
# print(cnt)






print("Выберите тип насоса")
print("1 - цетробежный (eta = 0.75)")
print("2 - поршневой (eta = 0.85)")
print("3 - вихревой (eta = 0.55)")


pump_type = int(input("Введите номер типа (1, 2 или 3): "))
if pump_type == 1:
    eta = 0.75
    name = "центробежный"
elif pump_type == 2:
    eta = 0.85
    name = "поршневой"
elif pump_type == 3:
    eta = 0.55
    name = "вихревой"
else:
    print("Некорректный выбор типа насоса!")
    exit()

Q = float(input("Введите подачу Q(0.5..500): "))
if not (0.5 <= Q <= 500):
    print("Ошибка: Q должно быть в диапазоне от 0.5 до 500!")
    exit()

H = float(input("Введите напор H (1..200): "))
if not (1 <= H <= 200):
    print("Ошибка: H должно бытьв диапазоне от 1 до 200!")
    exit()

p = float(input("Введите плотность p (800..1200)"))
if not (800 <= p <= 1200):
    print("Ошибка p должно быть в диапазоне от 800 до 1200!")
    exit()

#3 - Расчет мощности 

g = 9.81
P = (p * g * Q * H) / (3600 * eta * 1000)

# Определение класса напора

if H < 10:
    head_class = "малый напор"
elif H <= 60:
    head_class = "средний"
else:
    head_class = "высокий класс"

print("Результат")
print(f"тип насоса: {name}")
print(f"Подача Q: {Q} м**3 / ч")
print(f"Напор H: {H} м")
print(f"Мощность P: {round(P, 2)} квт")
print(f"Класс напора: {head_class}")