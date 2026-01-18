from flask import Flask, Response, request, render_template_string

app = Flask(__name__)

# --- GÜVENLİK AYARI ---
ADMIN_PASSWORD = "omer" # Burayı istediğin şifre yapabilirsin

# --- UYGULAMA ALTYAPISI (MANIFEST) ---
@app.route('/manifest.json')
def manifest():
    res = """
    {
        "name": "Omer Pro Admin",
        "short_name": "OmerPro",
        "start_url": "/",
        "display": "standalone",
        "background_color": "#000",
        "theme_color": "#ff4500",
        "icons": [{"src": "https://cdn-icons-png.flaticon.com/512/842/842145.png", "sizes": "512x512", "type": "image/png"}]
    }
    """
    return Response(res, mimetype='application/json')

@app.route('/')
def index():
    return f"{stil} {meta_tags} {nav} {html_content}"

# --- YÖNETİCİ PANELİ ROTASI ---
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        if request.form.get('password') == ADMIN_PASSWORD:
            return f"{stil} {admin_panel_html}"
        return "Şifre Yanlış!"
    
    return f"""
    {stil}
    <div class="container" style="padding-top:100px; text-align:center;">
        <div class="card">
            <h2>YÖNETİCİ GİRİŞİ</h2>
            <form method="POST">
                <input type="password" name="password" placeholder="Yönetici Şifresi">
                <button class="btn-lux">GİRİŞ YAP</button>
            </form>
        </div>
    </div>
    """

stil = """
<style>
    :root { --main: #ff4500; --bg: #000; --glass: rgba(255, 255, 255, 0.03); --border: rgba(255, 255, 255, 0.1); --accent: #00f2ff; }
    * { box-sizing: border-box; -webkit-tap-highlight-color: transparent; font-family: 'Inter', sans-serif; }
    body { background: var(--bg); color: #fff; margin: 0; padding-bottom: 90px; }
    nav { background: rgba(0,0,0,0.85); padding: 20px; text-align: center; border-bottom: 1px solid var(--border); position: sticky; top: 0; z-index: 1000; backdrop-filter: blur(20px); }
    .logo { color: var(--main); font-weight: 900; font-size: 22px; letter-spacing: 3px; text-transform: uppercase; }
    .container { width: 92%; max-width: 800px; margin: 0 auto; padding: 20px 0; }
    .card { background: var(--glass); border: 1px solid var(--border); padding: 30px; border-radius: 30px; margin-bottom: 25px; backdrop-filter: blur(15px); }
    input, select { width: 100%; padding: 18px; margin: 10px 0; border-radius: 15px; border: 1px solid var(--border); background: rgba(255,255,255,0.05); color: #fff; font-size: 16px; }
    .btn-lux { display: block; width: 100%; background: #fff; color: #000; padding: 20px; border-radius: 18px; font-weight: 900; text-align: center; border: none; cursor: pointer; text-transform: uppercase; }
    .admin-stat { background: #111; padding: 20px; border-radius: 20px; border-left: 4px solid var(--main); margin-bottom: 10px; }
</style>
"""

meta_tags = """<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no"><link rel="manifest" href="/manifest.json">"""

nav = """<nav><div class="logo">ÖMER PRO</div></nav>"""

html_content = """
<div class="container" style="text-align:center;">
    <div class="card">
        <h1>SUPREME ELITE</h1>
        <p>Hesaplama Motoru Aktif</p>
        <button class="btn-lux" onclick="window.location.href='/admin'">Yönetici Girişi (Test)</button>
    </div>
</div>
"""

admin_panel_html = """
<div class="container">
    <h1>PANEL <span style="color:var(--main);">DASHBOARD</span></h1>
    <div class="admin-stat">
        <small>AKTİF ÖĞRENCİ SAYISI</small>
        <div style="font-size:24px; font-weight:900;">12</div>
    </div>
    <div class="admin-stat">
        <small>TOPLAM KAZANÇ (AYLIK)</small>
        <div style="font-size:24px; font-weight:900; color:var(--accent);">2.388 TL</div>
    </div>
    <div class="card">
        <h3>ÖĞRENCİ LİSTESİ</h3>
        <p style="font-size:14px; color:#555;">(Yakında veritabanı ile otomatikleşecek)</p>
        <ul style="list-style:none; padding:0;">
            <li style="border-bottom:1px solid #222; padding:10px 0;">👤 Müşteri 1 - Ödeme Bekliyor</li>
            <li style="border-bottom:1px solid #222; padding:10px 0;">👤 Müşteri 2 - Program Gönderildi</li>
        </ul>
    </div>
    <button class="btn-lux" onclick="window.location.href='/'">SİTEYE DÖN</button>
</div>
"""

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
