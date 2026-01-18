from flask import Flask, Response, request, redirect, url_for

app = Flask(__name__)

# --- SİSTEM AYARLARI ---
ADMIN_PASSWORD = "omer"
db_students = [] # Veritabanı (İsim, Hedef, Ödeme Durumu)
stats = {"total_earned": 0, "active_plans": 0}

# --- MOBİL UYGULAMA ALTYAPISI ---
@app.route('/manifest.json')
def manifest():
    res = """{"name": "Omer Pro Elite", "short_name": "OmerPro", "start_url": "/", "display": "standalone", "background_color": "#000", "theme_color": "#ff4500", "icons": [{"src": "https://cdn-icons-png.flaticon.com/512/842/842145.png", "sizes": "512x512", "type": "image/png"}]}"""
    return Response(res, mimetype='application/json')

# --- ANA SAYFA (MÜŞTERİ VİTRİNİ) ---
@app.route('/')
def index():
    return f"{stil} {meta_tags} {nav} {html_client_content}"

# --- ADMİN PANELİ
