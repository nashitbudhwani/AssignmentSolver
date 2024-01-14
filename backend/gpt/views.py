from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from openai import OpenAI
from decouple import config, Csv
import os

os.environ["OPENAI_API_KEY"] = config('OPENAI_API_KEY')

class ChatView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({'message': 'Hello, World!'})

    def post(self, request, *args, **kwargs):
        print(request.data)
        client = OpenAI()
        try:
            user_input = request.data.get('user_message')
            user_input = "What is the capital of India?"
            if not user_input:
                return Response({'error': 'Missing user_message in the request body'}, status=400)

            # Assuming the OpenAI client is initialized correctly
            completion = OpenAI().chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are an assignment solver. You are given a question and you have to answer it."},
                    {"role": "user", "content": user_input}
                ]
            )

            return Response({'answer': completion.choices[0].message.content}, status=200)
        except Exception as e:
            return Response({'error': f'Error processing the request: {str(e)}'}, status=500)
