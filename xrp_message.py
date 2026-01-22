import requests
import schedule
import time
from dotenv import load_dotenv
import os

load_dotenv()

# Replace with your own values
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")


def get_xrp_price():
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=ripple&vs_currencies=try"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers).json()
        return response["ripple"]["try"]
    except Exception as e:
        print(f"Error fetching price: {e}")
        return None

def send_telegram_message():
    price = get_xrp_price()
    
    if price:
        message = f"🔔 Live XRP Price: {price} TRY"
        # Using standard requests instead of the telegram library
        send_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        data = {"chat_id": CHAT_ID, "text": message}
        
        try:
            requests.post(send_url, data=data)
            print(f"Message sent! Price: {price}")
        except Exception as e:
            print(f"Failed to send Telegram message: {e}")

if __name__ == "__main__":
    # Schedule the job every 30 seconds
    schedule.every(30).seconds.do(send_telegram_message)
    
    print("Bot started ✅ Sending XRP prices every 30 seconds...")
    
    # Send one immediately to test
    send_telegram_message()
    
    while True:
        schedule.run_pending()
        time.sleep(1)