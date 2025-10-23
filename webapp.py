import os
import io
import requests
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, session, jsonify, send_file
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
from PIL import Image

app = Flask(__name__)
# Generate secure secret key: python -c "import secrets; print(secrets.token_hex(32))"
app.secret_key = os.environ.get('SECRET_KEY', 'your-secret-key-change-this-in-production')

# Hugging Face configuration
HF_TOKEN = os.environ.get("HF_TOKEN")
if not HF_TOKEN:
    raise RuntimeError("HF_TOKEN environment variable is required. Please set it before running the app.")
headers = {"Authorization": f"Bearer {HF_TOKEN}"}

# List of working Hugging Face models
MODELS = [
    "stabilityai/stable-diffusion-xl-base-1.0",
    "CompVis/stable-diffusion-v1-4",
    "prompthero/openjourney",
    "dreamlike-art/dreamlike-photoreal-2.0",
]

# Database setup
def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  username TEXT UNIQUE NOT NULL,
                  email TEXT UNIQUE NOT NULL,
                  password TEXT NOT NULL,
                  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()

init_db()

# Routes
@app.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute('SELECT * FROM users WHERE username = ?', (username,))
        user = c.fetchone()
        conn.close()
        
        if user and check_password_hash(user[3], password):
            session['user_id'] = user[0]
            session['username'] = user[1]
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error='Invalid username or password')
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        if password != confirm_password:
            return render_template('register.html', error='Passwords do not match')
        
        hashed_password = generate_password_hash(password)
        
        try:
            conn = sqlite3.connect('users.db')
            c = conn.cursor()
            c.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)',
                     (username, email, hashed_password))
            user_id = c.lastrowid
            conn.commit()
            conn.close()
            
            # Auto-login after registration
            session['user_id'] = user_id
            session['username'] = username
            return redirect(url_for('dashboard'))
        except sqlite3.IntegrityError:
            return render_template('register.html', error='Username or email already exists')
    
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html', username=session.get('username'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/generate', methods=['POST'])
def generate():
    if 'user_id' not in session:
        return jsonify({'error': 'Not authenticated'}), 401
    
    data = request.get_json()
    prompt = data.get('prompt', '').strip()
    
    if not prompt:
        return jsonify({'error': 'Please enter a prompt'}), 400
    
    print(f"\nGenerating image for: {prompt}")
    
    # Try each model until one works
    for model in MODELS:
        try:
            api_url = f"https://api-inference.huggingface.co/models/{model}"
            print(f"Trying model: {model}")
            
            response = requests.post(
                api_url,
                headers=headers,
                json={"inputs": prompt},
                timeout=60
            )
            
            if response.status_code == 200:
                print(f"✅ Success with {model}")
                # Return image as base64
                import base64
                image_base64 = base64.b64encode(response.content).decode('utf-8')
                return jsonify({
                    'success': True,
                    'image': f'data:image/png;base64,{image_base64}',
                    'model': model
                })
            elif response.status_code == 503:
                print(f"Model {model} is loading...")
                continue
            elif response.status_code == 404:
                print(f"Model {model} not found...")
                continue
            else:
                print(f"Error {response.status_code} with {model}")
                continue
                
        except Exception as e:
            print(f"Exception with {model}: {e}")
            continue
    
    return jsonify({'error': 'All models failed. Please try again later.'}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
