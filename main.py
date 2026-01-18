import os
from flask import Flask, render_template_string, request

# Flask uygulamasını tanımlıyoruz
app = Flask(__name__)

# Veritabanı ayarları
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'omer_coach.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

# Basit kullanıcı tablosu
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

# ANA SAYFA TASARIMI (VİTRİN)
html_index = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body { background:#000; color:#fff; font-family:sans-serif; text-align:center; padding:20px; }
        .card { border:2px solid #f1c40f; padding:20px; border-radius:15px; background:#111; max-width:320px; margin:auto; box-shadow: 0 0 15px rgba(241, 196, 15, 0.2); }
        .btn { background:#f1c40f; color:#000; width:100%; padding:14px; font-weight:bold; border:none; border-radius:5px; cursor:pointer; margin-top:15px; }
        input { width:90%; padding:10px; margin-bottom:10px; border-radius:5px; border:1px solid #333; background:#222; color:#fff; }
        h1 { color:#f1c40f; font-size:1.5rem; }
    </style>
</head>
<body>
    <h1>💪 ÖMER PRO COACH v1.0</h1>
    <p style="font-size:0.8rem; color:#888;">Boy: 166cm | Kilo: 55kg</p>
    <div class="card">
        <h3>💎 PREMIUM ÜYELİK</h3>
        <p style="text-align:left; font-size:0.9rem;">✅ 115g Protein Takibi<br>✅ Heavy Workout Programı<br>✅ Sert Disiplin & Koçluk</p>
        <hr style="border:0.5px solid #333;">
        <p style="font-size:1.2rem;"><b>Tutar: 199 TL / Ay</b></p>
        <form action="/odeme" method="POST">
            <input type="text" name="musteri_adi" placeholder="Adınız Soyadınız" required>
            <button type="submit" class="btn">HEMEN ABONE OL VE BAŞLA</button>
        </form>
    </div>
</body>
</html>
"""

# ÖDEME SAYFASI (PARA KAZANMA KISMI)
@app.route('/odeme', methods=['POST'])
def odeme():
    name = request.form.get('musteri_adi')
    # Ödeme bilgilerini gösteren sayfa
    return f"""
    <body style="background:#000; color:#fff; font-family:sans-serif; text-align:center; padding:20px;">
        <h1 style="color:#f1c40f;">Tebrikler {name}!</h1>
        <p>Aboneliğini başlatmak için ödemeyi tamamla:</p>
        <div style="border:2px solid #f1c40f; padding:20px; border-radius:15px; background:#111; display:inline-block; text-align:left; max-width:300px;">
            <p>🏦 <b>Banka IBAN:</b><br><span style="color:#f1c40f;">TR20 0006 2001 2200 0006 8738 89</span></p>
            <p>👤 <b>Alıcı:</b> Ömer Kaplan</p>
            <p>💰 <b>Tutar:</b> 199 TL</p>
        </div>
        <div style="margin-top:25px; padding:10px; border:1px dashed #555;">
            <p style="font-size:0.9rem;">⚠️ <b>ÖNEMLİ:</b> Ödemeyi yaptıktan sonra dekontu WhatsApp üzerinden gönderin.</p>
        </div>
        <br>
        <a href="/" style="color:#f1c40f; text-decoration:none;">🏠 Ana Sayfaya Dön</a>
    </body>
    """

@app.route('/')
def home():
    return render_template_string(html_index)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    # Render için otomatik port ayarı
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
