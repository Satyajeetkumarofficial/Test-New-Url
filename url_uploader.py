import os
import requests
from tqdm import tqdm
from telethon.sync import TelegramClient
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

# ====== CONFIG ======
api_id = int(os.getenv('API_ID'))
api_hash = os.getenv('API_HASH')
session_name = 'uploader_session'
target_user = os.getenv('TARGET_USER', '8020340814')
# =====================

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
            for chunk in r.iter_content(chunk_size=1024 * 1024):  # 1MB chunk
                if chunk:
                    f.write(chunk)
                    bar.update(len(chunk))
    return filename

def main():
    url = input("Enter Direct Download URL: ").strip()
    filename = url.split('/')[-1] or "downloaded_file"

    print("Downloading file...")
    filepath = download_file(url, filename)

    print("Connecting to Telegram...")
    client = TelegramClient(session_name, api_id, api_hash)
    client.start()

    print(f"Uploading {filename} to Telegram...")
    client.send_file(target_user, filepath, caption=f"Uploaded: {filename}")

    print("Upload complete!")
    os.remove(filepath)
    print("Local file removed.")

if __name__ == '__main__':
    main()
