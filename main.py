from flask import Flask, Response, request

app = Flask(__name__)

# --- SİSTEM VERİLERİ ---
ADMIN_PASSWORD = "omer"
students = [] # Yönetici panelinden eklediğin öğrenciler buraya gelecek

# --- PWA UYGULAMA ALTYAPISI ---
@app.route('/manifest.json')
def manifest():
    res = """
    {
        "name": "Omer Pro Coach",
        "short_name": "OmerPro",
        "start_url": "/",
        "display": "standalone",
        "background_color": "#000000",
        "theme_color": "#ff4500",
        "icons": [{"src": "https://cdn-icons-png.flaticon.com/512/842/842145.png", "sizes": "512x512", "type": "image/png"}]
    }
    """
    return Response(res, mimetype='application/json')

# --- ANA SAYFA (LÜKS MÜŞTERİ VİTRİNİ) ---
@app.route('/')
def index():
    return f"{stil} {meta_tags} {nav} {html_content}"

# --- YÖNETİCİ PANELİ (GİRİŞ & KONTROL) ---
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        if request.form.get('password') == ADMIN_PASSWORD:
            return render_admin_panel()
        return "Erişim Reddedildi!"
    return f"{stil} <div class='container' style='padding-top:100px; text-align:center;'><div class='card'><h2>MASTER ACCESS</h2><form method='POST'><input type='password' name='password' placeholder='Şifre' autofocus><button class='btn-lux'>SİSTEMİ AÇ</button></form></div></div>"

@app.route('/admin/add', methods=['POST'])
def add_student():
    name = request.form.get('name')
    status = request.form.get('status')
    program = request.form.get('program')
    if name: students.append({"name": name, "status": status, "program": program})
    return render_admin_panel()

@app.route('/admin/delete/<int:id>')
def delete_student(id):
    if 0 <= id < len(students): students.pop(id)
    return render_admin_panel()

def render_admin_panel():
    rows = ""
    for i, s in enumerate(students):
        color = "#00f2ff" if s['status'] == "Ödendi" else "#ff4444"
        rows += f"<tr><td>{s['name']}</td><td>{s['program']}</td><td style='color:{color};'>{s['status']}</td><td><a href='/admin/delete/{i}' style='text-decoration:none;'>❌</a></td></tr>"
    
    return f"""
    {stil}
    <div class="container">
        <h1 style='text-align:center;'>CEO <span style="color:var(--main);">DASHBOARD</span></h1>
        <div style='display:grid; grid-template-columns: 1fr 1fr; gap:10px; margin-bottom:20px;'>
            <div class='card' style='text-align:center;'> <small>ÖĞRENCİ</small><br><b>{len(students)}</b> </div>
            <div class='card' style='text-align:center;'> <small>CİRO</small><br><b style='color:var(--main);'>{len(students)*199} TL</b> </div>
        </div>
        <div class="card">
            <h3>ÖĞRENCİ EKLE</h3>
            <form action="/admin/add" method="POST">
                <input type="text" name="name" placeholder="İsim Soyisim" required>
                <select name="program" class="sel-lux"><option>Fat Loss</option><option>Muscle Gain</option><option>VIP Coaching</option></select>
                <select name="status" class="sel-lux"><option>Ödeme Bekliyor</option><option>Ödendi</option></select>
                <button class="btn-lux" style="background:var(--main); color:#fff; border:none;">SİSTEME İŞLE</button>
            </form>
        </div>
        <div class="card" style='padding:0;'>
            <table>
                <tr><th>İSİM</th><th>PLAN</th><th>DURUM</th><th>SİL</th></tr>
                {rows if rows else "<tr><td colspan='4'>Veri yok...</td></tr>"}
            </table>
        </div>
        <a href="/" class="btn-lux">VİTRİNE DÖN</a>
    </div>
    """

