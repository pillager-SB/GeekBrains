# В одной минуте 60 секунд
# В одном часе 60 минут = 3600 секунд
# В сутках 24 часа = 1440 минут = 86400 секунд

# Организуем ввод секунд пользователем

duration = int(input('Введите время в секундах: '))

# Раскладываем duration в соответствии с временными интервалами,
# вычисленные данные помещаем в список timepiece для удобства манипуляций с ними.

timepiece = [duration // 86400, duration // 3600 % 24, duration // 60 % 60, duration % 60]

print(f'duration = {duration} сек\n{timepiece[0]} дн {timepiece[1]} час {timepiece[2]} мин {timepiece[3]} сек')

# **** Часть, которую вроде бы делать было не нужно? Вывод в соответствии с наличием или отсутствием минут, часов, дней
# проверяем сумму элементов, расположенных левее от рассматриваемого временного интервала, если она равна 0,
# то эти элементы не выводятся

print('*' * 64)
if sum(timepiece[:-1]) == 0:
    print(f'{timepiece[3]} сек')

elif sum(timepiece[:-2]) == 0:
    print(f'{timepiece[2]} мин {timepiece[3]} сек')

elif sum(timepiece[:-3]) == 0:
    print(f'{timepiece[1]} час {timepiece[2]} мин {timepiece[3]} сек')

else:
    print(f'{timepiece[0]} дн {timepiece[1]} час {timepiece[2]} мин {timepiece[3]} сек')
