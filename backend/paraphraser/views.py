from rest_framework.views import APIView
from rest_framework.response import Response
from openai import OpenAI

def post(self, request, *args, **kwargs):
    try:
        input_text = request.data.get('input_text')

        if not input_text:
            return Response({'error': 'Missing input_text in the request data'}, status=status.HTTP_400_BAD_REQUEST)

        # Load pre-trained MarianMT model and tokenizer
        model_name = "Helsinki-NLP/opus-mt-en-ROMANCE"  # Replace with the desired model
        model = MarianMTModel.from_pretrained(model_name)
        tokenizer = MarianTokenizer.from_pretrained(model_name)

        # Tokenize the input text
        inputs = tokenizer(input_text, return_tensors="pt", max_length=512, truncation=True)

        # Generate paraphrased text
        outputs = model.generate(**inputs)

        # Decode the generated tokens
        paraphrased_text = tokenizer.batch_decode(outputs, skip_special_tokens=True)[0]

        return Response({'paraphrased_text': paraphrased_text}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': f'Error processing the request: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)