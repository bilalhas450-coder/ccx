from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv
import logging

load_dotenv()

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

ID_INSTANCE = os.getenv("ID_INSTANCE")
API_TOKEN = os.getenv("API_TOKEN")


# Mesaj gönderme fonksiyonu (Green API kullanımı)
def send_message(phone, message):
    if not ID_INSTANCE or not API_TOKEN:
        logging.error("ID_INSTANCE veya API_TOKEN çevre değişkenleri tanımlı değil")
        return
    url = f"https://api.green-api.com/waInstance{ID_INSTANCE}/SendMessage/{API_TOKEN}"
    payload = {
        "chatId": f"{phone}@c.us",
        "message": message
    }
    try:
        resp = requests.post(url, json=payload, timeout=10)
        resp.raise_for_status()
    except Exception:
        logging.exception("Mesaj gönderilemedi")


@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json(silent=True) or {}
    incoming = (data.get("message") or "").lower()
    phone = data.get("phone")

    if not phone:
        return jsonify(status="no phone"), 400

    # Basit WhatsApp Bot Mantığı
    if "merhaba" in incoming:
        reply = "Merhaba! Ortobella’ya hoş geldiniz 👋 Size nasıl yardımcı olabilirim?"
    elif "fiyat" in incoming:
        reply = "Hangi ürünün fiyatını öğrenmek istersiniz?"
    elif "tabanlık" in incoming:
        reply = "Tabanlıklarımız kişiye özel üretilip tüm ayak yapısına uyum sağlar. Detay verebilirim."
    else:
        reply = "Anlayamadım ama yardımcı olmaktan memnuniyet duyarım 🙂"

    send_message(phone, reply)
    return jsonify(status="ok")


@app.route('/')
def home():
    return "Ortobella WhatsApp Bot Çalışıyor!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
