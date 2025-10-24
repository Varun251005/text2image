# Firebase Deployment Guide

## Prerequisites
1. **Google Cloud Account** (with billing enabled)
2. **Firebase CLI** installed
3. **Docker** installed
4. **gcloud CLI** installed

## Step-by-Step Deployment

### 1. Install Required Tools

**Install Firebase CLI:**
```powershell
npm install -g firebase-tools
```

**Install Google Cloud CLI:**
Download from: https://cloud.google.com/sdk/docs/install

### 2. Login and Setup

```powershell
# Login to Firebase
firebase login

# Login to Google Cloud
gcloud auth login

# Set your project (replace YOUR_PROJECT_ID with your Firebase project ID)
gcloud config set project YOUR_PROJECT_ID
```

### 3. Enable Required APIs

```powershell
gcloud services enable run.googleapis.com
gcloud services enable containerregistry.googleapis.com
```

### 4. Build and Deploy to Cloud Run

```powershell
# Build the Docker image
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/text2image

# Deploy to Cloud Run
gcloud run deploy text2image `
  --image gcr.io/YOUR_PROJECT_ID/text2image `
  --platform managed `
  --region us-central1 `
  --allow-unauthenticated `
  --set-env-vars "HF_TOKEN=YOUR_HF_TOKEN_HERE"
```

### 5. Update Firebase Config

Edit `.firebaserc` and replace `your-project-id` with your actual Firebase project ID.

### 6. Deploy Firebase Hosting (Optional)

```powershell
firebase init hosting
firebase deploy --only hosting
```

## Environment Variables

Set these in Cloud Run:
- `HF_TOKEN` = Your Hugging Face API token
- `SECRET_KEY` = (Auto-generated if not provided)

## Important Notes

- **Billing**: Cloud Run requires billing to be enabled
- **Free Tier**: 2 million requests/month free
- **Region**: Default is us-central1, change if needed
- **Database**: SQLite will work but consider Cloud SQL for production

## Troubleshooting

If deployment fails:
1. Check billing is enabled
2. Verify all APIs are enabled
3. Ensure Docker is running
4. Check logs: `gcloud run logs read --service=text2image`

## Quick Deploy Script

```powershell
# Set your project ID
$PROJECT_ID = "your-project-id"
$HF_TOKEN = "your-hf-token"

# Build and deploy
gcloud builds submit --tag gcr.io/$PROJECT_ID/text2image
gcloud run deploy text2image `
  --image gcr.io/$PROJECT_ID/text2image `
  --platform managed `
  --region us-central1 `
  --allow-unauthenticated `
  --set-env-vars "HF_TOKEN=$HF_TOKEN"
```

## Alternative: Simple Deployment

If Firebase seems complex, try **Render.com** instead:
1. Sign up at render.com
2. Connect GitHub repository
3. Add HF_TOKEN environment variable
4. Deploy automatically!

Much simpler, no Docker or CLI required!
