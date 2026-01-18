from flask import Flask, Response, request

app = Flask(__name__)

# --- YÖNETİCİ VERİLERİ ---
ADMIN_PASSWORD = "omer"
students = [] # Burası artık bir veri merkezi

@app.route('/manifest.json')
def manifest():
    res = """{"name": "Omer Pro Admin", "short_name": "OmerPro", "start_url": "/", "display": "standalone", "background_color": "#000", "theme_color": "#ff4500", "icons": [{"src": "https://cdn-icons-png.flaticon.com/512/842/842145.png", "sizes": "512x512", "type": "image/png"}]}"""
    return Response(res, mimetype='application/json')

@app.route('/')
def index():
    return f"{stil} {meta_tags} {nav} {html_content}"

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        if request.form.get('password') == ADMIN_PASSWORD:
            return render_admin_panel()
        return "Giriş Reddedildi!"
    return f"{stil} <div class='container' style='padding-top:100px; text-align:center;'><div class='card'><h2>MASTER LOGIN</h2><form method='POST'><input type='password' name='password' placeholder='Şifre' autofocus><button class='btn-lux'>SİSTEME GİR</button></form></div></div>"

@app.route('/admin/add', methods=['POST'])
def add_student():
    name = request.form.get('name')
    status = request.form.get('status') # Ödeme Durumu
    program = request.form.get('program') # Program Tipi
    if name:
        students.append({"name": name, "status": status, "program": program})
    return render_admin_panel()

@app.route('/admin/delete/<int:id>')
def delete_student(id):
    if 0 <= id < len(students):
        students.pop(id)
    return render_admin_panel()

def render_admin_panel():
    rows = ""
    for i, s in enumerate(students):
        color = "#00f2ff" if s['status'] == "Ödendi" else "#ff4444"
        rows += f"""
        <tr>
            <td style='padding:15px; border-bottom:1px solid #222;'>{s['name']}</td>
            <td style='padding:15px; border-bottom:1px solid #222;'>{s['program']}</td>
            <td style='padding:15px; border-bottom:1px solid #222; color:{color};'>{s['status']}</td>
            <td style='padding:15px; border-bottom:1px solid #222;'><a href='/admin/delete/{i}' style='color:#ff4444; text-decoration:none;'>❌</a></td>
        </tr>"""

    return f"""
    {stil}
    <div class="container">
        <h1 style='letter-spacing:5px;'>CEO <span style="color:var(--main);">PANEL</span></h1>
        
        <div style='display:grid; grid-template-columns: 1fr 1fr; gap:15px; margin-bottom:20px;'>
            <div class='card' style='text-align:center; padding:15px;'>
                <small style='color:#555;'>TOPLAM ÖĞRENCİ</small>
                <div style='font-size:24px; font-weight:900;'>{len(students)}</div>
            </div>
            <div class='card' style='text-align:center; padding:15px;'>
                <small style='color:#555;'>TAHMİNİ CİRO</small>
                <div style='font-size:24px; font-weight:900; color:var(--main);'>{len(students) * 199} TL</div>
            </div>
        </div>

        <div class="card">
            <h3>HIZLI KAYIT EKLE</h3>
            <form action="/admin/add" method="POST" style='display:grid; gap:10px;'>
                <input type="text" name="name" placeholder="Öğrenci Adı" required>
                <select name="program" style='width:100%; padding:15px; border-radius:10px; background:#111; color:#fff; border:1px solid #333;'>
                    <option>Fat Loss</option>
                    <option>Muscle Gain</option>
                    <option>VIP Coaching</option>
                </select>
                <select name="status" style='width:100%; padding:15px; border-radius:10px; background:#111; color:#fff; border:1px solid #333;'>
                    <option>Ödeme Bekliyor</option>
                    <option>Ödendi</option>
                </select>
                <button class="btn-lux" style="background:var(--main); color:#fff;">SİSTEME İŞLE</button>
            </form>
        </div>
        
        <div class="card" style='padding:0; overflow:hidden;'>
            <table style='width:100%; border-collapse: collapse; text-align:left;'>
                <tr style='background:rgba(255,255,255,0.05);'>
                    <th style='padding:15px; color:#555;'>İSİM</th>
                    <th style='padding:15px; color:#555;'>PLAN</th>
                    <th style='padding:15px; color:#555;'>DURUM</th>
                    <th style='padding:15px; color:#555;'>İŞLEM</th>
                </tr>
                {rows if rows else "<tr><td colspan='4' style='padding:20px; text-align:center; color:#444;'>Veri yok...</td></tr>"}
            </table>
        </div>
        <a href="/" class="btn-lux" style='background:none; border:1px solid #333; color:#555;'>GÜVENLİ ÇIKIŞ</a>
    </div>
    """

stil = """<style>:root { --main: #ff4500; --bg: #000; --border: rgba(255,255,255,0.1); } * { box-sizing: border-box; font-family: 'Inter', sans-serif; } body { background: var(--bg); color: #fff; margin: 0; } .container { width: 95%; max-width: 900px; margin: 0 auto; padding: 20px 0; } .card { background: rgba(255,255,255,0.03); border: 1px solid var(--border); padding: 25px; border-radius: 20px; margin-bottom: 20px; } input { width: 100%; padding: 15px; border-radius: 10px; border: 1px solid #333; background: #0a0a0a; color: #fff; } .btn-lux { display: block; width: 100%; background: #fff; color: #000; padding: 15px; border-radius: 12px; font-weight: 900; text-align: center; border: none; cursor: pointer; text-decoration:none; }</style>"""
meta_tags = """<meta name="viewport" content="width=device-width, initial-scale=1.0">"""
nav = """<nav style='padding:20px; text-align:center; border-bottom:1px solid #111;'><div style='color:#ff4500; font-weight:900; letter-spacing:2px;'>ÖMER PRO SYSTEM</div></nav>"""
html_content = """<div class="container" style="text-align:center; padding-top:50px;"><div class="card"><h1>ELITE ACCESS</h1><p style='color:#555;'>Yönetici katmanına hoş geldin Ömer.</p><a href="/admin" class="btn-lux">TERMİNALİ AÇ</a></div></div>"""

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
