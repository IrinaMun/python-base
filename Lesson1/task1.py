# ЗАДАНИЕ 1
# Человеко-ориентированное представление интервала времени
# Спросить у пользователя размер интервала (в секундах). Вывести на экран строку в зависимости от размера интервала:
# 1) до минуты: <s> сек;
# 2) до часа: <m> мин <s> сек;
# 3) до суток: <h> час <m> мин <s> сек;
# 4) сутки или больше: <d> дн <h> час <m> мин <s> сек
# Например, если пользователь введет 4567 секунд, вывести:
# 1 час 16 мин 7 сек

u_sec = int(input('Для расчета времени введите нужное вам количество секунд: '))

minutes = u_sec // 60
seconds = u_sec % 60
hours = minutes // 60
minutes = minutes % 60
days = hours // 24
hours = hours % 24

if u_sec <= 59:
    print("%2d sec" % seconds)
elif 60 <= u_sec <= 3600:
    print("%2d min %2d sec" % (minutes, seconds))
elif 3600 <= u_sec <= 86390:
    print("%2d h %2d min %2d sec" % (hours, minutes, seconds))
elif u_sec >= 86400:
    print("%2dd %2dh %2dmin %2dsec" % (days, hours, minutes, seconds))
