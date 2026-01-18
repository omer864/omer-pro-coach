from flask import Flask

app = Flask(__name__)

@app.route('/')
def ana_sayfa():
    return """
    <!DOCTYPE html>
    <html lang="tr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>ÖMER PRO COACH | Personal Trainer</title>
        <style>
            body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #000; color: #fff; margin: 0; padding: 0; display: flex; justify-content: center; align-items: center; min-height: 100vh; }
            .container { width: 90%; max-width: 500px; background: #111; border: 2px solid #ff4500; border-radius: 20px; padding: 30px; text-align: center; box-shadow: 0 0 20px rgba(255, 69, 0, 0.3); }
            h1 { color: #ff4500; font-size: 28px; margin-bottom: 10px; text-transform: uppercase; }
            .tagline { font-style: italic; color: #ccc; margin-bottom: 25px; }
            .features { text-align: left; background: #222; padding: 15px; border-radius: 10px; margin-bottom: 25px; }
            .features li { list-style: none; margin-bottom: 10px; color: #eee; border-bottom: 1px solid #333; padding-bottom: 5px; }
            .features li:before { content: "🔥 "; }
            .price-box { background: #ff4500; color: #fff; padding: 15px; border-radius: 10px; margin-bottom: 25px; font-weight: bold; }
            .payment-info { font-size: 14px; background: #000; padding: 15px; border-radius: 10px; border: 1px dashed #ff4500; margin-bottom: 25px; }
            .btn { display: block; background: #25d366; color: #fff; text-decoration: none; padding: 15px; border-radius: 10px; font-weight: bold; transition: 0.3s; }
            .btn:hover { background: #128c7e; transform: scale(1.05); }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🔥 ÖMER PRO COACH 🔥</h1>
            <p class="tagline">Disiplin, Ter ve Sonuç.</p>
            
            <div class="features">
                <li>Kişiye Özel Antrenman Planı</li>
                <li>Beslenme ve Supplement Takibi</li>
                <li>7/24 WhatsApp Desteği</li>
                <li>Haftalık Form Kontrolü</li>
            </div>

            <div class="price-box">
                AYLIK ABONELİK: 199 TL
            </div>

            <div class="payment-info">
                <strong>BANKA BİLGİLERİ</strong><br>
                <strong>Alıcı:</strong> Ömer KAPLAN<br>
                <strong>IBAN:</strong> TR20 0006 2001 2200 0006 8738 89
            </div>

            <a href="https://wa.me/905301297064" class="btn">WHATSAPP İLE KAYIT OL VE BAŞLA</a>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