# --- TASARIM VE İÇERİK BİLEŞENLERİ ---
stil = """
<style>
    :root { --main: #ff4500; --bg: #000; --border: rgba(255,255,255,0.1); }
    * { box-sizing: border-box; font-family: 'Inter', sans-serif; -webkit-tap-highlight-color: transparent; }
    body { background: var(--bg); color: #fff; margin: 0; padding-bottom: 100px; }
    .container { width: 92%; max-width: 800px; margin: 0 auto; }
    .card { background: rgba(255,255,255,0.03); border: 1px solid var(--border); padding: 25px; border-radius: 25px; margin-top: 20px; backdrop-filter: blur(10px); }
    input, .sel-lux { width: 100%; padding: 16px; margin: 8px 0; border-radius: 12px; border: 1px solid #333; background: #0a0a0a; color: #fff; font-size: 16px; }
    .btn-lux { display: block; width: 100%; background: #fff; color: #000; padding: 18px; border-radius: 15px; font-weight: 900; text-align: center; text-decoration: none; margin-top: 15px; border: none; cursor: pointer; }
    table { width: 100%; border-collapse: collapse; margin-top: 10px; font-size: 14px; }
    th, td { padding: 15px; text-align: left; border-bottom: 1px solid #111; }
    .tab-bar { position: fixed; bottom: 0; left: 0; width: 100%; background: rgba(10,10,10,0.95); display: flex; justify-content: space-around; padding: 15px; border-top: 1px solid var(--border); z-index: 1000; }
    .tab-item { color: #555; text-decoration: none; font-size: 11px; text-align: center; font-weight: bold; }
</style>
"""

meta_tags = """<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no"><link rel="manifest" href="/manifest.json"><meta name="apple-mobile-web-app-capable" content="yes">"""

nav = """<nav style='padding:20px; text-align:center; border-bottom:1px solid #111; position:sticky; top:0; background:black; z-index:100;'><div style='color:var(--main); font-weight:900; letter-spacing:3px;'>ÖMER PRO</div></nav>"""

html_content = """
<div class="container">
    <div style="text-align:center; padding: 40px 0;">
        <h1 style="font-size:3rem; margin:0; line-height:1;">SUPREME<br><span style="color:var(--main);">COACHING</span></h1>
        <p style="color:#555;">Bilimsel Veri ve Lüks Tasarımın Birleşimi</p>
    </div>

    <div id="engine" class="card">
        <h2 style="margin-top:0;">🔬 BIOMETRIC ENGINE</h2>
        <input type="number" id="h" placeholder="Boy (cm)">
        <input type="number" id="w" placeholder="Kilo (kg)">
        <input type="number" id="age" placeholder="Yaş">
        <select id="goal" class="sel-lux">
            <option value="cut">Fat Loss (Yağ Yakımı)</option>
            <option value="bulk">Massive Bulk (Hacim)</option>
        </select>
        <button class="btn-lux" onclick="run()">HESAPLA</button>
        <div id="res" style="display:none; margin-top:20px; padding:20px; background:rgba(255,69,0,0.1); border-radius:15px; border:1px solid var(--main);">
            <p>Günlük Kalori: <b id="c" style="color:var(--main);"></b></p>
            <p>Protein: <b id="p"></b>g</p>
            <a id="wa" href="" class="btn-lux" style="background:var(--main); color:#fff;">VIP KAYDI BAŞLAT</a>
        </div>
    </div>

    <div class="card" style="text-align:center; border: 1px solid var(--main);">
        <h3 style="margin:0; color:var(--main);">VIP ACCESS</h3>
        <p>Aylık 199 TL</p>
        <div style="background:#000; padding:15px; border-radius:12px; font-size:13px;">
            <b>ÖMER KAPLAN</b><br>
            <span style="color:#00f2ff;">TR20 0006 2001 2200 0006 8738 89</span>
        </div>
    </div>
</div>

<div class="tab-bar">
    <a href="/" class="tab-item" style="color:var(--main);">🏠<br>HOME</a>
    <a href="#engine" class="tab-item">🔬<br>ENGINE</a>
    <a href="/admin" class="tab-item">🔑<br>ADMIN</a>
</div>

<script>
function run(){
    let h=document.getElementById('h').value, w=document.getElementById('w').value, a=document.getElementById('age').value;
    if(!h||!w||!a)return;
    let cal = Math.round(((10*w)+(6.25*h)-(5*a)+5)*1.5);
    document.getElementById('c').innerText = cal;
    document.getElementById('p').innerText = w*2;
    document.getElementById('res').style.display='block';
    document.getElementById('wa').href = "https://wa.me/905301297064?text=Selam Ömer Hocam, verilerim Boy:"+h+" Kilo:"+w+" VIP Kayıt olmak istiyorum.";
}
</script>
"""

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
