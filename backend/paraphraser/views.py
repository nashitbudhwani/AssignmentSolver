from rest_framework.views import APIView
from rest_framework.response import Response
from openai import OpenAI
from rest_framework import status
import os
from decouple import config, Csv

os.environ["OPENAI_API_KEY"] = config('OPENAI_API_KEY')

class ParaphraseView(APIView):
    def post(self, request, *args, **kwargs):
        input_text = request.data.get('input_text')
        return Response({'paraphrased_text': "hellow"}, status=status.HTTP_200_OK)
        if not input_text:
            return Response({'error': 'Missing input_text in the request body'}, status=status.HTTP_400_BAD_REQUEST)

        # Set your OpenAI API key
    
        client = OpenAI()
        # Use the OpenAI API for paraphrasing with text-davinci-003 engine
        

        completion = OpenAI().chat.completions.create(
                model="text-davinci-003",
                messages=[
                    {"role": "system", "content": "You are an assignment solver. You are given a question and you have to answer it."},
                    {"role": "user", "content": input_text}
                ]
            )

        paraphrased_text = completion.choices[0].message.content

        return Response({'paraphrased_text': paraphrased_text}, status=status.HTTP_200_OK)
