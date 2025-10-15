# Diet Recipe Generator 🍽️

A beautiful FastAPI web application that generates personalized dinner recipes based on your dietary preferences using OpenAI's GPT-4.

## Features

- 🥗 **Dietary Preferences**: Choose from Vegetarian, Vegan, or No Restrictions
- 🤖 **AI-Powered**: Uses OpenAI GPT-4 for intelligent recipe generation
- 🎨 **Beautiful UI**: Modern, responsive design with gradient backgrounds
- 🔒 **Secure**: API keys are not stored, used only for the request
- ⚡ **Fast**: Built with FastAPI for high performance
- 🐍 **Python 3.13 Compatible**: Uses the latest Python features

## Requirements

- Python 3.13+
- OpenAI API key

## Installation

1. **Clone or download the project**
   ```bash
   cd test-app3
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your OpenAI API key**
   ```bash
   # Copy the environment template
   cp env_template.txt .env
   
   # Edit the .env file and add your actual API key
   # Replace 'your_openai_api_key_here' with your real OpenAI API key
   ```

## Usage

1. **Get your OpenAI API key**
   - Visit [OpenAI Platform](https://platform.openai.com/api-keys)
   - Create a new API key
   - Add it to your `.env` file (see installation step 4)

2. **Run the application**
   ```bash
   python main.py
   ```

3. **Open your browser**
   - Go to `http://localhost:8000`
   - Select your dietary preference
   - Click "Generate My Recipe"

## API Endpoints

### GET `/`
- Serves the main web interface

### POST `/generate-recipe`
- Generates a recipe based on dietary preferences
- **Parameters:**
  - `dietary_preference`: `vegetarian`, `vegan`, or `no_restrictions`
- **Returns:** JSON with recipe details
- **Note:** API key is automatically loaded from environment variables

## Example Usage

```bash
curl -X POST "http://localhost:8000/generate-recipe" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "dietary_preference=vegetarian"
```

## Project Structure

```
test-app3/
├── main.py              # FastAPI application
├── requirements.txt     # Python dependencies
├── env_template.txt     # Environment variables template
├── .env                 # Your environment variables (create this)
├── templates/
│   └── index.html      # Web interface template
├── static/             # Static files (currently empty)
└── README.md           # This file
```

## Dependencies

- **FastAPI 0.115.6**: Modern, fast web framework
- **OpenAI 1.51.0**: Official OpenAI Python client
- **Uvicorn**: ASGI server for FastAPI
- **Jinja2**: Template engine
- **Pydantic**: Data validation

## Security Notes

- 🔒 API keys are stored securely in your local `.env` file
- 🔒 Keys are loaded from environment variables at runtime
- 🔒 No user data is persisted
- 🔒 The `.env` file is not tracked by git (add it to `.gitignore`)

## Troubleshooting

### Common Issues

1. **"OpenAI API key not found" error**
   - Make sure you've created a `.env` file with your API key
   - Verify the `.env` file contains `OPENAI_API_KEY=your_actual_key_here`
   - Check that your API key has sufficient credits

2. **"Error generating recipe" error**
   - Verify your OpenAI API key is valid in the `.env` file
   - Check your internet connection
   - Ensure you have OpenAI API credits

3. **Port already in use**
   - The app runs on port 8000 by default
   - If busy, modify `main.py` to use a different port

### Development

To run in development mode with auto-reload:
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## License

This project is open source and available under the MIT License.

## Deployment

### Deploy to Vercel (Recommended)

This app is configured for easy deployment to Vercel:

1. **Push to Git repository** (GitHub, GitLab, or Bitbucket)
2. **Connect to Vercel** and import your repository
3. **Set environment variables** in Vercel dashboard:
   - `OPENAI_API_KEY`: Your OpenAI API key
4. **Deploy!** Vercel will automatically build and deploy

For detailed deployment instructions, see [DEPLOYMENT.md](DEPLOYMENT.md).

### Other Deployment Options

- **Railway**: Compatible with standard FastAPI deployment
- **Heroku**: Use the `main.py` entry point
- **DigitalOcean App Platform**: Standard Python deployment
- **AWS Lambda**: Requires additional serverless configuration

## Contributing

Feel free to submit issues and enhancement requests!

---

**Enjoy cooking with AI! 🍳✨**
