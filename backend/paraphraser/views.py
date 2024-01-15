from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from decouple import config
import requests

class ParaphraseView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            # Extract input_text from the request
            input_text = request.data.get('input_text')

            if not input_text:
                return Response({'error': 'Missing input_text in the request body'}, status=status.HTTP_400_BAD_REQUEST)

            API_URL = "https://api-inference.huggingface.co/models/tuner007/pegasus_paraphrase"
            headers = {"Authorization": f"Bearer {config('HUGGING_FACE_API_KEY')}"}

            def query(payload):
                response = requests.post(API_URL, headers=headers, json=payload)

                if response.status_code == 200:
                    return response.json()
                else:
                    return None  # Handle error response
            
            output = query({"inputs": input_text})
        
            if output:
                return Response({'paraphrased_text': output[0]['generated_text']}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Error in Hugging Face API response'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        except Exception as e:
            return Response({'error': f'Error processing the request: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
