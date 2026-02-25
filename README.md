# Simple Chat Agent

A simple conversational AI agent built with Flask and OpenAI, ready to deploy on Render.

## Features

- Clean, modern chat interface
- Powered by OpenAI GPT-4o-mini
- Responsive design for mobile and desktop
- Easy deployment to Render

## Deployment Instructions

### 1. Fork/Clone this Repository

### 2. Create a Render Account
Go to [render.com](https://render.com) and sign up for a free account.

### 3. Create a New Web Service
1. Click "New +" and select "Web Service"
2. Connect your GitHub repository
3. Select "Python" as the environment
4. Render will automatically detect the 

### 4. Set Environment Variables
Add your OpenAI API key:
- Key: `OPENAI_API_KEY`
- Value: Your OpenAI API key from [platform.openai.com](https://platform.openai.com)

### 5. Deploy
Click "Create Web Service" and Render will deploy your chat agent!

## Local Development

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set your OpenAI API key:
   ```bash
   export OPENAI_API_KEY="your-api-key-here"
   ```

3. Run the app:
   ```bash
   python app.py
   ```

4. Open http://localhost:5000 in your browser

## License

MIT