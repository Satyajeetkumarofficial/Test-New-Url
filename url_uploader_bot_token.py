import os
import requests
from tqdm import tqdm
from telegram import Bot
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID', '')

bot = Bot(token=BOT_TOKEN)

def download_file(url, filename):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        total_size = int(r.headers.get('content-length', 0))
        with open(filename, 'wb') as f, tqdm(
            desc=filename,
            total=total_size,
            unit='B',
            unit_scale=True,
            unit_divisor=1024,
        ) as bar:
            for chunk in r.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    f.write(chunk)
                    bar.update(len(chunk))
    return filename

def main():
    url = input("Enter Direct Download URL: ").strip()
    filename = url.split('/')[-1] or "downloaded_file"

    print("Downloading file...")
    filepath = download_file(url, filename)

    print("Sending file to Telegram via bot...")
    with open(filepath, 'rb') as f:
        bot.send_document(chat_id=CHAT_ID, document=f, filename=filename)

    print("Upload complete!")
    os.remove(filepath)
    print("Local file removed.")

if __name__ == '__main__':
    main()
