# 🎨 AI Image Generator Web Application

A beautiful, full-featured web application for generating AI images using Hugging Face's Stable Diffusion models. Complete with user authentication, modern UI, and responsive design.

## ✨ Features

- 🔐 **User Authentication** - Secure registration and login system
- 🎨 **AI Image Generation** - Generate images from text prompts
- 🔄 **Multiple Models** - Automatic fallback between different AI models
- 📱 **Responsive Design** - Works on desktop, tablet, and mobile
- 💾 **Download Images** - Save generated images to your device
- 🎯 **Quick Examples** - One-click example prompts
- ⚡ **Real-time Status** - Live feedback during generation

## 🚀 Quick Start

### 1. Install Dependencies

```powershell
pip install -r requirements.txt
```

### 2. Run the Application

```powershell
python webapp.py
```

### 3. Open Your Browser

Navigate to: **http://127.0.0.1:5000**

## 📖 How to Use

### First Time Users

1. **Register Account**
   - Go to http://127.0.0.1:5000
   - Click "Sign up"
   - Enter username, email, and password
   - Click "Sign Up"

2. **Login**
   - Enter your username and password
   - Click "Sign In"

3. **Generate Images**
   - Enter a detailed prompt (e.g., "A beautiful sunset over mountains")
   - Click "Generate Image"
   - Wait for the AI to create your image
   - Download or generate more images!

### Example Prompts

Try these prompts for best results:

- "A futuristic city at sunset with flying cars"
- "A cute cat wearing sunglasses on a beach"
- "A magical forest with glowing mushrooms"
- "An astronaut riding a horse on Mars"
- "A dragon flying over snow-capped mountains"

## 🛠️ Technology Stack

- **Backend**: Flask (Python web framework)
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Database**: SQLite (for user management)
- **AI API**: Hugging Face Inference API
- **Models**: Stable Diffusion XL, SD v1.4, OpenJourney, DreamLike

## 📁 Project Structure

```
image2text/
├── webapp.py              # Flask backend server
├── app.py                 # Original Gradio app (still works!)
├── requirements.txt       # Python dependencies
├── users.db              # SQLite database (auto-created)
├── templates/            # HTML templates
│   ├── login.html        # Login page
│   ├── register.html     # Registration page
│   └── dashboard.html    # Main dashboard
└── static/               # Static assets
    └── style.css         # Stylesheets
```

## 🎯 Features Explained

### Authentication System
- Secure password hashing using Werkzeug
- Session-based authentication
- SQLite database for user storage
- Protected routes requiring login

### Image Generation
- Direct API calls to Hugging Face
- Multiple model fallback for reliability
- Real-time status updates
- Base64 image encoding for instant display

### Modern UI/UX
- Gradient animations
- Smooth transitions
- Loading spinners
- Responsive grid layout
- Mobile-friendly design

## 🔧 Configuration

### Change Secret Key (Important for Production!)

Edit `webapp.py` line 12:
```python
app.secret_key = 'your-unique-secret-key-here'
```

### Add Your Own Hugging Face Token

Edit `webapp.py` line 15:
```python
HF_TOKEN = "your_token_here"
```

Or set environment variable:
```powershell
$env:HF_TOKEN = "your_token_here"
```

## 🌐 Run Both Apps

You can run both versions:

**Gradio Version** (Original):
```powershell
python app.py
# Opens at http://127.0.0.1:7864
```

**Flask Web App** (New):
```powershell
python webapp.py
# Opens at http://127.0.0.1:5000
```

## 🎨 Customization

### Add More AI Models

Edit the `MODELS` list in `webapp.py`:
```python
MODELS = [
    "stabilityai/stable-diffusion-xl-base-1.0",
    "your-model-here",
]
```

### Change Color Scheme

Edit `static/style.css` and modify the gradient colors:
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

## 🐛 Troubleshooting

### Port Already in Use
```powershell
# Change port in webapp.py (last line):
app.run(debug=True, host='0.0.0.0', port=5001)
```

### Database Errors
```powershell
# Delete and recreate database:
rm users.db
python webapp.py
```

### Image Generation Fails
- Check your Hugging Face token is valid
- Wait a moment if model is loading (503 error)
- Try a different, simpler prompt

## 📝 License

This project is open source and available for personal and educational use.

## 🙏 Credits

- **AI Models**: Stability AI, CompVis, Hugging Face
- **Framework**: Flask, Gradio
- **Design**: Custom CSS with modern gradient animations

## 💡 Future Enhancements

- [ ] Save generation history
- [ ] User galleries
- [ ] Advanced settings (size, steps, etc.)
- [ ] Social sharing
- [ ] API rate limiting
- [ ] Image editing tools

---

Made with ❤️ for AI art enthusiasts
