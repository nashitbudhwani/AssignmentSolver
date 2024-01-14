from rest_framework.views import APIView
from rest_framework.response import Response
import requests
import os
from decouple import config, Csv


OCR_API_KEY = config('OCR_API_KEY')

class OCRView(APIView):
    def post(self, request, *args, **kwargs):
        if 'image' not in request.FILES:
            return Response({'error': 'No image file provided'}, status=400)

        image = request.FILES['image']
        temp_image_path = 'temp_image.png'

        try:
            ocr_url = 'https://api.ocr.space/parse/image'
            payload = {
                'apikey': OCR_API_KEY,
                'language': 'eng',
            }

            with open(temp_image_path, 'wb') as image_file:
                image_file.write(image.read())

            with open(temp_image_path, 'rb') as image_file:
                files = {'image': (temp_image_path, image_file)}
                response = requests.post(ocr_url, data=payload, files=files)

            os.remove(temp_image_path)

            if response.status_code == 200:
                result = response.json()
                text = ' '.join([item['ParsedText'] for item in result['ParsedResults']])
                return Response({'text': text}, status=200)
            else:
                return Response({'error': f'OCR API error: {response.text}'}, status=response.status_code)
        except Exception as e:
            return Response({'error': f'Error processing the image: {str(e)}'}, status=500)
