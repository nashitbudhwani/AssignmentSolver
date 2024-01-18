from rest_framework.views import APIView
from rest_framework.response import Response
import requests
import os
from django.core.files.uploadedfile import InMemoryUploadedFile
from decouple import config, Csv



class OCRView(APIView):
    API_URL = "https://api-inference.huggingface.co/models/microsoft/trocr-base-handwritten"
    HEADERS = {"Authorization": "Bearer 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"}

    def post(self, request, *args, **kwargs):
        try:
            # Check if 'image' key is present in request.FILES
            if 'image' not in request.FILES:
                return Response({'error': 'No image file provided'}, status=400)

            # Get the image from the request
            image = request.FILES['image']

            # Convert the image to binary data
            if not isinstance(image, InMemoryUploadedFile):
                return Response({'error': 'Invalid image file provided'}, status=400)

            file_data = image.read()

            # Make the API call
            response = requests.post(self.API_URL, headers=self.HEADERS, data=file_data)
            
            # Check if the API call was successful
            if response.status_code == 200:
                # Return the API response as JSON
                
                return Response({'text':response.json()[0]['generated_text']}, status=200)
            else:
                # Return an error response if the API call failed
                return Response({"error": "Failed to process the image"}, status=response.status_code)

        except Exception as e:
            # Handle any exceptions that may occur
            return Response({"error": str(e)}, status=500)