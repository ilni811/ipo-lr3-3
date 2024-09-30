#вводим данные с клавиатуры(день и месяц) 
day = int(input("введите день: "))
month = int(input("введите месяц: "))
#используем операторы ветвления if elif else для определение сезона и выводим значения 
if month >= 3 and month <= 5:
    print("весна")
elif month >= 6 and month <= 8:
    print ("лето")
elif month >= 9 and month <=11:
    print ("осень")
elif month == 12 or month <=3:
    print ("зима")
    #если ввели не существующий месяц то error
else: print("error")