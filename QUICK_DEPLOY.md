# 🚀 Quick Deploy to Render.com

## Step-by-Step Guide

### 1️⃣ Push to GitHub

```powershell
# Initialize git repository
git init

# Add all files
git add .

# Commit
git commit -m "AI Image Generator - Ready for deployment"

# Create a new repository on GitHub (go to github.com)
# Then add the remote and push:
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git branch -M main
git push -u origin main
```

### 2️⃣ Deploy on Render

1. **Go to**: https://render.com
2. **Sign Up** with your GitHub account
3. **Click**: "New +" button → "Web Service"
4. **Connect** your GitHub repository
5. **Configure**:
   - Name: `ai-image-generator` (or your choice)
   - Environment: `Python 3`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn webapp:app`
   - Instance Type: `Free`

6. **Add Environment Variables**:
   - Key: `HF_TOKEN`
   - Value: `your_huggingface_token_here`
   
   - Key: `SECRET_KEY`
   - Value: (generate one by running the command below)

7. **Click**: "Create Web Service"

### Generate Secret Key

Run this in PowerShell:
```powershell
python -c "import secrets; print(secrets.token_hex(32))"
```

Copy the output and use it as your SECRET_KEY.

---

## 🎉 That's It!

Your app will be deployed at:
```
https://ai-image-generator-xxxx.onrender.com
```

It takes about 5-10 minutes for the first deployment.

---

## 📱 Alternative: Railway.app

Even easier! Just:

1. Go to https://railway.app
2. Click "Start a New Project"
3. Choose "Deploy from GitHub repo"
4. Select your repository
5. Add environment variables:
   - `HF_TOKEN`: your Hugging Face token
   - `SECRET_KEY`: your generated secret key
6. Done! Railway auto-detects Python and deploys

---

## ⚡ For Local Testing with Production Settings

```powershell
# Set environment variables
$env:SECRET_KEY = "your-generated-secret-key"
$env:HF_TOKEN = "your_huggingface_token_here"

# Run with gunicorn (production server)
gunicorn webapp:app
```

Your app will run at http://127.0.0.1:8000

---

## 🔧 Troubleshooting

**App not starting?**
- Check environment variables are set
- Check logs in Render/Railway dashboard

**Images not generating?**
- Verify HF_TOKEN is correct
- Check if your token has proper permissions

**Database issues?**
- SQLite works fine for small apps
- For production, consider PostgreSQL (Render offers free tier)

---

## 📊 What's Deployed?

✅ Full web application  
✅ User authentication  
✅ AI image generation  
✅ Image gallery  
✅ Download functionality  
✅ Responsive design  

**Enjoy your deployed app! 🎨✨**
