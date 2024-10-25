from flask import Flask, request, jsonify
import textwrap
from transformers import pipeline
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def mlmodel():
    return 0

@app.route('/process_input', methods=['POST'])
def process_input():
    data = request.get_json()
    user_text = data['user_text']
    # Process user_text with your ML/AI model
    output = mlmodel(user_text)
    return jsonify({'output': output})


app.run(debug=True)