goods = ['Банан (Зелений)', 23.34, 'Полуниця', 45.56, 'Картопля молода', 15.99, 'Морква мита', 57.78]
users = ['vvv@gmail.com', '1111']
admins = ['vl@admin.com', 'qwerty']
basket = []
admin_email_pattern = '@admin.com'

is_login_true = False
is_admin = False
try:
    with open('admins.txt', 'r') as admin_file:
        admin_lines = admin_file.readlines()
        admins = [line.strip().split(':') for line in admin_lines]

    with open('users.txt', 'r') as user_file:
        user_lines = user_file.readlines()
        users = [line.strip().split(':') for line in user_lines]


    while True:
        while True:
            login = input("Введіть логін: ")
            password = input("Введіть пароль: ")

            if admin_email_pattern in login:
                if [login, password] in admins:
                    print("Ви ввійшли як адміністратор")
                    is_admin = True
                    break
                else:
                    print("Логін або пароль адміністратора не вірний. Спробуйте ще раз.")
            elif [login, password] in users:
                print(f"Ви ввійшли як користувач - {login}")
                break
            else:
                print("Логін або пароль не вірний. Спробуйте ще раз.")
        while True:
            if is_admin == True:
                    print('Для виходу введіть "exit"')
                    print('Для додавання товару введіть "add"')
                    print('Для видалення товару введіть "del"')
                    answer = input("Введіть команду: ")
                    if answer == 'exit':
                        exit()
                    elif answer == "add":
                        name = input("Введіть назву товару: ")
                        price = input("Введіть ціну товару: ")
                        goods.append(name)
                        goods.append(price)
                        print("Товар додано")
                    elif answer == "del":
                        name = input("Введіть назву товару: ")
                        if name in goods:
                            goods.remove(name)
                            goods.remove(goods[goods.index(name) + 1])
                            print("Товар видалено")
                        else:
                            print("Такого товару не існує")
                    elif answer == 'exit admin':
                        is_admin = False
                        break
            else:
                counter = 0
                for i in range(0, len(goods), 2):
                    counter += 1
                    print(f"{counter} : {goods[i]}\t\t{goods[i + 1]}$")
                    print('Який продукт бажаєте купити?')
                print('Для виходу введіть "exit"')
                answer = input("Ведіть назву продукту: ")

                if answer == 'exit':
                    print('Бажаєте вийти з програми?')
                    answer = input("Ведіть так або ні: ")
                    if answer == 'так':
                        print('До побачення!')
                        exit()
                    else:
                        break
                else:
                    if answer in goods:
                        basket.append(answer)
                        print("Продукт додано до кошика")
                    else:
                        print("Такого продукту не існує")
                        continue

except Exception as e:
    print(e)