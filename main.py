
from flask import Flask, Response, request, redirect, url_for

app = Flask(__name__)

# --- YÖNETİCİ VERİLERİ ---
ADMIN_PASSWORD = "omer"
students = []  # Öğrenciler burada tutulacak (Geçici hafıza)

@app.route('/manifest.json')
def manifest():
    res = """{"name": "Omer Pro Admin", "short_name": "OmerPro", "start_url": "/", "display": "standalone", "background_color": "#000", "theme_color": "#ff4500", "icons": [{"src": "https://cdn-icons-png.flaticon.com/512/842/842145.png", "sizes": "512x512", "type": "image/png"}]}"""
    return Response(res, mimetype='application/json')

# --- MÜŞTERİ VİTRİNİ ---
@app.route('/')
def index():
    return f"{stil} {meta_tags} {nav} {html_content}"

# --- YÖNETİCİ PANELİ ---
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        if request.form.get('password') == ADMIN_PASSWORD:
            return render_admin_panel()
        return "Hatalı Şifre!"
    return f"{stil} <div class='container' style='padding-top:100px; text-align:center;'><div class='card'><h2>YÖNETİCİ GİRİŞİ</h2><form method='POST'><input type='password' name='password' placeholder='Şifre'><button class='btn-lux'>GİRİŞ YAP</button></form></div></div>"

# ÖĞRENCİ EKLEME İŞLEMİ
@app.route('/admin/add', methods=['POST'])
def add_student():
    name = request.form.get('name')
    goal = request.form.get('goal')
    if name:
        students.append({"name": name, "goal": goal})
    return render_admin_panel()

# ÖĞRENCİ SİLME İŞLEMİ
@app.route('/admin/delete/<int:id>')
def delete_student(id):
    if 0 <= id < len(students):
        students.pop(id)
    return render_admin_panel()

def render_admin_panel():
    student_list_html = ""
    for i, s in enumerate(students):
        student_list_html += f"""
        <div class='admin-stat' style='display:flex; justify-content:space-between; align-items:center;'>
            <div><b>{s['name']}</b> - {s['goal']}</div>
            <a href='/admin/delete/{i}' style='color:#ff4444; text-decoration:none; font-weight:900;'>SİL</a>
        </div>"""
    
    return f"""
    {stil}
    <div class="container">
        <h1>ADMİN <span style="color:var(--main);">KONTROL</span></h1>
        <div class="card">
            <h3>YENİ ÖĞRENCİ EKLE</h3>
            <form action="/admin/add" method="POST">
                <input type="text" name="name" placeholder="Öğrenci Adı Soyadı" required>
                <input type="text" name="goal" placeholder="Hedefi (Örn: Yağ Yakımı)" required>
                <button class="btn-lux" style="background:var(--main); color:#fff;">KAYDET</button>
            </form>
        </div>
        
        <div class="card">
            <h3>AKTİF ÖĞRENCİLER ({len(students)})</h3>
            {student_list_html if students else "<p style='color:#555;'>Henüz öğrenci eklenmedi.</p>"}
        </div>
        <a href="/" class="btn-lux">SİTEYE DÖN</a>
    </div>
    """

stil = """<style>:root { --main: #ff4500; --bg: #000; --glass: rgba(255, 255, 255, 0.03); --border: rgba(255, 255, 255, 0.1); --accent: #00f2ff; } * { box-sizing: border-box; font-family: 'Inter', sans-serif; } body { background: var(--bg); color: #fff; margin: 0; padding-bottom: 90px; } nav { background: rgba(0,0,0,0.85); padding: 20px; text-align: center; border-bottom: 1px solid var(--border); } .logo { color: var(--main); font-weight: 900; font-size: 22px; letter-spacing: 3px; text-transform: uppercase; } .container { width: 92%; max-width: 800px; margin: 0 auto; padding: 20px 0; } .card { background: var(--glass); border: 1px solid var(--border); padding: 30px; border-radius: 30px; margin-bottom: 25px; } input { width: 100%; padding: 18px; margin: 10px 0; border-radius: 15px; border: 1px solid var(--border); background: rgba(255,255,255,0.05); color: #fff; } .btn-lux { display: block; width: 100%; background: #fff; color: #000; padding: 20px; border-radius: 18px; font-weight: 900; text-align: center; border: none; cursor: pointer; text-decoration:none; margin-top:10px; } .admin-stat { background: #111; padding: 15px; border-radius: 15px; margin-bottom: 10px; border-left: 4px solid var(--main); }</style>"""
meta_tags = """<meta name="viewport" content="width=device-width, initial-scale=1.0"><link rel="manifest" href="/manifest.json">"""
nav = """<nav><div class="logo">ÖMER PRO</div></nav>"""
html_content = """<div class="container" style="text-align:center;"><div class="card"><h1>SUPREME SYSTEM</h1><p>Diagnostic Engine Online</p><a href="/admin" class="btn-lux">YÖNETİCİ GİRİŞİ</a></div></div>"""

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
