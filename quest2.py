print('Привет это лучший квест в классе(но не факт).')
print('В вопросах перед вариантами ответов написан их номер.')
print('Чтобы выбрать один из них - введите номер ответа.')
print('')
print('❗️❗️И САМОЕ ГЛАВНОЕ❗️❗️:')
print('Не смейте писать номер варианта ответа, которого нет❗️❗️❗️')
print('Не надо проверять эту защиту от дураков, зачем тебе это?')
print('Ты же не дурак')
print('-----------------------------------------------------------------------')
print('Что поделать?:')
print('1)Делать уроки; 2)Играть в Fortnite; 3)Играть в CS2')
a = input()
if a == '1' or a == '3':
    if a == '1':
        print('Ну и молодец')
    elif a == '3':
        print('Какая CS?? Уж лучше иди уроки делай')
    print('Как звали детей Алексея Михайловича Романова?')
    print('1)Софья, Иван, Петр, Федор; 2)Софья, Иван, Петр, Роман')
    b = input()
    if b == '1':
        print('Ураа, правильно')
        print('Что больше?')
        print('1)√19-3√2 ; 2) √21-2√5')
        c = input()
        if c == '1':
            print('ОК, теперь русский')
            print('СДЕЛА...ЫЙ, 1)Н BKB 2)НН?')
            d = input()
            if d == '2':
                print('Все сделал, иди спи')
            else:
                print('Нет, миссия "Уроки" провалена')
        else:
            print('Нет🙁, миссия "Уроки" провалена')
    else:
        print('Какой еще Роман?')
        print('Миссия "Уроки" провалена')

elif a == '2':
    print('Ну ОК')
    print('1)Public или 2)BOX PVP ?')
    b = input()
    if b == '1':
        print('1)Хот дроп или 2)нет?')
        с = input()
        if c == '1':
            print('В вас стреляли у вас мало ХП')
            print('1)Захилиться или 2)отомстить?')
            d = input()
            if d == '1':
                print('Вы видите человека за стенкой')
                print('нападать на него с 1)правой стороны стенки или с 2)левой?')
                e = input()
                if e == '1':
                    print('Еще 1 устранение 😀')
                    print('Остался 1 человек, стрелять со 1)снеайперки или 2)побежать с дробовиком?')
                    f = input()
                    if f == '1':
                        print('Королевская победа!!!👑')
                    elif f == '2':
                        print('Вы проиграли🙁')
                    else:
                        print('А я ведь предупреждал😢😠')
                        print('Дуракам нельзя играть в мою игру😶')
                elif e == '2':
                    print('Вы проиграли🙁')
                else:
                    print('А я ведь предупреждал😢😠')
                    print('Дуракам нельзя играть в мою игру😶')
            elif d == '2':
                print('Вы проиграли🙁')
            else:
                print('А я ведь предупреждал😢😠')
                print('Дуракам нельзя играть в мою игру😶')
        elif c == '2':
            print('После вас высадились еще люди')
            print('1)Файтиться или 2)убежать?')
            l = input()
            if l == '1':
                print('Вы проиграли🙁')
            elif l == '2':
                print('Вы все равно проиграли🙁')
            else:
                print('А я ведь предупреждал😢😠')
                print('Дуракам нельзя играть в мою игру😶')
        else:
            print('А я ведь предупреждал😢😠')
            print('Дуракам нельзя играть в мою игру😶')
    elif b == '2':
        print('1)Строиться в начале или бегать 2)понизу?')
        k = input()
        if k == '1':
            print('Вашу стенку сломали')
            print('1)Ждать пока ее отредачат или 2)поставить рампу?')
            z = input()
            if z == '1':
                print('Вы проиграли🙁')
            elif z == '2':
                print('Вы отредачили раму и')
                print('выйграли 😀')
            else:
                print('А я ведь предупреждал😢😠')
                print('Дуракам нельзя играть в мою игру😶')
        elif k == '2':
            print('Вы проиграли🙁')
        else:
            print('А я ведь предупреждал😢😠')
            print('Дуракам нельзя играть в мою игру😶')
    else:
        print('А я ведь предупреждал😢😠')
        print('Дуракам нельзя играть в мою игру😶')
else:
    print('А я ведь предупреждал😢😠')
    print('Дуракам нельзя играть в мою игру😶')