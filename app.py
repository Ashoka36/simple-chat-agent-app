from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import openai
import os

app = Flask(__name__)
CORS(app)

# Initialize OpenAI client
client = openai.OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_message = data.get('message', '')
        
        if not user_message:
            return jsonify({'error': 'No message provided'}), 400
        
        # Call OpenAI API
        response = client.chat.completions.create(
            model='gpt-4o-mini',
            messages=[
                {'role': 'system', 'content': 'You are a helpful and friendly AI assistant. Be concise and engaging in your responses.'},
                {'role': 'user', 'content': user_message}
            ],
            max_tokens=500,
            temperature=0.7
        )
        
        ai_response = response.choices[0].message.content
        return jsonify({'response': ai_response})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))