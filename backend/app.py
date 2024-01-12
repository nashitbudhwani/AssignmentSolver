from flask import Flask, request, jsonify
from PIL import Image
import easyocr

app = Flask(__name__)

@app.route('/ocr', methods=['POST'])
def ocr():
    # Check if an image path is provided in the request
    if 'image_path' not in request.form:
        return jsonify({'error': 'No image path provided'}), 400

    image_path = request.form['image_path']

    # Perform OCR using easyocr
    try:
        reader = easyocr.Reader(['en'])  # You can specify the language(s) you want to use
        result = reader.readtext(image_path)

        # Extract text from the result
        text = ' '.join([item[1] for item in result])

        return jsonify({'text': text}), 200
    except Exception as e:
        return jsonify({'error': f'Error processing the image: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
