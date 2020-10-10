from telethon import TelegramClient, sync
import csv
import codecs


def private(api_id, api_hash):
    # auth
    client = TelegramClient('sphere_irens', api_id, api_hash).start()
    # request for targeted chanel
    ch = input('Enter invite link on private channel: ').strip()
    # asking user to set the final file's name
    filename = input("Enter file name, for changing/creating csv file (in script directory): ").lower().strip()
    # Collecting entity of channel invite link
    channel = client.get_entity(ch)
    # creating final array
    users = []
    # recieving parameters and pushing them to the final array
    try:
        for u in client.get_participants(channel):
            users.append({"id":u.id, "first_name":u.first_name,"last_name":u.last_name,"username":u.username})
    # print(u.id, u.first_name, u.last_name, u.username)
        with codecs.open(f'{filename}.csv','w','utf-8-sig') as f:
            writer = csv.DictWriter(
              f, fieldnames=list(users[0].keys()), quoting=csv.QUOTE_NONNUMERIC)
            writer.writeheader()
            for d in users:
                writer.writerow(d)
        print(f'Файл успешно сохранен как {filename}.csv!')
    except:
        print('Либо вы не являетесь администратором канала, либо канала не существует')
