from telethon import TelegramClient, sync
import csv
import codecs


def public(api_id, api_hash):
    # auth
    client = TelegramClient('sphere_irens', api_id, api_hash).start()
    # request for target channel
    try:
        channel = str(input('Enter adress of channel ( in invite link AFTER t.me\\ ): ')).lower().strip()
    except:
        print("Incorrect name")
    # asking user to set the final file's name
    fname = str(input("Enter file name, for changing/creating csv file (in script directory): ")).lower().strip()
    # create final array
    users = []
    channel = client.get_entity(channel)

    # get all the users and print them
    try:
        for u in client.get_participants(channel):
            users.append({"id": u.id, "first_name":u.first_name, "last_name": u.last_name,"username": u.username})

        with codecs.open(f'{fname}.csv', 'w', 'utf-8-sig') as f:
            writer = csv.DictWriter(
              f, fieldnames=list(users[0].keys()), quoting=csv.QUOTE_NONNUMERIC)
            writer.writeheader()
            for d in users:
                writer.writerow(d)
        print(f'Файл успешно сохранен как {fname}.csv!')
    except:
        print('Либо вы не являетесь администратором канала, либо канала не существует')

