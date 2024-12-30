from flask import render_template, request, jsonify
from app import app
from app.chatbot import get_response

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        if not request.is_json:
            return jsonify({'error': 'Request must be JSON'}), 400
        
        data = request.get_json()
        if 'message' not in data:
            return jsonify({'error': 'Message field is required'}), 400
            
        user_message = data['message']
        if not user_message or not isinstance(user_message, str):
            return jsonify({'error': 'Message must be a non-empty string'}), 400
            
        response = get_response(user_message)
        return jsonify({'response': response})
    except Exception as e:
        print(f"Error in chat endpoint: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500
