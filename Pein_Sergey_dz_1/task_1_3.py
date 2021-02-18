# 1-процент, 2 - 4 - процента, 0,5 - 20 - процентов
name = ''
for num in range(0, 21):

    if num == 1:
        name = 'процент'
    elif 2 <= num <= 4:
        name = 'процента'
    else:
        name = 'процентов'

    print(f'{num} {name}')
