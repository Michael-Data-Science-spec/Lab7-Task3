'''
Welcome to UCU Survival game!
'''
import _221_lvl1 as lvl1
import _221_lvl2 as lvl2
import _221_lvl3 as lvl3
import _221_case as case
import time
def timeprint(line):
    """
    Функція друкує літери у live режимі (кожна літера з певним інтервалом)
    """
    for i in line:
        print(i, end = "", flush = True)
        time.sleep(0.02)
    print()
timeprint("Welcome to UCU Survival game! \nВи перебуваєте на 3 поверсі \
Мультифункціональної будівлі УКУ. \nНазначений час сесії наближається,\
тому необхідно зробити все можливе, щоб потрапити на екзамен до пана \
Романюка якомога швидше. \nПроблема наступна: Ви на третьому поверсі, \
тим часом як пан Романюк з нетерпінням очікує на Вас у цоколі в \
ІТ просторі в аудиторії 008. \nДля того, щоб прибути в ІТ простір вчасно \
необіхно пройти три рівні. \nПравила гри першого рівня: \nВаше завдання \
- ввести необхідні числа заданого типу в порядку зростання. \nУ випадку, \
якщо потрібне число відсутнє у списку, натисніть Enter. \nBreak a leg:)")

start_tickets = 0
# because 0 is interpreted as False in python and if funca level function 
# returns False the program ends, and the level in normal case returns 
# number of tickets the player has, we needed to return the number of 
# tickets as a string to avoid the confusion
level1_tickets = lvl1.level1(start_tickets)  # is False in case user exceeds ticket limit
if level1_tickets == False:  # checks if the player exceeded ticket limit
    timeprint("На жаль, гру для вас закінчено, спробуйте зайти пізніше")
else:
    print("Вітаємо, ви пройшли перший рівень, помилившись",level1_tickets, "рази")
    timeprint("Вітаємо з досягненням другого рівня. Правила гри: \
Оберіть тип чисел, з яким ви хочете працювати. Далі вам буде задане певне \
рандомне число. Ваше завдання - ввести '1', якщо це число є даним типом чисел, \
або ж '0', якщо навпаки.")
    timeprint("Виберіть набір чисел з якими ви хочете працювати: ulam, happy, lucky: ")
    while True:
        typp = input()
        case.quit_func(typp)  # if user wants to stop the execution and types 'quit'
        if typp == 'ulam' or typp == 'lucky' or typp == 'happy':
            level2_tickets = lvl2.get_bin(typp, level1_tickets)  # is False in case user exceeds ticket limit
            break
        else:
            print("Неправильний ввід. Виберіть набір чисел з якими ви хочете \
працювати: ulam, happy, lucky: ")

    if level2_tickets == False:  # checks if the player exceeded ticket limit
        timeprint("На жаль, гру для вас закінчено, спробуйте зайти пізніше")
    else:
        print("Вітаємо, ви пройшли другий рівень, помилившись",level2_tickets, "рази")
        timeprint("Вітаємо з досягненням третього рівня. Правила гри: \n\
    Ви обираєте тип чисел, з яким хочете працювати. Буде виведено таблицю із \
рандомними числами у вигляді прямокутника. Ваше завдання - ввести ті числа, \
які не відносяться до вибраного вами типу чисел. Після цього залишуться лише \
необхідні числа, з яких вийде патерн букви, яку необхідно ввести як результат \
(З великої літери).")
        print("Оберіть набір чисел з якими ви хочете працювати: ulam, happy, lucky:")
        while True:
            typp = input()
            case.quit_func(typp)  # if user wants to stop the execution and types 'quit'
            if typp == 'ulam' or typp == 'lucky' or typp == 'happy':
                level3_tickets = lvl3.quadrangle(typp, level1_tickets)  # is False in case user exceeds ticket limit
                break
            else:
                print("Неправильний ввід. Виберіть набір чисел з якими ви \
хочете працювати: ulam, happy, lucky: ")
        if level3_tickets == False:  # checks if the player exceeded ticket limit
            timeprint("На жаль, гру для вас закінчено, спробуйте зайти пізніше")
        else:
            print("Вітаємо, ви пройшли гру, помилившись", level3_tickets, "рази")
            timeprint("Для того, щоб зіграти ще раз, поставте максимальну оцінку")
a = input("Напишіть quit щоб вийти: ")
case.quit_func(a)  # if user wants to stop the execution and types 'quit'
