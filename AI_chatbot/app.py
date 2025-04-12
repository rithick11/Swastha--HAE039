from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# === Configure Gemini ===
API_KEY ="AIzaSyCPa32KFgvclHrtj8GWxQHKBl4hV4vnGqQ"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-pro")
chat = model.start_chat()

# === Routes ===
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json['message']
    try:
        response = chat.send_message(user_input)
        return jsonify({'reply': response.text})
    except Exception as e:
        return jsonify({'reply': f"❌ Error: {e}"})


if __name__ == '__main__':
    app.run(debug=True)
