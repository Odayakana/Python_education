def send_email(message, recipient, *, sender="university.help@gmail.com"):
    if not check_email(recipient) or not check_email(sender):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return False

    if recipient == sender:
        print("Нельзя отправить письмо самому себе!")
        return False

    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
        return True
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
        return True


def check_email(email):
    check_list = ['ru', 'net', 'com']
    email_ = email.split('.')
    if email_[len(email_) - 1] in check_list and '@' in email:
        return True
    return False


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
