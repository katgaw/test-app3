# Vercel Deployment Guide 🚀

This guide will help you deploy your Diet Recipe Generator FastAPI app to Vercel.

## Prerequisites

- Vercel account (free at [vercel.com](https://vercel.com))
- OpenAI API key
- Git repository (GitHub, GitLab, or Bitbucket)

## Deployment Steps

### 1. Prepare Your Repository

Make sure your project structure looks like this:
```
test-app3/
├── api/
│   └── index.py          # Vercel serverless function
├── templates/
│   └── index.html        # Web interface
├── static/               # Static files (if any)
├── requirements.txt      # Python dependencies
├── vercel.json          # Vercel configuration
├── env_template.txt     # Environment template
└── README.md
```

### 2. Set Up Environment Variables

Before deploying, you'll need to set up your OpenAI API key in Vercel:

1. **Via Vercel Dashboard:**
   - Go to your project in Vercel dashboard
   - Navigate to Settings → Environment Variables
   - Add: `OPENAI_API_KEY` = `your_actual_api_key_here`

2. **Via Vercel CLI:**
   ```bash
   vercel env add OPENAI_API_KEY
   # Enter your API key when prompted
   ```

### 3. Deploy to Vercel

#### Option A: Deploy via Vercel Dashboard (Recommended)

1. **Push to Git:**
   ```bash
   git add .
   git commit -m "Add Vercel deployment configuration"
   git push origin main
   ```

2. **Import to Vercel:**
   - Go to [vercel.com/dashboard](https://vercel.com/dashboard)
   - Click "New Project"
   - Import your Git repository
   - Vercel will auto-detect it's a Python project
   - Add your environment variables
   - Click "Deploy"

#### Option B: Deploy via Vercel CLI

1. **Install Vercel CLI:**
   ```bash
   npm install -g vercel
   ```

2. **Login to Vercel:**
   ```bash
   vercel login
   ```

3. **Deploy:**
   ```bash
   vercel
   ```

4. **Add Environment Variables:**
   ```bash
   vercel env add OPENAI_API_KEY
   ```

5. **Redeploy with Environment Variables:**
   ```bash
   vercel --prod
   ```

### 4. Configure Domain (Optional)

- Vercel provides a free `.vercel.app` domain
- You can add a custom domain in Project Settings → Domains

## Important Configuration Notes

### Vercel.json Configuration

The `vercel.json` file configures:
- **Builds**: Python serverless function and static files
- **Routes**: All requests go to the FastAPI app
- **Environment**: Links to your OpenAI API key

### API Structure

The `api/index.py` file:
- Contains the same FastAPI app as `main.py`
- Includes Vercel serverless function handler
- Avoids proxy conflicts by not passing proxy parameters to OpenAI client

### Dependency Management

The `requirements.txt` includes:
- `httpx==0.27.0`: Ensures compatible HTTP client version
- `openai==1.51.0`: Latest OpenAI SDK without proxy conflicts

## Troubleshooting

### Common Issues

1. **"Module not found" errors:**
   - Ensure all dependencies are in `requirements.txt`
   - Check that `api/index.py` imports are correct

2. **"OpenAI API key not found" errors:**
   - Verify environment variable is set in Vercel dashboard
   - Check variable name is exactly `OPENAI_API_KEY`

3. **Proxy/HTTP errors:**
   - The configuration avoids proxy conflicts
   - OpenAI client is initialized without proxy parameters

4. **Build failures:**
   - Check Python version compatibility
   - Ensure all file paths are correct

### Environment Variables in Vercel

To check your environment variables:
```bash
vercel env ls
```

To update an environment variable:
```bash
vercel env rm OPENAI_API_KEY
vercel env add OPENAI_API_KEY
```

## Local Development with Vercel

You can test your Vercel deployment locally:

```bash
# Install Vercel CLI
npm install -g vercel

# Run local development server
vercel dev
```

This will:
- Simulate Vercel's serverless environment
- Use your local `.env` file
- Run on `http://localhost:3000`

## Performance Considerations

- **Cold Starts**: First request may be slower due to serverless cold start
- **Memory Limits**: Vercel free tier has memory limits (1GB)
- **Timeout**: Functions timeout after 10 seconds (free tier)

## Cost

- **Free Tier**: Includes 100GB bandwidth, 1000 function invocations
- **Pro Tier**: $20/month for higher limits and better performance

## Security

- API keys are stored securely in Vercel's environment variables
- No sensitive data is committed to your repository
- HTTPS is enabled by default

## Monitoring

- Check function logs in Vercel dashboard
- Monitor performance metrics
- Set up alerts for errors

---

Your Diet Recipe Generator is now ready to serve users worldwide! 🌍✨
