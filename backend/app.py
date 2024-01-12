from flask import Flask, request, jsonify
from flasgger import Swagger
import requests
import os
from openai import OpenAI
from flask_cors import CORS
from dotenv import load_dotenv


app = Flask(__name__)
Swagger(app)
CORS(app)
load_dotenv()

OCR_API_KEY = secret_key = os.environ.get('OCR_API_KEY', 'default_value_if_not_present')  # Replace with your OCR API key
os.environ["OPENAI_API_KEY"] = os.environ.get('OPENAI_API_KEY', 'default_value_if_not_present')

# OCR api
@app.route('/ocr', methods=['POST'])
def ocr():
    """
    OCR API
    ---
    consumes:
      - multipart/form-data
    parameters:
      - name: image
        in: formData
        type: file
        required: true
        description: The image file to process
    responses:
      200:
        description: Text extracted from the image
        schema:
          type: object
          properties:
            text:
              type: string
      400:
        description: Bad Request
        schema:
          type: object
          properties:
            error:
              type: string
      500:
        description: Internal Server Error
        schema:
          type: object
          properties:
            error:
              type: string
    """
    # Check if an image file is provided in the request
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400

    image = request.files['image']

    # Save the image temporarily
    temp_image_path = 'temp_image.png'
    image.save(temp_image_path)

    # Perform OCR using OCR.space Free OCR API
    try:
        ocr_url = 'https://api.ocr.space/parse/image'
        payload = {
            'apikey': OCR_API_KEY,
            'language': 'eng',  # You can specify the language(s) you want to use
        }

        with open(temp_image_path, 'rb') as image_file:
            files = {'image': (temp_image_path, image_file)}
            response = requests.post(ocr_url, data=payload, files=files)

        # Remove the temporary image file
        os.remove(temp_image_path)

        if response.status_code == 200:
            result = response.json()
            text = ' '.join([item['ParsedText'] for item in result['ParsedResults']])
            return jsonify({'text': text}), 200
        else:
            return jsonify({'error': f'OCR API error: {response.text}'}), response.status_code
    except Exception as e:
        return jsonify({'error': f'Error processing the image: {str(e)}'}), 500
    

# GPT 3.5 api    
@app.route('/gpt3.5', methods=['POST'])
def gpt():
    """
    GPT 3.5 API
    ---
    responses:
      200:
        description: Generated text from GPT 3.5
        schema:
          type: object
          properties:
            text:
              type: string
    """
    client = OpenAI()

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
            {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
        ]
    )

    return ({'text':completion.choices[0].message}), 200

if __name__ == '__main__':
    app.run(debug=True)
