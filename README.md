# Simple Chat Agent

A simple conversational AI chat application powered by OpenAI GPT-4o-mini, ready for deployment on Render.

## Features

- Clean, modern chat interface
- Real-time AI responses using GPT-4o-mini
- Mobile-friendly responsive design
- Typing indicator animation
- Easy deployment on Render

## Deployment Instructions

1. Go to [render.com](https://render.com) and create a free account
2. Click "New +" and select "Web Service"
3. Connect your GitHub repository: `Ashoka36/simple-chat-agent-app`
4. Render will auto-detect the Python environment
5. Add environment variable:
   - Key: `OPENAI_API_KEY`
   - Value: Your OpenAI API key from [platform.openai.com](https://platform.openai.com)
6. Click "Create Web Service"
7. Once deployed, your chat app will be live at the provided URL

## Local Development

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set your OpenAI API key: `export OPENAI_API_KEY=your_key_here`
4. Run the app: `python app.py`
5. Open http://localhost:5000 in your browser

## Usage

Open the deployed URL in your browser and start chatting with the AI assistant.