
# Deploy Talimatı

## 1. Çevre değişkenleri
Projeyi çalıştırmadan önce bir `.env` dosyası oluşturun veya çevre değişkenlerini ayarlayın. Örnek değerler için `.env.example` dosyasını kullanın.

Gerekli değişkenler:

- `ID_INSTANCE` — Green API instance id
- `API_TOKEN` — Green API token
- `PORT` — (opsiyonel) sunucu portu, default `5000`

## 2. Bağımlılıklar
Sanal ortam oluşturup bağımlılıkları yükleyin:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 3. Lokal çalıştırma
Geliştirme için:

```bash
python app.py
```

Prod için (ör. Heroku/Render):

```bash
gunicorn --bind 0.0.0.0:$PORT app:app
```

## 4. Webhook
WhatsApp/Green API tarafında webhook URL'si olarak `https://YOUR_APP_URL/webhook` ayarlayın.

Not: Bu proje Green API ile örneklenmiştir; kullandığınız servis sağlayıcıya göre endpoint ve değişken isimleri farklı olabilir.
