
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return f"{stil} {nav} {html_content}"

stil = """
<style>
    :root { --main: #ff4500; --bg: #000; --glass: rgba(255, 255, 255, 0.03); --border: rgba(255, 255, 255, 0.1); --accent: #00f2ff; }
    * { box-sizing: border-box; scroll-behavior: smooth; font-family: 'Inter', sans-serif; }
    body { background: var(--bg); color: #fff; margin: 0; overflow-x: hidden; }
    
    /* 1. LÜKS ARAYÜZ: GLASSMORPHISM & ANIMATION */
    nav { background: rgba(0,0,0,0.85); padding: 20px 8%; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--border); position: sticky; top: 0; z-index: 1000; backdrop-filter: blur(25px); }
    .logo { color: var(--main); font-weight: 900; font-size: 24px; letter-spacing: 3px; text-transform: uppercase; }
    
    .container { width: 92%; max-width: 1200px; margin: 0 auto; padding: 40px 0; }
    .card { background: var(--glass); border: 1px solid var(--border); padding: 40px; border-radius: 35px; backdrop-filter: blur(15px); transition: 0.6s cubic-bezier(0.16, 1, 0.3, 1); }
    .card:hover { transform: scale(1.01); border-color: var(--main); box-shadow: 0 40px 100px rgba(255, 69, 0, 0.1); }

    /* 2. PSİKOLOJİK GÜVEN KATMANI: İKONLAR VE TAAHHÜTLER */
    .trust-badge { display: flex; align-items: center; gap: 10px; font-size: 12px; color: #777; font-weight: 600; text-transform: uppercase; margin-bottom: 20px; }
    .trust-badge span { color: var(--accent); }

    .hero h1 { font-size: clamp(3.5rem, 12vw, 7rem); margin: 0; font-weight: 950; text-align: center; letter-spacing: -4px; line-height: 0.85; background: linear-gradient(to bottom, #fff, #444); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }

    /* FORM & MOTOR */
    .grid-input { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; }
    input, select { width: 100%; padding: 20px; margin: 10px 0; border-radius: 18px; border: 1px solid var(--border); background: rgba(255,255,255,0.05); color: #fff; font-size: 16px; transition: 0.3s; }
    input:focus { border-color: var(--main); background: rgba(255,69,0,0.05); }

    .btn-supreme { display: block; width: 100%; background: #fff; color: #000; text-decoration: none; padding: 25px; border-radius: 22px; font-weight: 900; text-align: center; text-transform: uppercase; font-size: 18px; transition: 0.5s; border: none; cursor: pointer; margin-top: 25px; box-shadow: 0 10px 30px rgba(255,255,255,0.1); }
    .btn-supreme:hover { background: var(--main); color: #fff; transform: translateY(-5px); box-shadow: 0 20px 40px rgba(255, 69, 0, 0.3); }

    /* 3. KAPSAMLI MAKRO DASHBOARD */
    #macro-hub { display: none; margin-top: 40px; border-radius: 30px; background: rgba(0,0,0,0.5); padding: 30px; border: 1px solid var(--border); animation: slideUp 0.8s ease; }
    @keyframes slideUp { from { opacity: 0; transform: translateY(50px); } to { opacity: 1; transform: translateY(0); } }
</style>
"""

nav = """
<nav>
    <div class="logo">ÖMER PRO</div>
    <div style="font-size:11px; font-weight:800; letter-spacing:1px;">
        <a href="#lab" style="color:#fff; text-decoration:none; margin-left:25px;">DIAGNOSTIC</a>
        <a href="#vip" style="color:var(--main); text-decoration:none; margin-left:25px;">VIP ACCESS</a>
    </div>
</nav>
"""

html_content = """
<div class="container" style="text-align:center; padding-top:100px;">
    <div class="trust-badge" style="justify-content:center;"><span>✔</span> VERIFIED COACH <span>✔</span> SCIENTIFIC PROTOCOLS</div>
    <div class="hero"><h1>ELITE<br>SYSTEM</h1></div>
    <p style="color:#666; font-size:1.3rem; max-width:600px; margin:30px auto;">Sıradanlığın ötesinde, tamamen biyometrik veriye dayalı mühendislik.</p>
</div>

<div class="container">
    <div id="lab" class="card">
        <h2 style="margin-bottom:30px; font-size:1.5rem; letter-spacing:2px;">🔬 BİYO-İSTATİSTİK LABORATUVARI</h2>
        <div class="grid-input">
            <input type="number" id="h" placeholder="Boy (cm)">
            <input type="number" id="w" placeholder="Kilo (kg)">
            <input type="number" id="age" placeholder="Yaş">
        </div>
        <div class="grid-input" style="margin-top:10px;">
            <select id="goal">
                <option value="cut">Fat Loss (Definisyon)</option>
                <option value="lean">Muscle Gain (Temiz Kütle)</option>
                <option value="bulk">Heavy Build (Hacim)</option>
            </select>
            <select id="act">
                <option value="1.2">Sedanter (Hareketsiz)</option>
                <option value="1.55">Aktif (4-5 Gün)</option>
                <option value="1.9">Elite Athlete (7 Gün)</option>
            </select>
        </div>
        <button class="btn-supreme" onclick="runSupremeEngine()">Sistemi Analiz Et</button>

        <div id="macro-hub">
            <h3 style="color:var(--main); text-align:center;">📊 STRATEJİK BESLENME PLANI</h3>
            <div class="grid-input" style="text-align:center; margin-top:20px;">
                <div style="background:var(--glass); padding:20px; border-radius:20px;">
                    <div id="cal" style="font-size:28px; font-weight:900; color:var(--main);">-</div>
                    <small style="color:#555;">GÜNLÜK KALORİ</small>
                </div>
                <div style="background:var(--glass); padding:20px; border-radius:20px;">
                    <div id="pro" style="font-size:28px; font-weight:900;">-</div>
                    <small style="color:#555;">PROTEİN (g)</small>
                </div>
                <div style="background:var(--glass); padding:20px; border-radius:20px;">
                    <div id="carb" style="font-size:28px; font-weight:900;">-</div>
                    <small style="color:#555;">KARB (g)</small>
                </div>
                <div style="background:var(--glass); padding:20px; border-radius:20px;">
                    <div id="fat" style="font-size:28px; font-weight:900;">-</div>
                    <small style="color:#555;">YAĞ (g)</small>
                </div>
            </div>
            <p id="system-note" style="text-align:center; margin-top:30px
