#Создайте функцию send_email, которая принимает 2 обычных аргумента сообщение и получатель и 1 обязательно именованный аргумент со значением по умолчанию - отправитель.
# Если строки recipient и sender не содержит "@" или не оканчивается на ".com"/".ru"/".net", то вывести на экран(в консоль) строку: "Невозможно отправить письмо с адреса <sender> на адрес <recipient>"
# Если же sender и recipient совпадают, то вывести "Нельзя отправить письмо самому себе!"
# Если же отправитель по умолчанию - university.help@gmail.com, то вывести сообщение: "Письмо успешно отправлено с адреса <sender> на адрес <recipient>."
# В противном случае вывести сообщение: "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <sender> на адрес <recipient>."

def send_email(message, recipient, *, sender='urban.help@gmail.com'):
    ver = 0
    keys = (".com", ".ru", ".net",)
    for i in keys:
        if sender.endswith(i) and '@' in sender:
            for j in keys:
                if recipient.endswith(j) and '@' in recipient and sender == recipient:
                    ver = 1
                    break
                elif recipient.endswith(j) and '@' in recipient and sender == 'urban.info@gmail.com':
                    ver = 2
                    break
                elif recipient.endswith(j) and '@' in recipient and sender != 'urban.info@gmail.com':
                    ver = 3
                    break
                else:
                    continue
            break
        else:
            continue
    if ver == 0:
        print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
    elif ver == 1:
        print('Нельзя отправить письмо самому себе!')
    elif ver == 2:
        print('Письмо успешно отправлено с адреса', sender, 'на адрес', recipient)
    else:
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо успешно отправлено с адреса', sender, 'на адрес', recipient)

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email( 'Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
