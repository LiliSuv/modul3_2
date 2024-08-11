def send_email(message, recipient,  sender="university.help@gmail.com"):
    x = ['.ru', '.com', '.net', ]
    if recipient == sender:
        print (message[1])
    else:
        if any (i in recipient for i in x) and recipient.find ('@') > 0:
            if any (i in sender for i in x) and sender.find ('@') > 0:
                print (''.join (message[2]))
            else:
                print (''.join (message[0]))
        else:
            print (''.join (message[0]))
def rec():
    for i in range (6):
        recipient= recipient_[i]
        message = ('Невозможно отправить письмо с адреса university.help@gmail.com', ' на адрес ', recipient), (
            'Нельзя отправить письмо самому себе'), (
            'Письмо отправлено с адреса university.help@gmail.com', " на адрес ", recipient)
        send_email (message, recipient)
def rec_():
    sender = input ('Напишите адрес с которго вы хотите отправить письма ')
    for i in range (6):
        recipient= recipient_[i]
        message = ('Невозможно отправить письмо с адреса ', sender, ' на адрес ', recipient), (
            'Нельзя отправить письмо самому себе'), (
            'Письмо отправлено с адреса', sender, " на адрес  ", recipient, ' НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ')
        send_email (message, recipient,sender)
recipient_="ddd@mail.ru", 'dhdhff@yandex.com', "eudhf@gmail.net","university.help@gmail.com",'dhdhf.gmail.com',"ddd@mail.ry"
y = input ('Вы хотите отправить письма со своего адреса? Да или нет?')
if y == ('да'):
    rec ()
elif y == ('нет'):
    rec_ ()
else:
    print('В данной ситуации я помочь Вам не могу')





