from telethon import TelegramClient, sync
import csv
import codecs

api_id = int('*api_id*') # your api id from Telegram Api
api_hash = '*api_hash*' # your api hash from Telegram Api

client = TelegramClient('current', api_id, api_hash).start()

try:
    ch = input('Введите ник канала (в ссылке после t.me/): ').strip()
except:
    print("Неверное имя")
filename = input("Введите имя файла, для замены или создания документа с информацией о пользователях: ").lower().strip()
# choose the one that I want list users from
channel = ch
users = []

# get all the users and print them
try:
    for u in client.get_participants(channel):
        users.append({"id":u.id, "first_name":u.first_name,"last_name":u.last_name,"username":u.username})
    with codecs.open(f'{filename}.csv','w','utf-8-sig') as f:
        writer = csv.DictWriter(
            f, fieldnames=list(users[0].keys()), quoting=csv.QUOTE_NONNUMERIC)
        writer.writeheader()
        for d in users:
            writer.writerow(d)
    print(f'Файл успешно сохранен как {filename}.csv!')
except:
    print('Либо вы не являетесь администратором канала, либо канала не существует')