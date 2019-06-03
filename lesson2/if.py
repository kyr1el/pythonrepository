age = int(input("Введите ваш возраст "))
gender = str(input("Введите ваш пол"))

if age <= 6:
     print('Иди в детсад')
elif age <= 17:
     print ('Иди в школу')
elif age <= 22:
     print('СЕССИЯ')
elif age <= 59:
     print('Работа')
elif age <= 64:
    if gender == "женский":
        print("Ты на пенсии")
    if gender == "мужской":
        print("Еще пять немного")



def take_figures(first,second):
    if  (first != str(first) or second != str(second)):
        return 0
    elif first == second:
        return 1
    elif (first != second and len(first) >= len(second)):
        return 2
    elif (first != second and second == 'learn'):
        return 3
print(take_figures('rre','learn'))