from rest_framework.views import APIView
from rest_framework.response import Response
from openai import OpenAI

class ParaphraseView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            input_text = request.data.get('input_text')

            if not input_text:
                return Response({'error': 'Missing input_text in the request body'}, status=400)

            # Use the OpenAI API for paraphrasing
            response = OpenAI().chat.completions.create(
                engine="text-davinci-003",
                prompt=input_text,
                max_tokens=50,
                temperature=0.7,
                n=1,
            )

            paraphrased_text = response.choices[0].text.strip()

            return Response({'paraphrased_text': paraphrased_text}, status=200)
        except Exception as e:
            return Response({'error': f'Error processing the request: {str(e)}'}, status=500)
