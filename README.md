# Telegram URL Uploader (4GB+ Support)

A Python-based Telegram uploader bot that downloads files from direct HTTP/HTTPS URLs and sends them to your Telegram using a **UserBot (Telethon)**. Supports large files over **4GB**.

## Features

- Download large files from direct URLs (streamed, memory efficient)
- Upload to Telegram chats, channels, or saved messages
- 4GB+ file size support (using your Telegram account)
- Koyeb/Render deploy-ready

---

## Setup Instructions

### 1. Get Telegram API Credentials

Go to [https://my.telegram.org](https://my.telegram.org):

- Create a new app
- Note your **API ID** and **API Hash**

### 2. Clone the Project

Or download the ZIP provided.

```bash
git clone https://github.com/your-repo/telegram-url-uploader.git
cd telegram-url-uploader
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment

Create a `.env` file based on `.env.example`:

```env
API_ID=your_api_id
API_HASH=your_api_hash
TARGET_USER=me   # or target username/chat_id
```

### 5. Run the Script

```bash
python url_uploader.py
```

Enter the direct download URL when prompted.

---

## Deployment (e.g., Koyeb)

- Add `Procfile` with content:  
  ```bash
  worker: python url_uploader.py
  ```

- Set secret variables in Koyeb:
  - `API_ID`
  - `API_HASH`
  - `TARGET_USER`

- Ensure persistent disk or temp storage available for large downloads.

---

## Notes

- Only direct, public download links are supported (no Google Drive or Dropbox).
- Uses a session file (`uploader_session.session`) for login.
- Your Telegram account will be prompted once for login (code via Telegram).

---

## License

MIT License
