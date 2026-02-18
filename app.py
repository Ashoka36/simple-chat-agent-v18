from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    # Simple bot logic
    bot_response = f"Hi! You said: '{user_message}'. I am your simple chat agent, successfully hosted on Render!"
    return jsonify({"response": bot_response})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
