# 🚀 Deployment Guide for AI Image Generator

## Deploy to Render (Recommended - Free Tier Available)

### Step 1: Prepare Files

Already done! Your project has all necessary files.

### Step 2: Push to GitHub

```powershell
# Initialize git (if not already)
git init
git add .
git commit -m "Initial commit - AI Image Generator"

# Create a new repository on GitHub, then:
git remote add origin https://github.com/YOUR_USERNAME/ai-image-generator.git
git branch -M main
git push -u origin main
```

### Step 3: Deploy to Render

1. Go to [render.com](https://render.com)
2. Sign up with GitHub
3. Click "New +" → "Web Service"
4. Connect your GitHub repository
5. Configure:
   - **Name**: ai-image-generator
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn webapp:app`
   - **Environment Variables**: Add `HF_TOKEN` with your Hugging Face token

6. Click "Create Web Service"

Your app will be live at: `https://ai-image-generator-xxxx.onrender.com`

---

## Deploy to Railway (Alternative - Free Tier)

### Step 1: Install Railway CLI (Optional)

```powershell
npm i -g @railway/cli
```

### Step 2: Deploy

1. Go to [railway.app](https://railway.app)
2. Sign up with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Select your repository
5. Add environment variable: `HF_TOKEN`
6. Railway auto-detects Python and deploys!

---

## Deploy to PythonAnywhere (Free Forever)

### Step 1: Sign Up

1. Go to [pythonanywhere.com](https://www.pythonanywhere.com)
2. Create a free account

### Step 2: Upload Files

1. Go to "Files" tab
2. Upload all your project files or use:

```bash
git clone https://github.com/YOUR_USERNAME/ai-image-generator.git
```

### Step 3: Setup Web App

1. Go to "Web" tab
2. Click "Add a new web app"
3. Choose Flask
4. Set source code to your project folder
5. Edit WSGI configuration file:

```python
import sys
path = '/home/YOUR_USERNAME/ai-image-generator'
if path not in sys.path:
    sys.path.append(path)

from webapp import app as application
```

6. Set environment variable in web app settings
7. Click "Reload"

Your app will be at: `https://YOUR_USERNAME.pythonanywhere.com`

---

## Deploy to Heroku

### Step 1: Create Procfile (Already created below)

### Step 2: Deploy

```powershell
# Install Heroku CLI from heroku.com/cli
heroku login
heroku create your-app-name
git push heroku main
heroku config:set HF_TOKEN=your_token_here
heroku open
```

---

## 🔒 Important Before Deploying

1. **Change Secret Key** in `webapp.py`:
```python
app.secret_key = 'your-very-long-random-secret-key-here'
```

Generate a secure key:
```powershell
python -c "import secrets; print(secrets.token_hex(32))"
```

2. **Set Environment Variable** for your Hugging Face token on the hosting platform

3. **Update Database** for production (optional - SQLite works for small apps)

---

## 📊 Hosting Comparison

| Platform | Free Tier | Ease | Speed |
|----------|-----------|------|-------|
| **Render** | ✅ Yes | ⭐⭐⭐⭐⭐ | Fast |
| **Railway** | ✅ Yes | ⭐⭐⭐⭐⭐ | Fast |
| **PythonAnywhere** | ✅ Forever | ⭐⭐⭐⭐ | Medium |
| **Heroku** | ❌ No | ⭐⭐⭐⭐ | Fast |

**Recommended**: Start with **Render** or **Railway** for easiest deployment!

---

## 🎯 Quick Start (Render)

1. Push code to GitHub
2. Connect GitHub to Render
3. Add HF_TOKEN environment variable
4. Deploy!

**Need help with any specific platform? Let me know!** 🚀
