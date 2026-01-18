from flask import Flask, Response

app = Flask(__name__)

# Uygulama Manifestosu (Yükleme kodu altyapısı)
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
        "icons": [
            {
                "src": "https://cdn-icons-png.flaticon.com/512/842/842145.png",
                "sizes": "512x512",
                "type": "image/png"
            }
        ]
    }
    """
    return Response(res, mimetype='application/json')

@app.route('/')
def index():
    return f"{stil} {meta_tags} {nav} {html_content}"

stil = """
<style>
    :root { --main: #ff4500; --bg: #000; --glass: rgba(255, 255, 255, 0.03); --border: rgba(255, 255, 255, 0.1); --accent: #00f2ff; }
    * { box-sizing: border-box; -webkit-tap-highlight-color: transparent; font-family: 'Inter', sans-serif; }
    body { background: var(--bg); color: #fff; margin: 0; overflow-x: hidden; padding-bottom: 90px; }
    
    nav { background: rgba(0,0,0,0.85); padding: 20px; text-align: center; border-bottom: 1px solid var(--border); position: sticky; top: 0; z-index: 1000; backdrop-filter: blur(20px); }
    .logo { color: var(--main); font-weight: 900; font-size: 22px; letter-spacing: 3px; text-transform: uppercase; }

    .container { width: 92%; max-width: 800px; margin: 0 auto; padding: 20px 0; }
    .card { background: var(--glass); border: 1px solid var(--border); padding: 30px; border-radius: 30px; margin-bottom: 25px; backdrop-filter: blur(15px); transition: 0.4s; }
    .card:hover { border-color: var(--main); box-shadow: 0 20px 50px rgba(255, 69, 0, 0.1); }

    .hero h1 { font-size: clamp(2.5rem, 8vw, 5rem); font-weight: 950; text-align: center; margin: 40px 0 10px; line-height: 0.85; letter-spacing: -3px; background: linear-gradient(to bottom, #fff, #555); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
    
    input, select { width: 100%; padding: 18px; margin: 10px 0; border-radius: 15px; border: 1px solid var(--border); background: rgba(255,255,255,0.05); color: #fff; font-size: 16px; outline: none; transition: 0.3s; }
    input:focus { border-color: var(--main); background: rgba(255,69,0,0.05); }

    .btn-lux { display: block; width: 100%; background: #fff; color: #000; text-decoration: none; padding: 22px; border-radius: 20px; font-weight: 900; text-align: center; text-transform: uppercase; font-size: 16px; transition: 0.4s; border: none; cursor: pointer; margin-top: 20px; box-shadow: 0 10px 30px rgba(255,255,255,0.1); }
    .btn-lux:hover { background: var(--main); color: #fff; transform: translateY(-3px); box-shadow: 0 15px 35px rgba(255, 69, 0, 0.3); }

    #macro-hub { display: none; margin-top: 30px; border-radius: 25px; background: rgba(255,69,0,0.05); padding: 25px; border: 1px solid var(--main); animation: fadeInUp 0.6s ease; }
    @keyframes fadeInUp { from { opacity: 0; transform: translateY(30px); } to { opacity: 1; transform: translateY(0); } }

    .tab-bar { position: fixed; bottom: 0; left: 0; width: 100%; background: rgba(5,5,5,0.98); display: flex; justify-content: space-around; padding: 18px; border-top: 1px solid var(--border); z-index: 1001; backdrop-filter: blur(15px); }
    .tab-item { color: #444; text-decoration: none; font-size: 10px; text-align: center; font-weight: 800; text-transform: uppercase; }
    .tab-item.active { color: var(--main); }

    .badge { display: inline-block; padding: 6px 15px; border-radius: 50px; background: rgba(0,242,255,0.1); color: var(--accent); font-size: 10px; font-weight: 800; letter-spacing: 1px; margin-bottom: 10px; }
</style>
"""

meta_tags = """
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<link rel="manifest" href="/manifest.json">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<link rel="apple-touch-icon" href="https://cdn-icons-png.flaticon.com/512/842/842145.png">
"""

nav = """
<nav><div class="logo">ÖMER PRO</div></nav>
"""

html_content = """
<div class="container" style="text-align:center;">
    <span class="badge">CERTIFIED ELITE COACHING</span>
    <div class="hero"><h1>SUPREME<br><span style="color:var(--main);">PHYSIQUE</span></h1></div>
    <p style="color:#666; font-size:1.1rem; max-width:500px; margin:20px auto;">En ileri biyometrik algoritmalarla tasarlanmış dijital koçluk platformu.</p>
</div>

<div class="container">
    <div id="lab" class="card">
        <h2 style="margin-top:0; font-size:1.4rem; letter-spacing:1px;">🔬 DIAGNOSTIC UNIT</h2>
        <div style="display:grid; grid-template-columns: 1fr 1fr; gap:12px;">
            <input type="number" id="h" placeholder="Boy (cm)">
            <input type="number" id="w" placeholder="Kilo (kg)">
        </div>
        <input type="number" id="age" placeholder="Yaş">
        <select id="goal">
            <option value="cut">Extreme Fat Loss (Definisyon)</option>
            <option value="lean">Lean Muscle Build (Temiz Kütle)</option>
            <option value="bulk">Massive Bulk (Hacim Artışı)</option>
        </select>
        <button class="btn-lux" onclick="runEngine()">Sistemi Başlat</button>

        <div id="macro-hub">
            <h3 style="color:var(--main); text-align:center; margin-top:0; font-size:1rem; letter-spacing:2px;">BİYOMETRİK VERİLER</h3>
            <div style="display:grid; grid-template-columns: 1fr 1fr; gap:15px; text-align:center;">
                <div style="background:rgba(0,0,0,0.5); padding:20px; border-radius:22px; border:1px solid var(--border);">
                    <small style="color:#555;">GÜNLÜK KALORİ</small>
                    <div id="cal" style="font-size:24px; font-weight:900; color:var(--main);">-</div>
                </div>
                <div style="background:rgba(0,0,0,0.5); padding:20px; border-radius:22px; border:1px solid var(--border);">
                    <small style="color:#555;">PROTEİN (g)</small>
                    <div id="pro" style="font-size:24px; font-weight:900; color:#fff;">-</div>
                </div>
            </div>
            <a id="wa_app" href="https://wa.me/905301297064" class="btn-lux" style="background:var(--main); color:#fff; margin-top:25px;">VIP PROGRAMI AKTİF ET</a>
        </div>
    </div>

    <div id="vip" class="card" style="text-align:center; border: 1px solid var(--main);">
        <h2 style="color:var(--main); margin-top:0; letter-spacing:3px;">VIP ACCESS</h2>
        <p style="font-size:14px; color:#888;">Özel Antrenman, Beslenme ve 7/24 Teknik Takip.</p>
        <div style="font-size:42px; font-weight:950; margin:20px 0;">199 TL <span style="font-size:14px; color:#444;">/ AY</span></div>
        <div style="background:#000; padding:20px; border-radius:20px; border:1px solid var(--border); margin-bottom:10px;">
            <p style="font-size:11px; margin:0; color:#666; text-transform:uppercase; letter-spacing:1px;">Resmi Ödeme Bilgileri</p>
            <p style="font-size:14px; margin:10px 0; font-weight:800;">ALICI: ÖMER KAPLAN</p>
            <p style="font-size:14px; margin:5px 0; color:var(--accent); font-weight:900;">TR20 0006 2001 2200 0006 8738 89</p>
        </div>
        <p style="font-size:10px; color:#444; margin-top:15px;">*Ödeme sonrası WhatsApp üzerinden dekont iletiniz.</p>
    </div>
</div>

<div class="tab-bar">
    <a href="#" class="tab-item active">🏠<br>HOME</a>
    <a href="#lab" class="tab-item">🔬<br>ENGINE</a>
    <a href="https://wa.me/905301297064" class="tab-item">💬<br>COACH</a>
</div>

<script>
function runEngine() {
    let h = parseFloat(document.getElementById('h').value);
    let w = parseFloat(document.getElementById('w').value);
    let a = parseFloat(document.getElementById('age').value);
    let goal = document.getElementById('goal').value;

    if(!h || !w || !a) { alert("Sistem için tüm verileri giriniz."); return; }

    let bmr = (10 * w) + (6.25 * h) - (5 * a) + 5;
    let tdee = Math.round(bmr * 1.55);
    if(goal === 'cut') tdee -= 500; else if(goal === 'bulk') tdee += 500;
    
    document.getElementById('cal').innerText = tdee;
    document.getElementById('pro').innerText = Math.round(w * 2.2);
    document.getElementById('macro-hub').style.display = "block";

    let msg = `Merhaba Ömer Hocam, Boy:${h}, Kilo:${w}, Yaş:${a} verilerimle analiz yaptım. VIP paketinizi satın almak ve süreci başlatmak istiyorum.`;
    document.getElementById('wa_app').href = "https://wa.me/905301297064?text=" + encodeURIComponent(msg);
}
</script>
"""

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
