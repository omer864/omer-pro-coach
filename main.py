import os
from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>ÖMER PRO COACH</title>
        <style>
            body { background:#000; color:#fff; font-family:sans-serif; text-align:center; padding:20px; }
            .card { border:2px solid #ff4d00; padding:20px; border-radius:15px; background:#111; max-width:400px; margin:auto; box-shadow: 0 0 15px rgba(255, 77, 0, 0.5); }
            .btn { background:#ff4d00; color:#000; width:100%; padding:15px; font-weight:bold; border-radius:8px; cursor:pointer; text-decoration:none; display:block; margin-top:20px; }
            h1 { color:#ff4d00; }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🔥 ÖMER PRO COACH 🔥</h1>
            <p>Hayalindeki vücut için profesyonel destek vakti!</p>
            <hr style="border:0.5px solid #333;">
            <h3>AYLIK ABONELİK: 199 TL</h3>
            <p style="font-size:14px; color:#aaa;">Ödemeyi aşağıdaki IBAN'a yap ve dekontu gönder.</p>
            <p><strong>IBAN:</strong> TR00 0000 0000 0000 0000 0000 00</p>
            <p><strong>Alıcı:</strong> Ömer ...</p>
            <a href="https://wa.me/905301297064" class="btn">WHATSAPP İLE KAYIT OL</a>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
