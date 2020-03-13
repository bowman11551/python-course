while True:
    print('Как тебя зовут?')
    user_name = input()
    print('Привет %s тебя ждёт увлекательный тест!' % user_name)
    value = 0

    question_list = [
            {'question': 'Сколько на нашей планете океанов?', 'answers': [
                {'text': '1. 4', 'true': False},
                {'text': '2. 5', 'true': True},
                {'text': '3. 6', 'true': False}
            ]},
            {'question': 'Единица измерения силы тока?', 'answers': [
                {'text': '1. Ампер', 'true': True},
                {'text': '2. Вольт', 'true': False},
                {'text': '3. Ватт', 'true': False}
            ]},

            {'question': 'Ag - в переодической системе Менделеева это?', 'answers': [
                  {'text': '1. Серебро', 'true': False},
                  {'text': '2. Золото', 'true': True},
                  {'text': '3. Медь', 'true': False}
             ]},
             {'question': 'Самая длинная река в мире это?', 'answers': [
                   {'text': '1. Нил', 'true': False},
                   {'text': '2. Янцзы', 'true': False},
                   {'text': '3. Амазонка', 'true': True}
             ]},
             {'question': 'Сколько хромосом в геноме человека?', 'answers': [
                    {'text': '1. 42', 'true': False},
                    {'text': '2. 44', 'true': False},
                    {'text': '3. 46', 'true': True}
             ]},
        ]

    for q in question_list:
            print(q['question'])
            for a in q['answers']:
                print(a['text'])
            answer = int(input())
            el = q['answers'][answer-1]
            if el['true'] == True:
                print('Правильно!')
                value +=  1
            else:
                print('Не правильно!')
    print("Вы набрали %s правильных ответа" % (value))

    print("Желаете пройти тест повторно? Y/N")
    reboot = str(input())
    if reboot == "N":
        print("Спасибо за прохождение! Пока!")
        break
