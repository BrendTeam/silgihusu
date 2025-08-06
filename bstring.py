from telethon.sync import TelegramClient
from telethon.sessions import StringSession

API_ID = 1558926
API_HASH = "69c4c16e17e9f637818f2cfce8f9bce5"

def main():
    print("Telefon nömrənizi yazın")

    client = TelegramClient(StringSession(), API_ID, API_HASH)
    client.start()
 
    string_session = client.session.save()
    print(f'\nAşağıdakı string sessionu kopyalayın:\n\n {string_session}\n')

if __name__ == "__main__":
    main()
