# XRP Price Telegram Bot

A simple Python automation script that periodically fetches the live XRP price from the CoinGecko API and sends updates via a Telegram bot.

---

## Features
- Fetches real-time XRP price
- Sends periodic Telegram notifications
- Uses environment variables for secure configuration
- Scheduled execution using `schedule`

---

## Technologies
- Python
- Requests
- CoinGecko API
- Telegram Bot API
- python-dotenv

---

## How to Run

1. Create a `.env` file:

**BOT_TOKEN**=your_telegram_bot_token

**CHAT_ID**=your_chat_id

⚠️ Do not commit the `.env` file to GitHub.

2. Install dependencies:
```bash
pip install requests schedule python-dotenv
```

3. Run the script:
```bash
python xrp_message.py
```

---

## Notes

This project is intended as a small automation example demonstrating API usage and scheduled tasks in Python.