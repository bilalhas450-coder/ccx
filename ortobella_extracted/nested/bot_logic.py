
import json

with open("product_data.json", "r", encoding="utf-8") as f:
    PRODUCTS = json.load(f)

def handle_message(payload):
    text = extract_text(payload)
    if not text:
        return {"status": "no_message"}

    text_lower = text.lower()

    if "tabanlık" in text_lower:
        return product_reply("tabanlik")

    if "ayakkabı" in text_lower:
        return product_reply("ayakkabi")

    return {
        "reply": "Ortobella’ya hoş geldiniz! Size nasıl yardımcı olabilirim? 👟"
    }

def extract_text(payload):
    try:
        return payload["entry"][0]["changes"][0]["value"]["messages"][0]["text"]["body"]
    except:
        return None

def product_reply(category):
    items = [p for p in PRODUCTS if p["category"] == category]
    if not items:
        return {"reply": "Şu an bu kategori için ürün bulunamadı."}
    msg_lines = ["Sizin için seçtiklerim:", ""]
    for p in items:
        msg_lines.append(f"• {p['name']} – {p['price']} TL")
        msg_lines.append(p.get('url', ''))
        msg_lines.append("")

    msg_lines.append("Her biri ortopedik ve konfor odaklıdır. Hangisi ile ilgilenirsiniz? 😊")
    msg = "\n".join(msg_lines)
    return {"reply": msg}
